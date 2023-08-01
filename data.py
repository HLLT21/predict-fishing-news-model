import os 
import json
import pandas as pd



columns = ['newsTitle', 'newsContent', 'clickbaitClass']
sample = []
count = 1
def get_data(path):
    global columns
    global sample
    global count 
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        newsTitle = data['sourceDataInfo']['newsTitle']
        newsContent = data['sourceDataInfo']['newsContent']
        clickbaitClass = data['labeledDataInfo']['clickbaitClass']
        sample.append([newsTitle, newsContent, clickbaitClass])
        print(count)
        count+=1
        # pd.DataFrame(columns=columns, data=sample).to_csv('/Users/mac/Desktop/github/predict-fishing-news/data/data_frame.csv')
        
def bruteforce(path):
    for file in os.listdir(path):
        temp = path+'/'+file
        if os.path.isdir(temp):
            bruteforce(temp)
        else:
            get_data(temp)
# path = '/Users/mac/Downloads/146.낚시성 기사 탐지 데이터/01.데이터/Training/02.라벨링데이터'
# os.chdir(path)
# for file in os.listdir():
#     if os.path.isdir(file):
#         bruteforce(path+'/'+file)  
    
# pd.DataFrame(columns=columns, data=sample, index=None).to_csv('/Users/mac/Desktop/github/predict-fishing-news/data/data_frame.csv')
    
# print('end')


df = pd.read_csv('data/data_frame.csv')
print(df.shape)