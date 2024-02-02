#Exercise 7:this program will rename al the png files
import os

files = os.listdir("clutteredFolder")#mention the name of existing png folder
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1