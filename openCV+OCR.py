#!/usr/bin/env python
# coding: utf-8

# In[192]:


# 어플에서 input되는 값
birthday = '981006'
diseaseCode = 'S52'

# # create-model

# In[3]:


NANONETS_API_KEY = 'VeKySt5RmXLGQ9_2B59rZkFla-G73pVX'
NANONETS_MODEL_ID = '3beb7ed2-489f-4b32-bf82-347c109b15b1'

model_id = NANONETS_MODEL_ID
api_key = NANONETS_API_KEY

# In[4]:


import requests, os, json

url = "https://app.nanonets.com/api/v2/ObjectDetection/Model/"

##
payload = "{\"categories\" : [\"number_plate\"], \"model_type\": \"ocr\"}"
headers = {'Content-Type': "application/json", }

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''), data=payload)
model_id = '3beb7ed2-489f-4b32-bf82-347c109b15b1'

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)

# # upload-training

# In[5]:


import os, requests, json
from tqdm import tqdm

pathToAnnotations = './annotations/json'
pathToImages = './images'

for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in tqdm(files):
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        if imageName == "":
            continue
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        jsonData = annotation.read()
        url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/UploadFile/'
        data = {'file': open(imagePath, 'rb'),
                'data': ('', '[{"filename":"' + imageName + ".jpg" + '", "object": ' + jsonData + '}]'),
                'modelId': ('', model_id)}
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        if response.status_code > 250 or response.status_code < 200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")

# #  train-model

# In[6]:


import requests, os

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")

# # model-state

# In[7]:


import requests, os, json

model_id = NANONETS_MODEL_ID
api_key = NANONETS_API_KEY

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(api_key, ''))

state = json.loads(response.text)["state"]
status = json.loads(response.text)["status"]

if state != 5:
    print("The model isn't ready yet, its status is:", status)
    print(
        "We will send you an email when the model is ready. If you are impatient, run this script again in 10 minutes to check.")
else:
    print("NEXT RUN: python ./code/prediction.py ./images/151.jpg")

# In[40]:


image_path = '/Users/jueunkim/Desktop/메아리/thinDoc.jpg'

# In[130]:


import requests, os, sys
import json
import unicodedata
import time

# import file

model_id = NANONETS_MODEL_ID
api_key = NANONETS_API_KEY

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(image_path, 'rb'), 'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

# print(response.text)
# print(type(response.text))
responseText = response.text.encode('utf-8').decode("utf-8")
print(type(responseText))
with open("data/encodedResponseText.json", "w") as resp:
    resp.write(responseText)

data = json.load(open('data/encodedResponseText.json'))

# In[131]:


import pandas as pd

# In[143]:


diagnosisList = []
patientList = []
print(data)
for i in data['result'][0]['prediction'][0]['cells']:
    diagnosisList.append(i['text'])

for i in data['result'][0]['prediction'][1]['cells']:
    patientList.append(i['text'])

with open('data/diagnosis.txt', 'w') as diagnosis:
    for item in diagnosisList:
        diagnosis.write("%s\n" % item)

with open("data/patient.txt", "w") as patient:
    for item in patientList:
        patient.write("%s\n" % item)

# In[144]:


diagnosisDF = pd.DataFrame()
patientDF = pd.DataFrame()

# In[145]:


# patientList DataFrame으로 만들기.

for t in range((len(patientList)) // 7):  # patient의 column의 수는 6개
    patientAppendList = []
    for i, item in enumerate(patientList):
        if t * 7 <= i < (t + 1) * 7:
            patientAppendList.append(item)
    appendSeries = pd.Series(patientAppendList)
    patientDF = patientDF.append(appendSeries, ignore_index=True)

patientDF.columns = ["환자 등록 번호", "환자 성명", "진료 기간", "병실", "진료과", "환자 구분", "구분"]
patientDF = patientDF.iloc[1]
patientDF

# In[146]:


# diagnosis의 column의 수는 11개

for t in range((len(diagnosisList)) // 11):
    diagnosisAppendList = []
    for i, item in enumerate(diagnosisList):
        if t * 11 <= i < (t + 1) * 11:
            diagnosisAppendList.append(item)
    print(diagnosisAppendList)
    appendSeries = pd.Series(diagnosisAppendList)
    diagnosisDF = diagnosisDF.append(appendSeries, ignore_index=True)

# In[147]:


diagnosisDF

# In[148]:


patientDF

# In[150]:


diagnosisDF.columns = ['일자', '코드', '명칭', '금액', '횟수', '일수', '총액', '공단부담', '본인부담', '전액본인부담', '비급여']
diagnosisDF = diagnosisDF.iloc[3:]
diagnosisDF.drop(['금액', '횟수', '일수', '총액', '공단부담', '본인부담', '전액본인부담'], axis=1, inplace=True)

# In[151]:


non_benefit_DF = diagnosisDF[diagnosisDF['비급여'] != '']  # 비급여내역만을 추출

# In[153]:


non_benefit_DF.drop('비급여', axis=1, inplace=True)

# In[168]:


non_benefit_DF.reset_index(inplace=True)

# In[156]:


non_benefit_DF['진료과'] = patientDF['진료과']

# In[162]:


if int(birthday[:-1]) % 2 == 0:
    sex = 0
else:
    sex = 1

non_benefit_DF['성별'] = 1

# In[172]:


if birthday[-1] == '2' or '1':
    fullBirthday = '19' + birthday
elif birthday[-1] == '3' or '4':
    fullBirthday = '20' + birthday
elif birthday[-1] == '5' or '6':
    fullBirthday = '19' + birthday
elif birthday[-1] == '7' or '8':
    fullBirthday = '20' + birthday
elif birthday[-1] == '9' or '':
    fullBirthday = '18' + birthday

non_benefit_DF['환자생년월일'] = fullBirthday

# In[180]:


fullBirthday

birthY = fullBirthday[:4]
birthM = fullBirthday[4:6]
birthD = fullBirthday[7:]

# In[183]:


print(birthY)
print(birthM)
print(birthD)

# In[174]:


diaY, diaM, diaD = non_benefit_DF['일자'][0].split('-')

# In[184]:


diaY, diaM, diaD = int(diaY), int(diaM), int(diaD)
birthY, birthM, birthD = int(birthY), int(birthM), int(birthD)

if diaM > birthM:
    year = diaY - birthY
elif diaM < birthM:
    year = diaY - birthY - 1
else:
    if diaD >= birthD:
        year = diaY - birthY
    else:
        year = diaY - birthY - 1

non_benefit_DF['환자 만 나이'] = year
non_benefit_DF.drop('환자생년월일', axis=1, inplace=True)
non_benefit_DF.drop('일자', axis=1, inplace=True)

# In[186]:


non_benefit_DF.drop('index', axis=1, inplace=True)

# In[191]:


non_benefit_DF

# In[193]:


non_benefit_DF['상병코드'] = diseaseCode[0]

# In[194]:


non_benefit_DF

# In[ ]:




