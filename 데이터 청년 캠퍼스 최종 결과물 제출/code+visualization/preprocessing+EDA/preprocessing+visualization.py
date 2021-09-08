import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from scipy.stats import chi2_contingency

# warning 무시
warnings.filterwarnings(action='ignore')

# matplotlib 한글 깨짐 해결 - 컴퓨터에 있는 폰트로 설정해야 됨 
plt.rc('font',family='Malgun Gothic')

# 2018년 진료비확인신청 데이터 읽어오기 
df1 = pd.read_csv(r"C:\Users\HIRA\data\진료비확인심사조회시스템_20180101~20181231.csv", encoding = 'cp949',
                 usecols = ['순번','수진자생년월일','요양기호', '요양종별', '표준코드','진료과목','진료형태','상병기호','과다본인부담금','진료개시일자','분류코드(기관)',
                            '보험자구분','항코드(중분류)','구분', '분류', '항목(대분류)'])

# 2019년 진료비확인신청 데이터 읽어오기
df2 = pd.read_csv(r"C:\Users\HIRA\data\진료비확인심사조회시스템_20190101~20191231.csv", encoding = 'cp949',
                 usecols = ['순번','수진자생년월일','요양기호','요양종별', '표준코드','진료과목','진료형태','상병기호','과다본인부담금','진료개시일자','분류코드(기관)',
                            '보험자구분','항코드(중분류)','구분', '분류', '항목(대분류)'])

# 2020년 진료비확인신청 데이터 읽어오기
df3 = pd.read_csv(r"C:\Users\HIRA\data\진료비확인심사조회시스템_20200101~20201231.csv", encoding = 'cp949',
                 usecols = ['순번','수진자생년월일','요양기호','요양종별', '표준코드','진료과목','진료형태','상병기호','과다본인부담금','진료개시일자','분류코드(기관)',
                            '보험자구분','항코드(중분류)','구분', '분류', '항목(대분류)'])

# 2021년 진료비확인신청 데이터 읽어오기
df4 = pd.read_csv(r"C:\Users\HIRA\data\진료비확인심사조회시스템_20210101~20210630.csv", encoding = 'cp949',
                 usecols = ['순번','수진자생년월일','요양기호','요양종별','표준코드','진료과목','진료형태','상병기호','과다본인부담금','진료개시일자','분류코드(기관)',
                            '보험자구분','항코드(중분류)','구분', '분류', '항목(대분류)'])

# df에 하나로 합치기 
df = pd.concat([df1, df2, df3, df4])
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())

#같은 순번이면서 같은 표준코드이면서 겹치는 것을 DROP, 연번+순번이 달라야 다른 신청건 -> 연도별로 따로 해줘야함
df1.drop_duplicates(subset=['순번','표준코드'], inplace = True)
df1.drop(['순번','표준코드'], inplace = True, axis = 1)

df2.drop_duplicates(subset=['순번','표준코드'], inplace = True)
df2.drop(['순번','표준코드'], inplace = True, axis = 1)

df3.drop_duplicates(subset=['순번','표준코드'], inplace = True)
df3.drop(['순번','표준코드'], inplace = True, axis = 1)

df4.drop_duplicates(subset=['순번','표준코드'], inplace = True)
df4.drop(['순번','표준코드'], inplace = True, axis = 1)

# 연도별로 중복 삭제한 항목을 df에 하나로 합치기
df = pd.concat([df1, df2, df3, df4])
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.head)

# df_test = df[df.과다본인부담금 < 0]
# print(df_test)
# print(df_test.info())

# 과다본인부담금이 음수인 항목은 제거 
# 미수금 관련 항목으로 확인해본 결과, 0.017%로 매우 적은 비율임 
df = df[df.과다본인부담금 >= 0]
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df)

# target 변수인 환불여부 칼럼 추가 
df['환불여부'] = np.where((df.과다본인부담금 > 0), 1, 0)
df.drop('과다본인부담금', axis = 1, inplace= True)

# 수진자생년월일 정보로 환자성별 칼럼 추가 
# 남자 = 1, 여자 = 0
df['수진자생년월일'] = df['수진자생년월일'].astype('str')
sex = []
for d in df['수진자생년월일']:
    if int(d[-1]) % 2 == 0:
        sex.append(0)
    elif int(d[-1]) % 2 != 0 :
        sex.append(1)
