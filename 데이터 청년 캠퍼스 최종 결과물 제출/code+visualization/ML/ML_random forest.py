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
from sklearn.ensemble import RandomForestClassifier

# warning 무시 
warnings.filterwarnings('ignore')

# 데이터 읽어오기
df = pd.read_csv(r'./realLastDF.csv', encoding='cp949')

print(df.info())
df.drop('Unnamed: 0', axis=1, inplace=True)

# 범주형 변수 string(object)으로 변환
df['요양기호'] = df['요양기호'].astype('str')
df['환불여부'] = df['환불여부'].astype('str')
df['환자성별'] = df['환자성별'].astype('str')
df['연도 + 반기'] = df['연도 + 반기'].astype('str')

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # hyperparameter value 후보군 설정
    param = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 5000),
        "max_depth": trial.suggest_int("max_depth", 3, 10),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 50),
        "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 60),
        "max_features": trial.suggest_categorical("max_features", ["auto", "sqrt", "log2"]),
    }

    model = RandomForestClassifier(**param)
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
study = optuna.create_study(
    pruner = optuna.pruners.MedianPruner(n_startup_trials=5), direction='maximize')

study.optimize(objective, n_trials=100)

# best parameter 출력
print(study.best_params)
# best trial 출력 
print(study.best_trial)

fig = optuna.visualization.plot_param_importances(study)
fig.show()