import pandas as pd

scores = pd.DataFrame(
    [
       [96,76,60,85,80], #자바   
       [88,92,100,55,70], #파이썬
       [10,20,30,40,50] #js
    ]
)              
print(scores)    

scores = pd.DataFrame(
    [
       [96,76,60,85,80], #자바   
       [88,92,100,55,70], #파이썬
       [10,20,30,40,50] #js
    ],
    index=["java", "python", "js"]
)
print(scores)    

student_number = [1,2,3,4,5]
scores = pd.DataFrame(
    [
       [96,88,10], #자바   
       [76,92,20], #파이썬
       [60,100,30], #js
       [85,55,40],
       [80,70,50]
    ],
    index=student_number
)    
print(scores)




scores = pd.DataFrame(
    {
      "java":[96,76,60,85,80], #자바   
      "python":[88,92,100,55,70], #파이썬
       "js":[10,20,30,40,50] #js
    },
    index=student_number
    )
print(scores)    

#딕셔너리 데이터를 DataFrame으로 변환
scores_dict = {
       "java":[96,76,60,85,80], #자바   
      "python":[88,92,100,55,70], #파이썬
       "js":[10,20,30,40,50] #js
    }
scores= pd.DataFrame(scores_dict)
print(scores)

#이름 데이터 추가
scores["이름"] = ["임현종","김범수","김민경","이현우","조준상"]
print(scores)

#데이터 추가
scores.loc[6] = [80,80,80,"최서하"]
print(scores)

student_number = [1,2,3,4,5,6]
#학번,이름,성적을 모두 포함한 DataFrame 선언

scores = pd.DataFrame(
      {
        "이름": ["임현종","김범수","최서하","김민경","이현우","조준상"],
        "java":[96,76,60,85,80,20], #자바   
        "python":[88,92,100,55,70,45], #파이썬
        "js":[10,20,30,40,50,20] #js
    },
    index=student_number
    ).transpose()

print(scores)

#index 기준 정렬
print(scores.sort_index())
#index 기준 내림차순 정렬
print(scores.sort_index(ascending=False))

#이름 열 기준 오름차순 정렬
print(scores.sort_values(by="이름", ascending=True))

#첫2줄만조회
print(scores.head(2))
print(scores.tail(2))#마지막2줄

