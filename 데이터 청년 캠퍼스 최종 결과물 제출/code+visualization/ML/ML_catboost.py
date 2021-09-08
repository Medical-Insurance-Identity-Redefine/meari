import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score, roc_auc_score
import warnings
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
import optuna
from catboost import CatBoostClassifier
import functools

# warning 무시
warnings.filterwarnings('ignore')

# 데이터 읽어오기
df = pd.read_csv(r'./realLastDF.csv', encoding='cp949')
# print(df.nunique())
print(df.info())

df.drop('Unnamed: 0', axis=1, inplace=True)

# 범주형 변수 string(object)으로 변환
df['요양기호'] = df['요양기호'].astype('str')
df['환불여부'] = df['환불여부'].astype('str')
df['환자성별'] = df['환자성별'].astype('str')
df['연도 + 반기'] = df['연도 + 반기'].astype('str')

print('=========================================================')
print(df.info())
print(df.nunique())
print(df.isna().sum())

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

    # hyperparameter value 후보군 설정 
    param = {
        'objective' : trial.suggest_categorical('objective', ['Logloss','CrossEntropy']),
        'colsample_bylevel' : trial.suggest_float('colsample_bylevel', 0.01, 0.1),
        'depth' : trial.suggest_int('depth', 1, 16),
        'boosting_type' : trial.suggest_categorical('boosting_type', ['Ordered','Plain']),
        'bootstrap_type' : trial.suggest_categorical('bootstrap_type', ['Bayesian','Bernoulli','MVS']),
        'learning_rate' : trial.suggest_float('learning_rate', 0.0001, 1.0, log=True)
    }

    if param['bootstrap_type'] == 'Bayesian':
        param['bagging_temperature'] = trial.suggest_float('bagging_temperature', 0, 10)
    elif param['bootstrap_type'] == 'Bernoulli':
        param['subsample'] = trial.suggest_float('subsample', 0.1, 1)

    cb = CatBoostClassifier(**param, n_estimators=5000)

    # 학습시작
    cb.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False, early_stopping_rounds=300)

    # 임곗값은 0.4로 설정 
    threshold = 0.4
    preds = cb.predict_proba(X_test)
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

