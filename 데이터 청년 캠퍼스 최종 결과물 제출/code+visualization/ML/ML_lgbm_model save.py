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
import matplotlib.pyplot as plt
from numpy import sqrt
from numpy import argmax
import pickle

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
# sm = SMOTE(sampling_strategy='auto')

# 변수별로 라벨인코더 객체 생성 
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
le5 = LabelEncoder()
le6 = LabelEncoder()
le7 = LabelEncoder()
le8 = LabelEncoder()
le9 = LabelEncoder()
le10 = LabelEncoder()


print(df.info())

#for i in df.columns[df.dtypes == "object"]:
#    df[i] = le.fit_transform(list(df[i]))

# object type 변수 라벨인코딩한 후, 라벨인코더 객체 파일로 저장하기
df['보험자구분'] = le1.fit_transform(df['보험자구분'])
np.save('classes_보험자구분.npy',le1.classes_)

df['요양기호'] = le2.fit_transform(df['요양기호'])
np.save('classes_요양기호.npy',le2.classes_)

df['진료과목'] = le3.fit_transform(df['진료과목'])
np.save('classes_진료과목.npy',le3.classes_)

df['상병기호'] = le4.fit_transform(df['상병기호'])
np.save('classes_상병기호.npy',le4.classes_)

df['항코드(중분류)'] = le5.fit_transform(df['항코드(중분류)'])
np.save('classes_항코드(중분류).npy',le5.classes_)

df['분류코드(기관)'] = le6.fit_transform(df['분류코드(기관)'])
np.save('classes_분류코드(기관).npy',le6.classes_)

df['구분'] = le7.fit_transform(df['구분'])
np.save('classes_구분.npy',le7.classes_)

df['환불여부'] = le8.fit_transform(df['환불여부'])
np.save('classes_환불여부.npy',le8.classes_)

df['환자성별'] = le9.fit_transform(df['환자성별'])
np.save('classes_환자성별.npy',le9.classes_)

df['연도 + 반기'] = le10.fit_transform(df['연도 + 반기'])
np.save('classes_반기.npy',le10.classes_)

# feature 와 target
X = df.drop(['환불여부'], axis=1)
y = df['환불여부']

# def objective(trial):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
#     # X_resampled, y_resampled = sm.fit_resample(X_train, y_train)
#
#     param = {
#         "objective": "binary",
#         "metric": "binary_logloss",
#         "verbosity": -1,
#         "boosting_type": "gbdt",
#         "lambda_l1": trial.suggest_float("lambda_l1", 1e-8, 10.0, log=True),
#         "lambda_l2": trial.suggest_float("lambda_l2", 1e-8, 10.0, log=True),
#         "num_leaves": trial.suggest_int("num_leaves", 2, 256),
#         "feature_fraction": trial.suggest_float("feature_fraction", 0.4, 1.0),
#         "bagging_fraction": trial.suggest_float("bagging_fraction", 0.4, 1.0),
#         "bagging_freq": trial.suggest_int("bagging_freq", 1, 7),
#         "min_child_samples": trial.suggest_int("min_child_samples", 5, 100),
#         "learning_rate": trial.suggest_float("learning_rate", 1e-8, 1.0, log=True),
#         "n_estimators": trial.suggest_int("n_estimators", 1, 5000)
#     }
#
#     model = lgb.LGBMClassifier(**param, boost_from_average = False)
#     model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=200, verbose=False)
#
#     preds = model.predict_proba(X_test)
#     p = preds[:, 1]
#     precision, recall, thresholds = precision_recall_curve(y_test, p)
#
#     numerator = 2 * precision * recall
#     denom = recall + precision
#     fl_scores = np.divide(numerator, denom, out=np.zeros_like(denom), where=(denom!=0))
#     max_f1 = np.max(fl_scores)
#     max_f1_thresh = thresholds[np.argmax(fl_scores)]
#
#     y_prob_pred = (model.predict_proba(X_test)[:, 1] >= max_f1_thresh).astype(bool)
#
#     print("best threshold : " + str(max_f1_thresh))
#
#     print(classification_report(y_test, y_prob_pred))
#     print(confusion_matrix(y_test, y_prob_pred))
#     print(accuracy_score(y_test, y_prob_pred))
#     print(f1_score(y_test, y_prob_pred))
#     print(roc_auc_score(y_test, y_prob_pred))
#
#     return max_f1

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# X_resampled, y_resampled = sm.fit_resample(X_train, y_train)

# 앞서 실험했던 best parameter 넣어주기 
model = lgb.LGBMClassifier(lambda_l1=0.00022639590292560866, lambda_l2=7.99703215738238e-05, num_leaves=203, feature_fraction=0.45280215034201693,
                            bagging_fraction=0.7671116599998257, bagging_freq=3, min_child_samples=7,
                            learning_rate =0.012508709954831658, n_estimators=4496, boost_from_average = False)

model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=200, verbose=False)

# model save
file_name = 'lgbm_original age_based on best f1score.sav'
pickle.dump(model, open(file_name, 'wb'))

# 결과 확인하기 
preds = model.predict_proba(X_test)
p = preds[:, 1]

y_prob_pred = (model.predict_proba(X_test)[:, 1] >=  0.29692155636794143).astype(bool)
print(classification_report(y_test, y_prob_pred))
print(confusion_matrix(y_test, y_prob_pred))
print(accuracy_score(y_test, y_prob_pred))
print(f1_score(y_test, y_prob_pred))
print(roc_auc_score(y_test, y_prob_pred))

