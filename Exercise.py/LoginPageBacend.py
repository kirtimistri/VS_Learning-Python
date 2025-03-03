print("Enter the Username:")
a=input()
print("Enter teh Password:")
b=input()
f=open("myfile.txt",'w')
lines=[a,b]
for line in lines:
    f.write(line + "\n")
f.close()
