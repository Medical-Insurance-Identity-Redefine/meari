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

- 1 개발환경 및 패키지 설치 관련

- 2 전처리 및 EDA

- 3 머신러닝

- 4 파이프라인 관련

- 5 run this folder 파일 설명

- Jupyter Notebook 실행시 유의 사항

- Python Version 참조

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


### 1. 개발환경 및 패키지 설치 관련
   
	건강보험심사평가원 내부의 폐쇄망 PC에서 데이터 전처리와 머신러닝을 진행   
	OS는 Windows 64-bit   
	Pycharm으로 프로그래밍   
	python 3.8.8   
	패키지는 whl파일로 직접 설치 (package폴더 참고)   
   
   
### 2. 전처리 및 EDA
   
	데이터 전처리 및 EDA 시각화 코드 : code+visualization\preprocessing+EDA\preprocessing+visualization.py   
	데이터 전처리 과정별로 캡쳐한 결과 : code+visualization\preprocessing+EDA\preprocessing procedure capture   
	EDA에 대한 결과 : code+visualization\preprocessing+EDA\EDA   
	건강보험심사평가원에서 받은 진료비확인신청 데이터에 대한 raw data와 추가로 요청한 '요양종별코드-요양기호' 텍스트 파일은 더미를 만들지 못함   
	전처리 최종 결과에 대한 더미(즉, 머신러닝의 input data)는 임의로 제작(realLastDF.csv)   
   
   

### 3. 머신러닝
   
	code+visualization\ML에 5개의 머신러닝 관련 python 파일과 머신러닝 코드의 input file인 realLastDF.csv가 존재   
	1) xgboost, catboost, random forest, lightgbm을 학습시킨 파일   
	2) lightgbm 성능 고도화 파일    
	3) 파이프라인에 필요한 model과 label encoder 객체를 저장하는 파일   
   
	머신러닝 실행 결과에 대한 자료가 code+visualization\ML_results에 텍스트파일과 이미지파일로 존재   
   
   
   
### 4. 파이프라인 관련
   
	code+visualization\pipeline   
	1) 라벨인코더 객체 파일 9개   
	2) lightgbm model save 파일 1개   
   
      
      
### 5. run this folder 파일 설명
   
	code+visualization\run this folder   
	run this folder 전체를 주피터노트북에 올려서 Meari_final_code.ipynb 실행   
   
	5-1 최종 코드 관련   
	1) Make_dictionary : 사전 구축 코드 파일   
	2) Meari_final_code : OCR, NLP, ML 사용 코드 파일	   
	   
	5-2 OCR 관련   
	1) doclmage2.jpg : input file ( 진료비 세부내역서 )   
	2) hospCode.jpg ( 코드 결과물, 재생성 )   
	3) patientPK.jpg ( 코드 결과물, 재생성 )   
	4) croppedImage.jpg ( 코드 결과물, 재생성 )   
	5) data : nanonets 송신결과 파일 ( 재생성 )   
	6) meari-322801-754104bbf5e4a : google API Key   
	7) patient : 환자 정보에 대한 table detection 코드 결과물   
	8) diagnosis : 진료 받은 사항에 대한 table detection 코드 결과물   
	   
	5-3 사전 관련   
	1) stem_MethodDeleted.txt : rhino에 기본으로 탑재 된 명칭 사전 -> 수정 / anaconda3 -> Lib -> site-packages -> rhinoMorph -> resource 파일에 stem_MethodDeleted.txt 교체   
	2) insurance.txt : 급여 사전   
	3) insurance_non.txt : 비급여 사전   
	4) Dict_list.csv : 급여 명칭 csv 파일   
	5) Dict_list_non.csv : 비급여 명칭 csv 파일   
	   
	5-4 머신러닝 관련 : Meari_final_code 주석 참고   
       
          
             
             
             

