import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, roc_auc_score, f1_score, roc_curve, precision_recall_curve
import seaborn as sns
from sklearn.metrics import classification_report
from lightgbm import plot_importance
from sklearn.inspection import permutation_importance
import warnings
import optuna
import pickle
import matplotlib.pyplot as plt
from numpy import sqrt
from numpy import argmax
from imblearn.over_sampling import SMOTE

# matplotlib 한글 깨짐 해결
plt.rc('font',family='Malgun Gothic')

# warning 무시
warnings.filterwarnings('ignore')

# 데이터 읽어오기
df = pd.read_csv(r'realLastDF.csv', encoding='cp949')
# print(df.info())

df.drop('Unnamed: 0', axis=1, inplace=True)

# 범주형 변수 string(object)으로 변환
df['요양기호'] = df['요양기호'].astype('str')
df['환불여부'] = df['환불여부'].astype('str')
df['환자성별'] = df['환자성별'].astype('str')
df['연도 + 반기'] = df['연도 + 반기'].astype('str')
# print(df.info())

# ==============================1) 나이 그대로=======================================


# ===============================2) 나이 20 단위로=========================================
def category_age(x):
    if x <= 20 :
        return 0
    elif x <= 40 :
        return 1
    elif x <= 60:
        return 2
    elif x <= 80:
        return 3
    else:
        return 4

# df['환자 만 나이'] = df['환자 만 나이'].apply(category_age)

# =================================3) minmaxscaler===========================================
# sc = MinMaxScaler()
# df[['환자 만 나이']] = sc.fit_transform((df[['환자 만 나이']]))

# ======================================================================================
# oversampling 준비 
sm = SMOTE(sampling_strategy='auto')

# object type 변수는 라벨인코딩하기
# 환자 만 나이 제외하고 모두 object type
le = LabelEncoder()
for i in df.columns[df.dtypes == "object"]:
    df[i] = le.fit_transform(list(df[i]))

# feature와 target
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

# best parameter 출력
print(study.best_params)
# best trial 출력
print(study.best_trial)

fig = optuna.visualization.plot_optimization_history(study)
fig.show()

fig = optuna.visualization.plot_param_importances(study)
fig.show()
