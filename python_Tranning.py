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
a=[1,2,3,4,5,6,7,8,9,10]
for i in a :
    print(i)
print("\n --------------------!!ERROR!!------------------------")
#for loops 3rd instence 
for j in range(1,10,2):
    print(j*2)

# star pattern 
#  *
#  **
#  ***
#  ****
#  *****

P=['@','@ @','@ @ @','@ @ @ @','@ @ @ @ @']
for i in P:
    print(i)

# nested for loop 
A=[1,2,3,4,5,6,7,8,9,10]
B=[11,12,13,14,15,16,17,18,19,20]
for i in A:
    for j in B: 
        print(i,j)