### Jupyter Notebook 실행시 유의 사항
1) run this folder를 그대로 업로드 -> Meari_final_code.ipynb 코드 실행 -> cell -> run all 실행    
   
2) pip install ~  or import ~ 오류 해결 방법 : package version check -> version에 맞는 package or library download   

   
### Python Version 참조
absl-py                            0.13.0   
addict                             2.4.0   
alabaster                          0.7.12   
anaconda-client                    1.7.2   
anaconda-navigator                 2.0.3   
anaconda-project                   0.9.1   
anyio                              2.2.0   
appdirs                            1.4.4   
argh                               0.26.2   
argon2-cffi                        20.1.0   
asn1crypto                         1.4.0   
astroid                            2.5   
astropy                            4.2.1   
astunparse                         1.6.3   
async-generator                    1.10   
atomicwrites                       1.4.0   
attrs                              20.3.0   
autopep8                           1.5.6   
Babel                              2.9.0   
backcall                           0.2.0   
backports.functools-lru-cache      1.6.4   
backports.shutil-get-terminal-size 1.0.0   
backports.tempfile                 1.0   
backports.weakref                  1.0.post1   
bcrypt                             3.2.0   
beautifulsoup4                     4.9.3   
bitarray                           1.9.2   
bkcharts                           0.2   
black                              19.10b0   
bleach                             3.3.0   
bokeh                              2.3.2   
boto                               2.49.0   
Bottleneck                         1.3.2   
branca                             0.4.2   
brotlipy                           0.7.0   
cachetools                         4.2.2   
certifi                            2020.12.5   
cffi                               1.14.5   
chardet                            4.0.0   
chromedriver                       2.24.1   
chromedriver-autoinstaller         0.2.2   
click                              7.1.2   
cloudpickle                        1.6.0   
clyent                             1.2.2   
colorama                           0.4.4   
comtypes                           1.1.9   
conda                              4.10.3   
conda-build                        3.21.4   
conda-content-trust                0+unknown   
conda-package-handling             1.7.3   
conda-repo-cli                     1.0.4   
conda-token                        0.3.0   
conda-verify                       3.4.2   
contextlib2                        0.6.0.post1   
cryptography                       3.4.7   
cycler                             0.10.0   
Cython                             0.29.23   
cytoolz                            0.11.0   
dask                               2021.4.0   
decorator                          5.0.6   
defusedxml                         0.7.1   
diff-match-patch                   20200713   
distributed                        2021.4.0   
docutils                           0.17   
easyocr                            1.4   
entrypoints                        0.3   
et-xmlfile                         1.0.1   
fastcache                          1.1.0   
filelock                           3.0.12   
flake8                             3.9.0   
Flask                              1.1.2   
flatbuffers                        1.12   
folium                             0.12.1   
fsspec                             0.9.0    
future                             0.18.2    
gast                               0.4.0    
gevent                             21.1.2    
glob2                              0.7   
google-api-core                    2.0.1   
google-auth                        1.33.0   
google-auth-oauthlib               0.4.4   
google-cloud-vision                2.4.2   
google-pasta                       0.2.0   
googleapis-common-protos           1.53.0   
googlemaps                         4.4.5   
greenlet                           1.0.0   
grpcio                             1.34.1   
h5py                               3.1.0   
HeapDict                           1.0.1    
html5lib                           1.1    
idna                               2.10    
imagecodecs                        2021.3.31    
imageio                            2.9.0    
imagesize                          1.2.0    
importlib-metadata                 3.10.0    
iniconfig                          1.1.1    
intervaltree                       3.1.0   
ipykernel                          5.3.4    
ipython                            7.22.0   
ipython-genutils                   0.2.0   
ipywidgets                         7.6.3   
isort                              5.8.0   
itsdangerous                       1.1.0   
jdcal                              1.4.1   
jedi                               0.17.2    
Jinja2                             2.11.3   
joblib                             1.0.1   
JPype1                             1.3.0   
json5                              0.9.5    
jsonschema                         3.2.0   
jupyter                            1.0.0   
jupyter-client                     6.1.12   
jupyter-console                    6.4.0   
jupyter-core                       4.7.1   
jupyter-packaging                  0.7.12   
jupyter-server                     1.4.1   
jupyterlab                         3.0.14   
jupyterlab-pygments                0.1.2   
jupyterlab-server                  2.4.0   
jupyterlab-widgets                 1.0.0   
Keras                              2.4.3   
keras-nightly                      2.5.0.dev2021032900   
Keras-Preprocessing                1.1.2   
keyring                            22.3.0   
kiwisolver                         1.3.1   
lazy-object-proxy                  1.6.0   
libarchive-c                       2.9   
lightgbm                           3.2.1   
llvmlite                           0.36.0   
locket                             0.2.1   
lxml                               4.6.3   
Markdown                           3.3.4   
MarkupSafe                         1.1.1   
matplotlib                         3.3.4   
mccabe                             0.6.1   
menuinst                           1.4.16   
mistune                            0.8.4   
mkl-fft                            1.3.0   
mkl-random                         1.2.1   
mkl-service                        2.3.0   
mmcv                               0.4.3   
mock                               4.0.3   
more-itertools                     8.7.0   
mpmath                             1.2.1     
msgpack                            1.0.2     
multipledispatch                   0.6.0      
mypy-extensions                    0.4.3         
navigator-updater                  0.2.1       
nbclassic                          0.2.6        
nbclient                           0.5.3      
nbconvert                          6.0.7       
nbformat                           5.1.3        
nest-asyncio                       1.5.1       
networkx                           2.5     
nltk                               3.6.1      
nose                               1.3.7      
notebook                           6.3.0         
numba                              0.53.1   
numexpr                            2.7.3    
numpy                              1.19.5        
numpydoc                           1.1.0         
oauthlib                           3.1.1      
olefile                            0.46         
opencv-python                      4.5.2.54       
openpyxl                           3.0.7        
opt-einsum                         3.3.0         
packaging                          20.9       
pandas                             1.3.1         
pandocfilters                      1.4.3           
paramiko                           2.7.2         
parso                              0.7.0          
partd                              1.2.0      
path                               15.1.2         
pathlib2                           2.3.5         
pathspec                           0.7.0         
patsy                              0.5.1           
pdf2image                          1.16.0            
pep8                               1.7.1           
pexpect                            4.8.0       
pickleshare                        0.7.5        
Pillow                             6.2.1         
pip                                21.2.4        
pkginfo                            1.7.0          
pluggy                             0.13.1         
ply                                3.11         
prometheus-client                  0.10.1             
prompt-toolkit                     3.0.17        
proto-plus                         1.19.0          
protobuf                           3.17.3         
psutil                             5.8.0            
ptyprocess                         0.7.0       
py                                 1.10.0        
pyasn1                             0.4.8      
pyasn1-modules                     0.2.8       
pycodestyle                        2.6.0        
pycosat                            0.6.3       
pycparser                          2.20        
pycurl                             7.43.0.6         
pydocstyle                         6.0.0          
pyerfa                             1.7.3      
pyflakes                           2.2.0       
Pygments                           2.8.1       
pylint                             2.7.4         
pyls-black                         0.4.6         
pyls-spyder                        0.3.2        
PyNaCl                             1.4.0      
pyodbc                             4.0.0-unsupported        
pyOpenSSL                          20.0.1           
pyparsing                          2.4.7            
pyreadline                         2.1        
pyrsistent                         0.17.3         
PySocks                            1.7.1         
pytesseract                        0.3.8            
pytest                             6.2.3        
python-bidi                        0.4.2          
python-dateutil                    2.8.1         
python-jsonrpc-server              0.4.0         
python-language-server             0.36.2          
pytz                               2021.1          
PyWavelets                         1.1.1           
pywin32                            227            
pywin32-ctypes                     0.2.0          
pywinpty                           0.5.7             
PyYAML                             5.4.1           
pyzmq                              20.0.0          
QDarkStyle                         2.8.1          
QtAwesome                          1.0.2           
qtconsole                          5.0.3           
QtPy                               1.9.0          
regex                              2021.4.4          
requests                           2.25.1          
requests-oauthlib                  1.3.0          
rhinoMorph                         3.8.0.0         
rope                               0.18.0          
rsa                                4.7.2          
Rtree                              0.9.7          
ruamel-yaml-conda                  0.15.100          
scheduler                          0.6.1          
scikit-image                       0.18.1         
scikit-learn                       0.24.1          
scipy                              1.4.1             
seaborn                            0.11.1          
selenium                           3.141.0         
Send2Trash                         1.5.0                
setuptools                         52.0.0.post20210125            
simplegeneric                      0.8.1           
singledispatch                     0.0.0         
sip                                4.19.13         
six                                1.15.0           
sklearn                            0.0            
sniffio                            1.2.0              
snowballstemmer                    2.1.0          
sortedcollections                  2.1.0          
sortedcontainers                   2.3.0          
soupsieve                          2.2.1         
Sphinx                             4.0.1         
sphinxcontrib-applehelp            1.0.2         
sphinxcontrib-devhelp              1.0.2        
sphinxcontrib-htmlhelp             1.0.3          
sphinxcontrib-jsmath               1.0.1          
sphinxcontrib-qthelp               1.0.3           
sphinxcontrib-serializinghtml      1.1.4          
sphinxcontrib-websupport           1.2.4              
spyder                             4.2.5       
spyder-kernels                     1.10.2       
SQLAlchemy                         1.4.7          
statsmodels                        0.12.2               
sympy                              1.8           
tables                             3.6.1           
tblib                              1.7.0           
tensorboard                        2.5.0          
tensorboard-data-server            0.6.1           
tensorboard-plugin-wit             1.8.0          
tensorflow                         2.5.0         
tensorflow-estimator               2.5.0            
termcolor                          1.1.0          
terminado                          0.9.4              
terminaltables                     3.1.0           
testpath                           0.4.4           
textdistance                       4.2.1           
threadpoolctl                      2.1.0           
three-merge                        0.1.1         
tifffile                           2021.4.8          
toml                               0.10.2          
toolz                              0.11.1           
torch                              1.9.0                 
torchvision                        0.10.0        
tornado                            6.1         
tqdm                               4.59.0         
traitlets                          5.0.5          
typed-ast                          1.4.2           
typeguard                          2.12.1          
typing-extensions                  3.7.4.3          
ujson                              4.0.2         
unicodecsv                         0.14.1         
urllib3                            1.26.4        
watchdog                           1.0.2         
wcwidth                            0.2.5         
webencodings                       0.5.1           
Werkzeug                           1.0.1        
wheel                              0.36.2         
widgetsnbextension                 3.5.1         
win-inet-pton                      1.1.0         
win-unicode-console                0.5              
wincertstore                       0.2            
wrapt                              1.12.1         
xlrd                               2.0.1      
XlsxWriter                         1.3.8         
xlwings                            0.23.0         
xlwt                               1.3.0       
xmltodict                          0.12.0          
yapf                               0.31.0          
zict                               2.0.0          
zipp                               3.4.1         
zope.event                         4.5.0         
zope.interface                     5.3.0             


     
     
      
   
   
### Team_MEARI

| <IMG src="https://github.com/yooseonghyeon.png?size=100" width="150"> | <IMG src="https://github.com/JubyKim.png?size=100" width="150"> | <IMG src="https://github.com/ilovetayy.png?size=100" width="150">| <IMG src="https://github.com/Giggle1998.png?size=100" width="150">
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            유성현                            |                            김주은                            |                            이규영                            |                            이기표                            |

