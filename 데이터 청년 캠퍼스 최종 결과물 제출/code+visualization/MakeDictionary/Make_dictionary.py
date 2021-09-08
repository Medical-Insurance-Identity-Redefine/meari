#!/usr/bin/env python
# coding: utf-8

# # Make_dictionary
# - 의료 급여 비급여 명칭데이터를 통해 사전을 구축

# 형태소분석기 관련 설치
get_ipython().system('pip install JPype1')
get_ipython().system('pip install rhinoMorph')

import pandas as pd
import numpy as np
import re
import rhinoMorph

def Make_Dictionary(path): # 사전 만들기(csv 파일)
    df = pd.read_csv(path, encoding = 'cp949')   # 파일 불러오기
    df_list = df.명칭.to_list()  # 명칭만 해당하는 데이터를 리스트로 변환
    dic = []
    for i in range(len(df_list)):  # 특수기호 제거
        text = re.sub('[-_=+,/\?:^.*·''""(\)[\]<\>「\」|`~!%βⅡ°\ © ® ° α β γ δ ε ζ η θ ι κ λ μ π ο φ χ ψ ω Ф Э ф • ⁿ ‥ … € Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ Ⅵ ⅦⅧ ™ Ω ⅓ ⅔ ℃ ℓ → ← ∙ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ■ □ ▲ △ ▶ ◆◇ ◈ ◎ ○ ● ◐ ◑ ★ ☆ ♠ ♡ ♣ ♤ ♥ 〮 ㎀ ㎁ ㎂ ㎃ ㎄ ㎈ ㎉ ㎊ ㎋ ㎌ ㎍㎎ ㎕ ㎖ ㎗ ㎘ ㎚ ㎛ ㎜ ㎝ ㎞ ㎟ ㎠ ㎡ ㎢ ㎣ ㎤ ㎥ ㎦ ㎧ ㎼ ㎽ ㎾ ￠ ￡ ～ ︒ ︓ ⅓™αμΦ×,Ⅲ∥Ⅰ~ⅣΙ®ⅤⅥⅦ㎛*Øⓜ＊ㆍ?◈°ⅠⅡⅢⅣΙΙβ]', '', df_list[i])
        dic.append(text)
    rn = rhinoMorph.startRhino()   # 형태소분석기 객체 생성
    morphed_data = ''
    for data_each in dic:      # 전체 데이터 Tokenizer
        morphed_data_each = rhinoMorph.onlyMorph_list(
            rn, data_each[:-1], pos =['NNG', 'NNP' ,'SL'], eomi = True)
        joined_data_each = ' '. join(morphed_data_each)  # 문자열 하나로 연결
        if joined_data_each:                              # 내용이 있는 경우만 저장
            morphed_data += joined_data_each + '\t'
    data = morphed_data.replace('\t',' ')   # tab 제거
    data = data.split(' ')    # 공백을 기준으로 나눠 리스트로 저장
    set_list = set(data)
    final_list = list(set_list)   # 최종적으로 중복값 제거
    return final_list

path = "Dict_list.csv"   # 급여 사전 구축
dict = Make_Dictionary(path)
print(dict)

path_non = "Dict_list_non.csv"  # 비급여 사전 구축
dict_non = Make_Dictionary(path_non)
print(dict_non)

with open('insurance.txt', 'w', encoding = 'UTF-8') as f:  # 급여사전을 txt로 저장
    for name in dict:
        f.write(name+'\t')

with open('insurance_non.txt', 'w', encoding = 'UTF-8') as f: # 비급여사전을 txt로 저장
    for name in dict_non:
        f.write(name+'\t')
