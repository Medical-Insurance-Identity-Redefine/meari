import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedShuffleSplit, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score,roc_auc_score, classification_report
from sklearn.inspection import permutation_importance
from optuna import Trial, visualization

from optuna.samplers import TPESampler
from sklearn.metrics import mean_squared_error
import lightgbm as lgb
import xgboost as xgb
from sklearn import svm
import optuna
import functools
import warnings

# matplotlib 한글 깨짐 해결
mat.rcParams['font.family'] = 'Malgun Gothic'

plt.style.use('seaborn-pastel')

# warning 무시
warnings.filterwarnings('ignore')

# 데이터 읽어오기
df = pd.read_csv(r"realLastDF.csv", encoding='cp949')
# print(df.info())

df.drop('Unnamed: 0', axis=1, inplace=True)

# 범주형 변수 string(object)으로 변환
df['요양기호'] = df['요양기호'].astype('str')
df['환불여부'] = df['환불여부'].astype('str')
df['환자성별'] = df['환자성별'].astype('str')
df['연도 + 반기'] = df['연도 + 반기'].astype('str')
# print(df.info())

# object type 변수는 라벨인코딩하기
# 환자 만 나이 제외하고 모두 object type
le = LabelEncoder()
for i in df.columns[df.dtypes == "object"]:
    df[i] = le.fit_transform(list(df[i]))

# feature와 target
y = df['환불여부']
X = df.drop('환불여부', axis = 1)

def objective(trial):
    # train과 test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=42, stratify= y)

    # hyperparameter value 후보군 설정
    param = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "booster": trial.suggest_categorical("booster", ["gbtree", "gblinear", "dart"]),
        "lambda": trial.suggest_float("lambda", 1e-8, 1.0, log=True),
        "alpha": trial.suggest_float("alpha", 1e-8, 1.0, log=True),
        'random_state': trial.suggest_categorical('random_state', [24, 48,2020]),
        'booster': 'gbtree',
        'max_depth': trial.suggest_int("max_depth", 1, 9),
        'eta': trial.suggest_float("eta", 1e-8, 1.0, log=True),
        'gamma': trial.suggest_float("gamma", 1e-8, 1.0, log=True),
        'grow_policy': trial.suggest_categorical("grow_policy", ["depthwise", "lossguide"])
    }
    
    model = xgb.XGBClassifier(**param, n_estimators=5000)

    model.fit(X_train, y_train)

    # 임곗값은 0.4로 설정 
    threshold = 0.4
    preds = model.predict_proba(X_test)
    p = (preds[:, 1] > threshold).astype('int')

    print(classification_report(y_test, p))
    print(confusion_matrix(y_test, p))
    print(f1_score(y_test, p))
    return f1_score(y_test, p)

# 하이퍼파라미터 최적화
# objective 함수 100번 실행
# objective 함수의 return value인 f1 score가 maximize되도록 하는 방향으로
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

# best parameter 출력
print(study.best_params)
# best trial 출력 
print(study.best_trial)

fig = optuna.visualization.plot_param_importances(study)
fig.show()