df['환자성별'] = sex

#수진자생년월일 정보로 진료시점의 환자 만 나이 칼럼 추가 
df['진료개시일자'] = df['진료개시일자'].astype('int')
df['진료개시일자'] = df['진료개시일자'].astype('str')
age = []
temp= []

for birth in df['수진자생년월일']:
    if birth[-1] == '0' or birth[-1] == '9':
        temp.append('18' + birth[:6])
    elif birth[-1] == '2' or birth[-1] == '1' or birth[-1] == '5' or birth[-1] == '6':
        temp.append('19' + birth[:6])
    else :
        temp.append('20' + birth[:6])

df['수진자생년월일_temp'] = temp
for birth, diagnosis in zip(df['수진자생년월일_temp'], df['진료개시일자']):
    birth_d = int(birth[-2:])
    birth_m = int(birth[-4:-2])
    birth_y = int(birth[:4])

    diagnosis_d = int(diagnosis[-2:])
    diagnosis_m = int(diagnosis[-4:-2])
    diagnosis_y = int(diagnosis[:4])
    year = 0
    if diagnosis_m > birth_m :
        year = diagnosis_y - birth_y
    if diagnosis_m == birth_m :
        if diagnosis_d >= birth_d:
            year = diagnosis_y - birth_y
        else:
            year = diagnosis_y - birth_y - 1
    if diagnosis_m < birth_m :
        year = diagnosis_y - birth_y - 1

    age.append(year)

df['환자 만 나이'] = age

# 환자 만 나이 오류 제거 
# 담당자 입력오류 ex.주민번호 뒷부분 첫번째 자리와 출생연도가 현재연도보다 큼
df = df[df['환자 만 나이'] >= 0]
df = df[df['환자 만 나이'] <=100]

# 진료일자 기준 연도별 상반기 하반기 구분하는 칼럼 추가 
half = []
for i in df['진료개시일자']:
    if int(i[4:6]) <= 6 :
        half.append(i[:4] + '1')
    else :
        half.append(i[:4] + '2')
df['연도 + 반기'] = half

# 불필요한 칼럼 제거 
df.drop('수진자생년월일_temp', axis =1, inplace = True)
df.drop('수진자생년월일', axis =1, inplace = True)
df.drop('진료개시일자', axis = 1, inplace = True)

# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())

#'외래' 데이터만 추출하기
#print(df.진료형태.unique())
df = df[df['진료형태'] == '외래']
df.drop('진료형태', axis = 1, inplace = True)

# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df)

#=============================요양종별 null 채우기=============================================
# df_null에 요양종별이 null인 항목을 넣고, df에는 null인 항목 제거해서 구분하기 
df_null = df[df.요양종별.isna()]
df.dropna(subset=['요양종별'], inplace=True)

# 심평원에서 추가로 요청한 요양종별코드와 요양기호가 매칭되어 있는 파일임 
# 칼럼 3개 : 요양종별코드, 생성년월, 요양기호 
df_table = pd.read_csv(r'C:\Users\HIRA\data\clcd_test.txt', delimiter=',')
df_table.rename(columns={'RECU_CL_CD':'id'}, inplace=True)

# 생성년월 칼럼 제거 (불필요함)
df_table.drop('CRTR_YM', axis=1, inplace=True)
#df_table = df_table[(df_table.id == 1.) | (df_table.id == 11.) | (df_table.id == 21.) | (df_table.id == 31.)]

# 중복 제거 : 등록일자만 다른 행이 많음
df_table.drop_duplicates(subset=['ykiho'], inplace=True) 

# 요양종별이 null인 df의 요양기호의 unique list 추출하여 매칭파일에서 요양종별코드를 찾아 채워넣기 
li = list(df_null['요양기호'].unique())

for i in li:
    df_tmp = df_null[df_null.요양기호==i]
    for row in df_table.itertuples():
        if row.ykiho == i:
            df_tmp.fillna(row.id, inplace=True)
    df = pd.concat([df,df_tmp])

