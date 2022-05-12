#chapter2
total_dictionary = {}
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break  #q입력하면 멈춤
    else:
        total_dictionary[question] = "" #key에 question 들어가고 value에는 빈칸 

#chapter3

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)

#chapter4

total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})  #리스트에 딕셔너리 추가

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)

#chapter5

total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)

