# import time 
# x=0
# y=0
# print("WELCOME TO KBC\nfirst queston on your screen")
# time.sleep(3)
# print("FIRST QUESTION APKI SCREEN PAR YE ")
# time.sleep(2)
# print("YERAHA!!")
# question1=["what is the colour of sky ?","option 1 : blue","option 2 : red","option 3 : white"," option 4 : pink"]
# print(question1[0])
# print(question1[1])
# print(question1[2])
# print(question1[3])
# print(question1[4])
# user=int(input())
# print("COMPUTER G OPTION ",user,"LOCK KIYA JAYE!!")
# match user:
#     case 1:
#         print("option A lock!!")
#     case 2:
#         print("option 2 lock!!")
#     case 3:
#         print("option 3 lock !!!")
#     case 4:
#         print("option 4 lock !!")
# time.sleep(2.5)        
# choice=user
# if (1<=choice and 1>=choice):
#   print(choice)
#   print(" CONGRATULATION!!!\ncorrect answer you won 2 rs")
#   x=2
# else:
#     print("wrong answer")
# print("next question apki scren par")  
# time.sleep(2.5) 
# print("YE RAHA!!") 
# time.sleep(2)
# question2=["what is the colour of grass ?","option 1 : blue","option 2 : red","option 3 : green","option 4 : pink"]
# print(question2[0])
# print(question2[1])
# print(question2[2])
# print(question2[3])
# print(question2[4])
# user=int(input())
# print("COMPUTER G OPTION ",user,"LOCK KIYA JAYE!!")
# match user:
#     case 1:
#         print("option A lock!!")
#     case 2:
#         print("option B lock!!")
#     case 3:
#         print("option C lock !!!")  
#     case 4:
#         print("option D lock !!")
# time.sleep(2.5) 
# choice=user
# if (3>=choice and 3<=choice):
#   print(choice)
#   print(" CONGRATULATION!!!\ncorrect answer you won 2 rs")
#   y=2
# else:
#     print("wrong answer")
# print("THANK YOU FOR PLAYING\nyou are won rs:", x + y )
import random 
mylist = ["apple", "banana", "mango"] 
print(random.choices(mylist, weights = [10, 1, 1], k = 6)) 
class Person:
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ
  def info(self):
    print(f"{self.name} is a {self.occ}")
a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()





