 
x=0
y=0
print("WELCOME TO KBC\nfirst queston on your screen")
time.sleep(3)
print("FIRST QUESTION APKI SCREEN PAR YE ")
time.sleep(2)
print("YERAHA!!")
question1=["what is the colour of sky ?","option 1 : blue","option 2 : red","option 3 : white"," option 4 : pink"]
print(question1[0])
print(question1[1])
print(question1[2])
print(question1[3])
print(question1[4])
user=int(input())
print("COMPUTER G OPTION ",user,"LOCK KIYA JAYE!!")
match user:
    case 1:
        print("option A lock!!")
    case 2:
        print("option 2 lock!!")
    case 3:
        print("option 3 lock !!!")
    case 4:
        print("option 4 lock !!")
time.sleep(2.5)        
choice=user
if (1<=choice and 1>=choice):
  print(choice)
  print(" CONGRATULATION!!!\ncorrect answer you won 2 rs")
  x=2
else:
    print("wrong answer")
print("next question apki scren par")  
time.sleep(2.5) 
print("YE RAHA!!") 
time.sleep(2)