# 요양종별코드 대신 요양종별명칭으로 바꾸기 
df['요양종별'].replace({1.:'상급종합병원',
                    11.:'종합병원',
                    21.:'병원',
                    31.:'의원',
                    28.:'요양병원',
                    29.:'정신병원',
                    41.:'치과병원',
                    51.:'치과의원',
                    61.:'조산원',
                    71.:'보건소',
                    72.:'보건지소',
                    73.:'보건진료소',
                    74.:'모자보건센타',
                    75.:'보건의료원',
                    81.:'약국',
                    91.:'한방종합병원',
                    92.:'한방병원',
                    93.:'한의원',
                    94.:'한약방'}, inplace=True)

# 잘 채워졌나 확인 
# print(df.요양종별.unique())
#
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df)
# df.to_csv('fillNull.csv', encoding='cp949')

#상병기호 없으면 상병명도 없음 : 상병기호 null 채울 수 있는 방법이 없음(64개 버림)
df.dropna(subset = ['상병기호'], inplace = True)

# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())
#
# print(df.분류.unique())
# print(df.분류.value_counts())

# df.to_csv('neddToCheck.csv', encoding='cp949')
# df_new = df[(df.분류.isna()) | (df.분류==21.0) | (df.분류==31.0)]
# df_new.to_csv('분류_null.csv', encoding='cp949')

# 분류 칼럼의 정상값은 ABCDEF
# null값과 잘못 입력된 값을 확인 
df_missing_분류 = df[(df.분류.isna()) | (df.분류==21.0) | (df.분류==31.0)]

df.dropna(subset=['분류'], inplace=True)

# 정상인 항목만 추출 
df = df[(df.분류=='A') | (df.분류=='B') | (df.분류=='C') | (df.분류=='D') | (df.분류=='E') | (df.분류=='F')]
# df.to_csv('gyu_test_1.csv', encoding='cp949')
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())

# 요양기호, 환자성별, 환불여부 str로 변환
df['요양기호'] = df['요양기호'].astype('str')
df['환자성별'] = df['환자성별'].astype('str')
df['환불여부'] = df['환불여부'].astype('str')


# 상위 진료과목 9개에 대한 df를 확인하기 위함 
df_use = df[(df.진료과목 == '산부인과')|(df.진료과목 == '내과')|(df.진료과목=='정형외과')|(df.진료과목=='응급의학과')|(df.진료과목=='외과')|
             (df.진료과목=='신경외과')|(df.진료과목=='성형외과')|(df.진료과목=='소아청소년과')|(df.진료과목=='안과')]

# print('===============================================================================')
# print(df_use.isnull().sum())
# print(df_use.info())
# print(df_use.nunique())

#===================================================시각화 (EDA 폴더에 결과물 참조)=========================================================
# 타겟 변수 빈도수 파악
# df['환불여부'].value_counts().sort_index(ascending= True).plot(kind='bar')
# plt.xlabel('환불여부 (0:환불안됨, 1:환불됨)')
# plt.ylabel('count')
# plt.title('환불여부 count')
# plt.show()

df_refund = df[df.환불여부 == '1']
# 요양종별 빈도수 파악 : 전체항목
# df['요양종별'].value_counts().plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('요양종별')
# plt.title('전체항목 요양종별 count')
# plt.show()
#
# # 요양종별 빈도수 파악 : 환불항목
# df_refund['요양종별'].value_counts().plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('요양종별')
# plt.title('환불항목 요양종별 count')
# plt.show()
#
# # 진료과목 빈도수 파악 : 전체항목
# df['진료과목'].sort_index(ascending= True).value_counts().plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('진료과목')
# plt.title('전체항목 진료과목 count')
# plt.show()
#
# # 진료과목 빈도수 파악 : 환불항목
# df_refund['진료과목'].sort_index(ascending= True).value_counts().plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('진료과목')
# plt.title('환불항목 진료과목 count')
# plt.show()
#
# # 진료과목 빈도수 파악 : 전체항목
# df['진료과목'].value_counts().plot.pie(autopct='%.2f%%')
# plt.axis('equal')
# plt.show()
#
# # 진료과목 빈도수 파악 : 환불항목
# df_refund['진료과목'].value_counts().plot.pie(autopct='%.2f%%')
# plt.axis('equal')
# plt.show()

