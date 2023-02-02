# array = {
#     'user1':[
#         "Sergey",
#         "Alexeevich",
#         "Skvorkin",

#     ],
#     'user2':[
#         "Masha",
#         "Sergeyevna",
#         "Kim"
#     ],
#     'user3':[
#         "Ilya",
#         "Maksimovich",
#         "Bayo"
#     ],
#     'user4':[
#         "Andrey",
#         "Alexandrovich",
#         "Sokolov"
#     ],
#     'user5':[
#         "Eveline",
#         "Olegovna",
#         "Bugova"
#     ],
#     'user6':[
#         "Ruslan",
#         "Sergeevich",
#         "Strem"
#     ]
# }
# value = input("Фамилия для поиска: ")
# print(array["user1"][2])
# for i in range(1,len(array)):
#     if array['user'+str(i)][2] == value :
#         print(array['user'+str(i)])
# print(array["user1"])





# Lab 2 FP
count = 0
name = input("Ф.И.О учащегося: ")

# Правильны ответ - 2
ans1 = int(input("Сколько типов комментария есть в Python ?"))

# Правильны ответ - pip install
ans2 = input("Как можно установить библиотеку в компилятор ? (Команда)")

# Правильны ответ - for i in range(100,1,-1) или for i in range(1,-100,-1)
ans3 = input("Как задать цикл For ,значения которого будут уменьшаться на 1 ? (Команда)")

# Правильны ответ - нет ограничения
ans4 = input("Сколько блоков 'Elif' можно задать в цикле IF ?")
print("Здравствуйте , "+name +" !")
if ans1 == 2:
    count+1
    print("Ответ на 1й вопрос правильный")
else :
    print("Ответ на 1й вопрос не правильный")

if ans2 == "pip install" :
    count+1
    print("Ответ на 2й вопрос правильный")
else:
    print("Ответ на 2й вопрос правильный")

if ans3 == "for i in range(100,1,-1)":
    count+1
    print("Ответ на 3й вопрос правильный")
else:
    print("Ответ на 3й вопрос правильный")

if ans4 == "нет ограничения":
    count+1
    print("Ответ на 4й вопрос правильный")
else:
    print("Ответ на 4й вопрос правильный")

