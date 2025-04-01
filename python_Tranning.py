#create a nested loop which will be loop again when user will put an invalid input 
# def event():
#     print("Enter in which evet you are participating in \n 1: Sports \n 2: Dj night \n3: CulturalEvent")
#     a=int(input("Enter Your choice : "))
    
#     while(a):
       
#         if(a>0 or a<=3):
#             if a==1:
#                 print(" 1: Sports \nGo to first floor")
#                 break
#             elif a==2:
#                 print(" 2: Dj night \nGo to second floor")
#                 break
#             elif a==3:
#                 print(" 3: CulturalEvent \nGo to third floor")
#                 break
#             else:
#                 print("Enter a valid input \n --------------------!!ERROR!!------------------------")
#                 event()
#                 break
#         else:
#           print("Enter a valid input")

# event()

#for loop 
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a :
#     print(i)
# print("\n --------------------!!ERROR!!------------------------")
# #for loops 3rd instence 
# for j in range(1,10,2):
#     print(j*2)

# star pattern 
#  *
#  **
#  ***
#  ****
#  *****

# P=['@','@ @','@ @ @','@ @ @ @','@ @ @ @ @']

# for i in P:
#     print(i)

# #logic for dynamic pattern 
# def printstar():
#       i=0
#       for i in range(10) :
#             print("$ "*(i+1))
         

# printstar()
    # x=['$']
    # z=0
    # for i in x:
    #     x.append('$')
    #     z=z+1
    #     print(z)
    #     break
    #     for i in x:
    #         print(i)

# nested for loop 
# A=[1,2,3,4,5,6,7,8,9,10]
# B=[11,12,13,14,15,16,17,18,19,20]
# for i in A:
#     for j in B: 
#         print(i,j)

# for i in range(11):
#     print(i)


def carA():
    row=5
    j=30
    for row in range(row):
        for j in range(j):
            if(row==0 and (j>=6 and j<=16)
                or (row==1 and (j==5 or j==17))
                or (row==2 and (j==4 or j==18))
                or (row==3 and (j==3 or j==19))
                or (row==4 and (j>=0 and j<=2))
                or (row==4 and (j>=20 and j<=22))
                or (row==5 and (j==0 or j==22))               
                ):                
                print('@',end=' ') 
            else:
                print(' ',end=' ')
        print()

def carB():
    row=5
    j=30
    for row in range(row):
        for j in range(j):
            if(row==0 and (j>=3 and j<=16)
                or (row==1 and (j>=2 and j<=13))
                or (row==1 and j==17)
                or (row==2 and (j>=1 and j<=13))
                or (row==2 and j==18)
                or (row==3 and (j>=0 and j<=13))
                or (row==3 and j==19)
                or (row==4 and (j>=0 and j<=13))
                or (row==4 and (j>=20 and j<=22))
                or (row==5 and (j==0 or j==22))           
                ):  
                print('@',end=' ')
            else:
                print(' ',end=' ')
        print()
    

def weel2():
    row=[6,7,8,9]
    col=30
    for i in row:
        for j in range(col) :
             if( (i==6 and (j==0 or j==22))
                or (i==6 and (j>=5 and j<=6))
                or (i==6 and (j>=15 and j<=16))
                or (i==7 and (j==0 or j==22))
                or (i==7 and (j>=4 and j<=7))
                or (i==7 and (j>=14 and j<=17))
                or (i==8 and (j>=0 and j<=2))
                or (i==8 and (j>=4 and j<=7))
                or (i==8 and (j>=9 and j<=12))
                or (i==8 and (j>=14 and j<=17))
                or (i==8 and (j>=19 and j<=22))
                or (i==9 and (j>=5 and j<=6))
                or (i==9 and (j>=15 and j<=16))
                ):   
                print('@',end=' ')
             else:
                print(' ',end=' ')
        print()
    print("weel2")

def weel4():
    row=[6,7,8,9]
    col=30
    for i in row:
        for j in range(col) :
             if( 
                (i==6 and (j==0 or j==22))
                or (i==7 and (j==0 or j==22))
                or (i==7 and (j>=2 and j<=3))
                or (i==7 and (j>=7 and j<=8))
                or (i==7 and (j>=12 and j<=13))
                or (i==7 and (j>=17 and j<=18))
                or (i==7 and (j>=20 and j<=22))
                or (i==8 and (j>=1 and j<=4))
                or (i==8 and (j>=6 and j<=9))
                or (i==8 and (j>=11 and j<=14))
                or (i==8 and (j>=16 and j<=19))
                or (i==9 and (j>=2 and j<=3))
                or (i==9 and (j>=7 and j<=8))
                or (i==9 and (j>=12 and j<=13))
                or (i==9 and (j>=17 and j<=18))
                ):               
                print('@',end=' ')
             else:
                print(' ',end=' ')
        print()
    print("weel4")

def choice():
    print("Choose a car \n CAR A : 1 \n CAR B : 2 ")
    x=int(input("Enter Your Choice :"))
    print(f"Choose weels for car {x} \n 1 : Two weels \n 2 : Four weels ")
    y=int(input("Enter Your Choice :"))
    if (x==1 and y==1):
        carA()
        weel2()
    elif(x==1 and y==2):
        carA()
        weel4()          
    elif(x==2 and y==1):
        carB()
        weel2()   
    elif(x==2  and y ==2):
        carB()
        weel4()
    else:print(" invalid input \n -----------------!!ERROR!!---------------------")
carA()
# carB()
# weel4()
# weel2()        
# # from Python_clock import *
# samay()
# choice()
