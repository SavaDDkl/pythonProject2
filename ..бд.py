import random

class Activity:
    def __init__(self, name, progress = 0, feeling = 100 ):
        self.name = name
        self.progress = progress
        self.feeling = feeling

class Student:
    def __init__(self , name, progress = 0, feeling = 100):
        self.name = name
        self.progress = progress
        self.feeling = feeling
        self.alive = True

    def __str__(self):
        return f'{self.name}(успеваемость:{self.progress}, настроение:{self.feeling})'

    def do (self, activity: Activity):
        print(f'{self.name}взялся за  {activity.name}')
        self.progress += activity.progress
        self.feeling += activity.feeling

    def check_alive(self):
        self.alive = self.progress > 0 and self.feeling > 0

stud1 = Student('Mark')
stud2 = Student('Denic')
math = Activity('Математика', progress=4 , feeling=-3)
football = Activity('Футбол', progress=-1 , feeling=6)
computer = Activity('Играет в компьютер', progress=-2 , feeling=4)
homework = Activity('ДЗ', progress=3 , feeling=-3)
film = Activity('Фильм', progress=0 , feeling=5)
physic = Activity('Физика', progress=4 , feeling=-3)
training = Activity('Тренировка', progress=3 , feeling=3)
history = Activity('История', progress=4 , feeling=-3)

activities = [math,football,computer,homework,film,physic,training,history]
for day in range(30):
    print(f'-День {day+1}')
    stud1.do(random.choice(activities))
    stud2.do(random.choice(activities))
    print('---')
    print(stud1)
    print(stud2)
    if not stud1.alive or not stud2.alive:
        break
