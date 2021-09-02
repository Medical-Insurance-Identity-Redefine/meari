# MEARI

<img src="https://user-images.githubusercontent.com/87626172/131877946-3ad59fb4-c608-45d7-b744-97f6dd0d85fd.png" width="135" align = "left">

```
🍎 2021 데이터청년캠퍼스 <빅리더 아카데미> 🍎

Big Leader Academy
- 2021. 06. 28 ~ 2021. 08. 30

AI를 활용한 비급여 진료비 자가점검 서비스😊
```


<br/>

## 목차

- 개발환경 및 사용한 라이브러리

- 서비스 workflow

- 기능 개발여부/담당자

- 핵심기능 구현 방법

- Team_Meari


### 개발환경 및 사용한 라이브러리
|                       라이브러리                    |               목적                 |      
| :------------------------------------------------: | :------------------------------: |
|                        pandas                      |        데이터 분석 및 전처리      |
|                       lightgbm                     |           머신러닝 모델          |
|                       xgboost                      |           머신러닝 모델          |
|                       catboost                     |           머신러닝 모델          |
|                       sklearn                      |     머신러닝 모델, 성능지표 등    | 
|                       optuna                       |       하이퍼파라미터 최적화       |
|                       pickle                       |   머신러닝 모델 저장 및 불러오기  |
|                 matplotlib, seaborn                |            데이터 시각화         |
|                       Nanonets                     |              OCR API            |
|                 google cloud vision                |              OCR API            |
|                        openCV                      |              영상처리            |
|                      rhinoMorph                    |            형태소분석기          |
<br>

### 서비스 workflow
![image](https://user-images.githubusercontent.com/87626172/131874143-de4d3444-1cca-4d11-9b9a-94a83ba880e0.png)


### 기능 개발여부/담당자

|    기술     |        기능        | 담당자 | 구현 여부 |
| :---------: | :---------------------: | :----: | :-------: |
|  데이터전처리   |        데이터정제         |  성현  |     ✅     |
|  OpenCV + OCR   |        서류읽어오기         |  주은  |     ✅     |
|   NLP    |         사전제작          |  기표  |     ✅     |
|  Machine Learning   |        예측모델제작        |  규영  |     ✅     |
|      어플제작       |        프로토타입         |  주은  |     ✅     |



### 파트별 중요 코드
1. EDA

~~~python
le = preprocessing.LabelEncoder()
df_encoded = df

for i in df_encoded.columns[df_encoded.dtypes == 'object']:
    df_encoded[i] = le.fit_transform(list(df_encoded[i]))

def crammersV(var1, var2):
    crosstab = np.array(pd.crosstab(var1, var2, rownames=None, colnames=None))
    stat = chi2_contingency(crosstab)[0]
    obs = np.sum(crosstab)
    mini = min(crosstab.shape) - 1
    return (stat/(obs*mini))

rows = []
for var1 in df_encoded:
    col = []
    for var2 in df_encoded:
        crammers = crammersV(df_encoded[var1], df_encoded[var2])
        col.append(round(crammers,2))
    rows.append(col)

crammers_res = np.array(rows)
df_new = pd.DataFrame(crammers_res, columns=df_encoded.columns, index=df_encoded.columns)
mask = np.zeros_like(df_new, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

with sns.axes_style('white'):
    plt.rc('font', family='Malgun Gothic')
    ax = sns.heatmap(df_new, mask=mask, vmin=0., vmax=1., square=True, annot=True, cmap='YlGnBu')
plt.show()
   }
   
~~~

2. OpenCV + OCR

~~~python
# testImage 기준, 요양기호정보cell대비 환자등록번호 cell의 크기는 0.42었음.
# 사용자가 사진을 찍는 방향이나 각도에 따라 달라질 수 있으니 적당한 범위를 정해준다.
for index , item in enumerate(areaList):
    if 0.3 < pkArea / item < 0.55:
        x = xList[index]
        y = yList[index]
        h = hList[index]
        w = wList[index]

crop_img = image[y:y+h, x:x+w]

#요양정보 cell의 칼럼.
cv2.imwrite('hospCode.jpg',crop_img)
hospCode=cv2.imread('hospCode.jpg')
~~~

3. NLP

~~~python
morphed_data_each = rhinoMorph.onlyMorph_list(rn, data_each, pos =['NNG', 'NNP','SL'], eomi = True)
~~~


4. Machine Learning
~~~python
X = df.drop(['환불여부'], axis=1)
y = df['환불여부']

def objective(trial):
    # train과 test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # oversampling하는 경우, train data에 대해서 oversampling하기 
    # fit할 때 X_train, y_train 대신 X_resampled, y_resampled로 바꿀 것 
    # X_resampled, y_resampled = sm.fit_resample(X_train, y_train)

    # hyperparameter value 후보군 설정
    param = {
        "objective": "binary",
        "metric": "binary_logloss",
        "verbosity": -1,
        "boosting_type": "gbdt",
        "lambda_l1": trial.suggest_float("lambda_l1", 1e-8, 10.0, log=True),
        "lambda_l2": trial.suggest_float("lambda_l2", 1e-8, 10.0, log=True),
        "num_leaves": trial.suggest_int("num_leaves", 2, 256),
        "feature_fraction": trial.suggest_float("feature_fraction", 0.4, 1.0),
        "bagging_fraction": trial.suggest_float("bagging_fraction", 0.4, 1.0),
        "bagging_freq": trial.suggest_int("bagging_freq", 1, 7),
        "min_child_samples": trial.suggest_int("min_child_samples", 5, 100),
        "learning_rate": trial.suggest_float("learning_rate", 1e-8, 1.0, log=True),
        "n_estimators": trial.suggest_int("n_estimators", 1, 5000)
    }

    model = lgb.LGBMClassifier(**param, boost_from_average = False)
    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=200, verbose=False)

    # best threshold를 계산하기 위한 과정 
    preds = model.predict_proba(X_test)
    p = preds[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, p)

    numerator = 2 * precision * recall
    denom = recall + precision
    fl_scores = np.divide(numerator, denom, out=np.zeros_like(denom), where=(denom!=0))
    max_f1 = np.max(fl_scores)
    max_f1_thresh = thresholds[np.argmax(fl_scores)]

    y_prob_pred = (model.predict_proba(X_test)[:, 1] >= max_f1_thresh).astype(bool)

    print("best threshold : " + str(max_f1_thresh))

    print(classification_report(y_test, y_prob_pred))
    print(confusion_matrix(y_test, y_prob_pred))
    print(accuracy_score(y_test, y_prob_pred))
    print(f1_score(y_test, y_prob_pred))
    print(roc_auc_score(y_test, y_prob_pred))

    return max_f1

