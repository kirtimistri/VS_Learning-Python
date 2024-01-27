#Exercise 1: calculator without switch case 
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
#exercise 2 : good morning sir
# import datetime
# currentTime = datetime.datetime.now()
# currentTime.hour
# if currentTime.hour < 12:
#    print('Good morning.')
# elif 12 <= currentTime.hour < 18:
#  print('Good afternoon.')
# else:
#  print('Good evening.')
# exwecise 3:koun banega carorepati(KBC)
# 2
# question1=["what is the colour of sky ?","option 1 : blue","option 2 : red","option 3 : white"," option 4 : pink"]
# print(question1[0])
# print(question1[1])
# print(question1[2])
# print(question1[3])
# print(question1[4])
# user=int(input())
# print(user)
# match user:
#     case 1:
#         print("option A lock!!")
#     case 2:
#         print("option 2 lock!!")
#     case 3:
#         print("option 3 lock !!!")
#     case 4:
#         print("option 4 lock !!")
# choice=user
# if (1<=choice and 1>=choice):
#   print(choice)
#   print(" CONGRATULATION!!!\ncorrect answer you won 2 rs")
# else:
#     print("wrong answer")
    

# question2=["what is the colour of grass ?","option 1 : blue","option 2 : red","option 3 : green","option 4 : pink"]
# print(question2[0])
# print(question2[1])
# print(question2[2])
# print(question2[3])
# print(question2[4])
# user=int(input())
# print(user)
# match user:
#     case 1:
#         print("option A lock!!")
#     case 2:
#         print("option B lock!!")
#     case 3:
#         print("option C lock !!!")
#     case 4:
#         print("option D lock !!")
# choice=user
# if (3>=choice and 3<=choice):
#   print(choice)
#   print(" CONGRATULATION!!!\ncorrect answer you won 2 rs")
# else:
#     print("wrong answer")
#   Exercise 4:the secret code language 
# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
# Ecsersice 3:SNAKE WATER GUN GAME
import random
print('Snake - Water - Gun')
# Input no. of rounds
n = int(input('Enter number of rounds: '))
# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']
# Round numbers
rounds = 1
# Count of computer wins
comp_win = 0
# Count of player wins
user_win = 0
# There will be n rounds of game
while rounds <= n:
	# Display round
	print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")
	# Exception handling
	try:
		player = input("Choose your option: ")
		print("players opion:",player)
	except EOFError as e:
		print(e)
	# Control of bad inputs
	if player != 's' and player != 'w' and player != 'g':
		print("Invalid input, try again\n")
		continue
	# random.choice() will randomly choose
	# item from list- options
	computer = random.choice(options)
	print("computers option:",computer)
	# Conditions based on the game rule
	if computer == 's':
		if player == 'w':
			comp_win += 1
		elif player == 'g':
			user_win += 1

	elif computer == 'w':
		if player == 'g':
			comp_win += 1
		elif player == 's':
			user_win += 1
			
	elif computer == 'g':
		if player == 's':
			comp_win += 1
		elif player == 'w':
			user_win += 1
	# Announce winner of every round
	if user_win > comp_win:
		print(f"You Won round {rounds}\n")
	elif comp_win > user_win:
		print(f"Computer Won round {rounds}\n")
	else:
		print("Draw!!\n")
	rounds += 1
# Final winner based on the number of wons
if user_win > comp_win:
	print("Congratulations!! You Won")
elif comp_win > user_win:
	print("You lose!!")
else:
	print("Match Draw!!")






