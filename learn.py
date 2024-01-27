# a = True
# b = None
#c=5.6
# print(type(a))
# print(type(b)) 
# print(type(c)) 
#dict1={"name":"kirti","age":19,"canvote":True}
#print(dict1) 
# print(5+6) 
# print(15-6) 
# print(15/6) 
# print(15//6) 
# print(15%6) 
# print(15*6) 
# a=5
# b=5
# ans1=a+b
# print("the addition of a and b is\n ") 
# print(ans1) 
# ans2=a-b
# print("the substraction of a and b is\n") 
# print(ans2) 
# ans3=a/b
# print("the division of a and b is\n ") 
# print(ans3) 
# ans4=a*b
# print("the addition of a and b is\n ") 
# print(ans4) 
# ans5=a//b
# print("the floorvalue  of a and b is\n ") 
# print(ans5) 
# ans6=a%b
# print("the modulo of a and b is\n ") 
# print(ans6) 
# a="1"
# b="2"
# a=1
# b=2
# print(int(a+b))
# string="15"
# number=7
# string_number=int (string)
# sum = number + string_number  
# print("sum of both number is :",sum)
#implicit type casting 
# a=2.5
# b=4
# print(a+b)
#a=input("who is your love?")
#print(a," is my love")
# info='''Python is one of the most demanded programming languages in the job market.
#  Surprisingly, it is equally easy to learn and master  Python.
#    This python tutorial for absolute beginners 
#    in Hindi series will focus on teaching you python concepts from the ground up. '''
# for character in info:
#  print(character)
#all the built in function of python are here 
# a="kirti, avinash ,mistri"
# print(a)
# print(a.upper())
# b="Kirti"
# c=" "
# print(a.lower())
# print(a.rstrip("i"))
# print(b.replace("I","1"))
# print(a.split())
# print(b.capitalize())
# print(b.center(200))
# print(a.count("i"))
# print(b.endswith("I",0,5))
# print(a.find("a"))
# print(b.isalpha())
# print(a.islower())
# print(c.isprintable())
# print(c.isspace())
# print(b.istitle())
# print(a.startswith("k"))
# print(b.swapcase())
# print(a.title())
# print(len(c))
# # print(a[-4:-2])
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# a="string"
# print(len(a))
# print(a[2:6])
#here are if else statements 
# z=int(input (" hows your marks? "))
# if(32<=z):
#     print("you are passed!! :)")
# else:
#     print("you are faild :(") 
#here some elif code
# mony= int(input("how much mony you have"))
# candy=5
# if(mony-candy==0):
#     print("i can not buy ")
# elif(mony-candy>0):
#     print("i can buy")
# else:
#      print("i can borrow mony from friends")
# print(" i was thiking about to buy some candy's")
# match case 
#this is a small calculator code 
# x= int(input("enter x :"))
# y=  int(input("enter y :"))
# print( "enter any two number for mathamatical operation\nuse 0 for +\n use 1 for -\nuse 2 for *\nuse 3")
# z= int(input("enter your operation"))
# match z:
#     case 0:
#         print("addition is ",x+y)
#     case 1:
#          print(" substraction is ",x-y)
#     case 2:
#         print("multiplication is ",x*y)
#     case 3:
#         print("division is ",x/y)
#for loop statements
# a="kirtu"
# for i in a:
#     print(i)
#     if (i=="u"):
#         print("my friend used to call me this")
#for list 
# fevouratedish=["pavbhaji","panipuri","panir masala","kadhi","dhivada","icecreem"]
# for dish in fevouratedish:
#     print(dish)
#     for item in dish:
#      print(item) 
# for k in range (100):
#  print(k+1,end =" ") 
# for i in range(5):
# 	print(i, end=" ")
# i=0
# while(i<=10):
#     print(i)
#     i=i+1
# print("while loop is over")
#this code is for break and continue statement 
# for i in range(10):
#     if(i==10):
#         break
#     print("2 X",i+1,"=",(i+1)*2)
# print("this is the 2 table")
# for i in range(10):
#     if(i==6):
#         print("continue ki vajha se 2 X 7 =14 gayap ho gaya")
#         continue
#     print("2 X",i+1,"=",(i+1)*2)
# print("this is the 2 table")
# i=0
# while True:
#     print(i)
#     i = i+1
#     if(i%10==0):
#         break
# function 
# a=int(input("enter first value "))
# b=int(input("enter second value "))
# c=int(input("enter third value "))
# def average(a,b,c):
#     avg=(a+b+c)/2
#     print(avg)h
# average(a,b,c)
# x=int(input("enter first value "))
# y=int(input("enter second value "))
# z=int(input("enter third value "))
# average(x,y,z)
#functions arrguments 
#1defult arrguments 
# def average (a=1,b=2):
#     print("the average is :",(a+b)/2)
# average()
#List
# l=[8,6,5,2]
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
#liast comprihention 
# i=0
# lst=[ i+5 for i in range(5)]
# print(lst)
# i=0
# lst=[ i+5 for i in range(5) if i%2==0]
# print(lst)
#methods(inbuilt function)of list 
# x=[89,95,65,86,20,10]
# mood=["sad","sleppy","hungree"]
# print(mood)
# mood.append("happy")
# print(mood)
# print(mood.index("happy"))
# print(mood.count("happy"))
#x=mood.copy()
# print(x)
# mood.insert(2,"angrry")
# print(mood)
# mood.extend(x)
# print(mood)
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
# x.reverse()
# print(x)
#tupple
# tup=(1,2,3,"string")
# print(type(tup))
# print(tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# if 3 in tup:
#     print("yes 3 exist in tup")
# tup2=tup[0:3]
# print(tup2)
#operations on tuple
# print(tup.count(3))
# print(tup.index(1))
# print(len(tup))
#string formating  
# statement="{0} is a beautiful lady and i like her {1}"
# name="kirti"
# ulike="personality"
# print(statement.format(name,ulike))
# print(f"{name} is a beautiful lady and i like her {ulike}")
#Recursion
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
#fibonachi sequence
# s={1,1,0,6,7,8}
# print(s)
# greeting={"hello","thank you","good morning","good afternoon", " good night "}
# for wish in greeting:
#     print(wish)
#function of set 
# set1={1,2,3,7}
# set2={4,5,6,7}
# print( set1 ,"\n", set2 )
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.difference(set2))
# print(set1.isdisjoint(set2))
# print(set1.issuperset(set2))
# set1.add(5)
# print(set1)
# set1.remove(5)
# print(set1)
# print(set1.pop())
#dictinories in python 
# dic={"rool1":"karan","rool2":"pranav","rool3":"tanvi","rool4":"suvesh","rool5":"kirti"}
# dic2={122:"karan",123:"pranav",124:"tanvi",125:"suvesh",126:"kirti"}
# print(dic["rool1"])
# print(dic.get("rool2"))
# print(dic.keys())
# print(dic.values())
# dic.update(dic2)
# print(dic)
# dic.pop("rool1")
# print(dic)
# dic.popitem()
# print(dic)
# for i in range(5):
#   print(i)
# else:print("sorry no i")
# for i in range(5):
#   print(i)
#   if i==4:
#     break
# else:print("sorry no i")
#handling execption error
# a=input("Enter a vald number to print a table :")
# print(f"multipication of table {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i}={int(a)*i}" )
# except:
#     print("sorry some error occured")
# print("some inp lines of code")
# print("end of program ")
# try:
#     num=int(input("enter an integer :"))
#     a=[1,2,3,4,5]
#     print(a[num])
# except ValueError:
#        print("number entered is not an integer :(")
# except IndexError:
#        print("enter index does not exist :(")
# finally keyword
# def fun1  ():
#     try:
#         list=[1,2,3,4]
#         print(list)
#         i=int(input("Enter any index of list"))
#         print(list(i))
#         return 0 
#     except:
#         print("some error occured!!!")
#         return 1
#     finally:
#      print(" i am always executed ")
# print(" this is the imple print function out of the function ")
# x=fun1()
# print(x)
#short hand if else
# a = 1
# b = 1
# print("A is garater") if a > b else print("a and b are equal") if a == b else print("B is greter")
# c = 9 if a>b else 0
# print(c)
#enumrate
# marks=[0,9,50,60,70,90,100]
# for i in marks:
#     print (i)
#     if(i==100):
#         print("its an high score")
#     i= i+1
#this code is similer to this one 
# for i,marks in enumerate(marks):
#     print(i)
#     if(i==6):
#      print("its an high score")
# import pandas as pd
# print(pd.__version__)
# def main():
#     print("runnning code directly ")
#     if __name__=="__main__":
#      main()
#local or global veriables
# x=7
# print(f"this is the global x veriable{x}")
# def hello():
#     global x
#     x=9
#     print(f"hello the local veriable x is{x}")
# hello()
# print(f"out of function x is {x}")
# i=0
# f=open("myfile.txt","r")
# while True:
#     i=i+1
#     line =f.readline()
#     if not line:
#      break 
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of student {i} in maths is :{m1}")
#     print(f"Marks of student {i} in science is :{m2}")
#     print(f"Marks of student {i} in history is :{m3}")
#     print (line)
# with open ("myfile.txt","r") as f :
#  print(type(f) )
#  f.seek(10)
#  data=f.read(5) 
#  print(data)
#lambla functon in python 
# def apply(fx,value):
#      return 6+fx(value)
# cube =lambda x:x*x*x
# print(apply(cube,2))
# map 
# def cube(x):
#     return x*x*x
# print(cube(2))
# l=[1,2,3,4,5]
#newl=[]
#for number in l:
    #newl.append(cube(number))