# 하이퍼파라미터 최적화
# objective 함수 100번 실행
# objective 함수의 return value인 f1 score가 maximize되도록 하는 방향으로 
study = optuna.create_study(
    pruner = optuna.pruners.MedianPruner(n_startup_trials=5), direction='maximize')

study.optimize(objective, n_trials=100)
~~~


5. Application
~~~swift
func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            if let pickedImage = info[.originalImage] as? UIImage {
                    imageView.contentMode = .scaleAspectFit
                    imageView.image = pickedImage
            }
            dismiss(animated: true, completion: nil)
            var sv = UIView()
            sv = UIViewController.displaySpinner(onView: self.view)
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                UIViewController.removeSpinner(spinner: sv)
                let alert = UIAlertController(title: "비급여 진료비 확인 서비스 대상입니다.", message: """
                    92%의 확률로 환불이 가능한 항목입니다.
                    해당 서비스를 신청하시려면 서류제출하기 버튼을 눌러주세요.
                    """, preferredStyle: .alert)
                let defaultAction = UIAlertAction(title: "OK", style: .destructive, handler : nil)
                alert.addAction(defaultAction)
                self.present(alert, animated: true, completion: nil)
            }
            self.submitButton.isHidden = false
        }
~~~

### Jupyter Notebook 실행시 유의 사항
1) run this folder를 그대로 업로드 -> Meari_final_code.ipynb 코드 실행 -> cell -> run all 실행    
   
2) pip install ~  or import ~ 오류 해결 방법 : package version check -> version에 맞는 package or library download   
   
   
### Team_MEARI

| <IMG src="https://github.com/yooseonghyeon.png?size=100" width="150"> | <IMG src="https://github.com/JubyKim.png?size=100" width="150"> | <IMG src="https://github.com/ilovetayy.png?size=100" width="150">| <IMG src="https://github.com/Giggle1998.png?size=100" width="150">
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            유성현                            |                            김주은                            |                            이규영                            |                            이기표                            |