# # 환자성별 빈도수 파악 : 전체항목
# df['환자성별'].value_counts().plot.pie(autopct='%.2f%%')
# plt.axis('equal')
# plt.title('전체항목 환자 성비')
# plt.show()
#
# # 환자성별 빈도수 파악 : 환불항목
# df_refund['환자성별'].value_counts().plot.pie(autopct='%.2f%%')
# plt.axis('equal')
# plt.title('환불항목 환자 성비')
# plt.show()
#
# # 상병기호 빈도수 파악 : 전체항목
# df['상병기호'].value_counts().nlargest(20).plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('Top 20 상병기호')
# plt.title('Top 20 상병기호 빈도수 - 전체항목')
# plt.show()
#
# # 상병기호 빈도수 파악 : 환불항목
# df_refund['상병기호'].value_counts().nlargest(20).plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('Top 20 상병기호')
# plt.title('Top 20 상병기호 빈도수 - 환불항목')
# plt.show()
#
# # 분류코드 빈도수 파악 : 전체항목
# df['분류코드(기관)'].value_counts().nlargest(20).plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('Top 20 분류코드')
# plt.title('Top 20 분류코드 빈도수 - 전체항목')
# plt.show()
#
# # 분류코드 빈도수 파악 : 환불항목
# df_refund['분류코드(기관)'].value_counts().nlargest(20).plot(kind='barh')
# plt.xlabel('count')
# plt.ylabel('Top 20 분류코드')
# plt.title('Top 20 분류코드 빈도수 - 환불항목')
# plt.show()

# #환자 만 나이 : 전체항목
# print(df['환자 만 나이'].describe())
# kde = sns.kdeplot(df['환자 만 나이'])
# kde.set_xlabel('환자 만 나이')
# kde.set_ylabel('비율')
# plt.show()
#
# # skewness and kurtosis
# print('skewness : %f' %
#       df['환자 만 나이'].skew())
# print('kurtosis : %f' %
#       df['환자 만 나이'].kurt())
#
# #환자 만 나이 : 환불항목
# print(df_refund['환자 만 나이'].describe())
# kde = sns.kdeplot(df['환자 만 나이'])
# kde.set_xlabel('환자 만 나이')
# kde.set_ylabel('비율')
# plt.show()
#
# # skewness and kurtosis : 환불항목
# print('skewness : %f' %
#       df_refund['환자 만 나이'].skew())
# print('kurtosis : %f' %
#       df_refund['환자 만 나이'].kurt())

# ============================================두 변수 간의 관계===============================================

# 요양종별 - 진료과목
df_진료과목 = df[(df.진료과목 == '산부인과')|(df.진료과목 == ' 내과')|(df.진료과목=='정형외과')|(df.진료과목=='응급의학과')|(df.진료과목=='외과')|
             (df.진료과목=='신경외과')|(df.진료과목=='성형외과')|(df.진료과목=='소아청소년과')|(df.진료과목=='안과')]
df_요양종별 = df_진료과목[(df_진료과목.요양종별=='상급종합병원') | (df_진료과목.요양종별=='종합병원') | (df_진료과목.요양종별=='병원')|(df_진료과목.요양종별=='의원')]
# df_요양종별 : 진료과목 9개 & 요양종별 4개
# cnt = sns.countplot(x='진료과목',hue='요양종별', data=df_요양종별, palette='Set3')
# cnt.set_ylabel('count')
# cnt.set_xlabel('진료과목')
# plt.show()
#
# # 진료과목 - 성별
# cnt = sns.countplot(x='진료과목',hue='환자성별', data=df_진료과목, palette='Set3')
# cnt.set_ylabel('count')
# cnt.set_xlabel('진료과목')
# plt.show()
#
# # 진료과목 - 환불여부
# cnt = sns.countplot(x='진료과목',hue='환불여부', data=df_진료과목, palette='Set3')
# cnt.set_ylabel('count')
# cnt.set_xlabel('진료과목')
# plt.show()
#
# # 진료과목 - 나이
# box = sns.boxplot(y='진료과목', x='환자 만 나이', data=df_진료과목)
# box.set_xlabel('환자 나이')
# box.set_ylabel('진료과목')
# plt.show()
#
# # 성별 - 나이
# sns.catplot(x='환자성별', y='환자 만 나이', kind='boxen', data=df)
# plt.show()
#
# # 나이 - 환불여부
# sns.catplot(x='환불여부', y='환자 만 나이', kind='boxen', data=df)
# plt.show()