# newl=list(map(cube,l))
# print(newl)
#filter
# def filter_filter(a):
#     return a>2
# newnewl=list(filter(filter_filter,l))
# print(newnewl)
#reduce
# from functools import reduce
# numbers=[1,2,3,4,5]
# def mysum(x,y):
#      return x+y
# sum= reduce(mysum,numbers)
# print(sum)
# a=[1,2,43]
# b=[1,2,43]
# print(a is b)#compares exact location of object in memory 
# print(a == b)#compares value of memory
#classes and objects in python 
# class student:
#     name="name of student *: "
#     age="age of student *:"
#     college="college of student *:"
#     def studentinfo(self):
#      print(f"name of student is = {self.name}\nage of student is = {self.age}\ncollege name of student is = {self.college}")
# student1=student()
# student1.name='kirti'
# student1.age='19'
# student1.studentinfo()
# student1.college='indala college'
# student2=student()
# student2.name='asma'
# student2.age='19'
# student2.college=' BK birla college'
# student2.studentinfo()
# student3=student()
# student3.name='tushar'
# student3.age='19'
# student3.college='DY patil univercity pune '
# student3.studentinfo()
#decorator
# def decorator(fun1):
#      def decoretedfun1(*args, **kwargs):
#           print("good morning")
#           fun1(*args, **kwargs)
#           print("have a nice day!!")
#      return decoretedfun1
# @decorator
# def hello():
#      print("hello world")
# @decorator
# def add(a, b):
#   print(a+b)
# hello()
# add(1,2)
class MyClass:
  def __init__(self, value):
      self._value = value
  def show(self):
    print(f"Value is {self._value}")
  @property
  def ten_value(self):
      return 10* self._value 
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()











