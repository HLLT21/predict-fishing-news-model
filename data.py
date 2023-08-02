import os 
import json
import pandas as pd



'''
[제목, 내용, 카테고리, 낚시성]
'''
columns = ['newsTitle', 'newsContent', 'newsCategory','clickbaitClass']
sample = []
count = 1

def get_data(path):
    '''
    [제목, 내용, 카테고리, 낚시성] 순으로 데이터를 모음 알아서 해석하셈
    '''
    global columns
    global sample
    global count 
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        newsTitle = data['sourceDataInfo']['newsTitle']
        newsContent = data['sourceDataInfo']['newsContent']
        newsCategory = data['sourceDataInfo']['newsCategory']
        clickbaitClass = data['labeledDataInfo']['clickbaitClass']
        sample.append([newsTitle, newsContent, newsCategory, clickbaitClass])
        print(count)
        count+=1
        # pd.DataFrame(columns=columns, data=sample).to_csv('/Users/mac/Desktop/github/predict-fishing-news/data/data_frame.csv')
        

def bruteforce(path):
    '''
    폴더안의 파일을 읽은 후 폴더면 다시 재귀, .json이 포함되어 있으면 데이터 획득하는 get_data함수 실행
    '''
    for file in os.listdir(path):
        temp = path+'/'+file
        if os.path.isdir(temp):
            bruteforce(temp)
        elif '.json' in file:
            get_data(temp)
# path : 라벨링데이터 폴더 위치
# 예시
# path = 'C:/Users/gjaischool1/Downloads/146.낚시성 기사 탐지 데이터/01.데이터/Training/02.라벨링데이터'
path = '라벨링데이터 폴더 위치' ## 수정위치
os.chdir(path)
for file in os.listdir():
    if os.path.isdir(file):
        bruteforce(path+'/'+file)  
# 데이터 프레임을 저장할 위치 
# 예시
# pd.DataFrame(columns=columns, data=sample, index=None).to_csv('C:/Users/gjaischool1/github/predict-fishing-news-model/data/dataset.csv')
pd.DataFrame(columns=columns, data=sample, index=None).to_csv('데이터 프레임 저장할 위치') ## 수정위치
print('end')