df_refund_진료과목 = df_진료과목[df_진료과목.환불여부=='1']
df_refund_요양종별 = df_요양종별[df_요양종별.환불여부=='1']
# # 진료과목 - 요양종별
# cnt = sns.countplot(x='진료과목',hue='요양종별', data=df_refund_요양종별, palette='Set3')
# cnt.set_ylabel('count')
# cnt.set_xlabel('진료과목')
# plt.show()
#
# # 진료과목 - 성별
# cnt = sns.countplot(x='진료과목',hue='환자성별', data=df_refund_진료과목, palette='Set3')
# cnt.set_ylabel('count')
# cnt.set_xlabel('진료과목')
# plt.show()
#
# # 진료과목 - 나이
# box = sns.boxplot(y='진료과목', x='환자 만 나이', data=df_refund_진료과목)
# box.set_xlabel('환자 나이')
# box.set_ylabel('진료과목')
# plt.show()
#
# # 성별 - 나이
# sns.catplot(x='환자성별', y='환자 만 나이', kind='boxen', data=df_refund)
# plt.show()

#==============================================상관관계 분석================================================
# 다범주형 범수이기 때문에 crammersV method로 계산함 

#print(df.info())

# le = preprocessing.LabelEncoder()
# df_encoded = df
#
# for i in df_encoded.columns[df_encoded.dtypes == 'object']:
#     df_encoded[i] = le.fit_transform(list(df_encoded[i]))
#
# def crammersV(var1, var2):
#     crosstab = np.array(pd.crosstab(var1, var2, rownames=None, colnames=None))
#     stat = chi2_contingency(crosstab)[0]
#     obs = np.sum(crosstab)
#     mini = min(crosstab.shape) - 1
#     return (stat/(obs*mini))
#
# rows = []
# for var1 in df_encoded:
#     col = []
#     for var2 in df_encoded:
#         crammers = crammersV(df_encoded[var1], df_encoded[var2])
#         col.append(round(crammers,2))
#     rows.append(col)
#
# crammers_res = np.array(rows)
# df_new = pd.DataFrame(crammers_res, columns=df_encoded.columns, index=df_encoded.columns)
# mask = np.zeros_like(df_new, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True

# with sns.axes_style('white'):
#     plt.rc('font', family='Malgun Gothic')
#     ax = sns.heatmap(df_new, mask=mask, vmin=0., vmax=1., square=True, annot=True, cmap='YlGnBu')
# plt.show()

# =========================================상관관계 분석 결과==================================================
# 1 : 요양종별과 요양기호 -> 요양종별 drop
# 1 : 항코드(중분류)와 항목(대분류) -> 항목(대분류) drop
# 0.84 : 분류코드와 분류 -> 분류 drop

df.drop('요양종별', axis=1, inplace=True)
df.drop('항목(대분류)', axis=1, inplace=True)

 # 분류는 드롭한 row가 있으니까 드롭하기 전 상태로 돌려놓기 
# print(df.info())
# print(df_missing_분류.info())
df_missing_분류.drop(['요양종별','항목(대분류)'], axis=1, inplace=True)
df = pd.concat([df, df_missing_분류])
# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())

df.drop('분류', axis=1, inplace=True)

# 상위 9개 진료과목에 대해서만 진행하기로 결정 (EDA 폴더 자료 참고)
df = df[(df.진료과목 == '산부인과')|(df.진료과목 == '내과')|(df.진료과목=='정형외과')|(df.진료과목=='응급의학과')|(df.진료과목=='외과')|
             (df.진료과목=='신경외과')|(df.진료과목=='성형외과')|(df.진료과목=='소아청소년과')|(df.진료과목=='안과')]

# print('===============================================================================')
# print(df.isnull().sum())
# print(df.info())
# print(df.nunique())
# print(df.보험자구분.value_counts())
# print(df.요양기호.value_counts().nlargest(20))
# print(df.진료과목.value_counts())
# print(df.상병기호.value_counts().nlargest(20))
# print(df['항코드(중분류)'].value_counts())
# print(df['분류코드(기관)'].value_counts().nlargest(20))
# print(df.구분.value_counts())
# print(df.환불여부.value_counts())
# print(df.환자성별.value_counts())
# print(df['환자 만 나이'].value_counts())
# print(df['연도 + 반기'].value_counts())

#=======================================================머신러닝 준비=====================================================

# df.to_csv('0826_final.csv', encoding='cp949')
df.to_csv('realLastDF.csv', encoding='cp949')


