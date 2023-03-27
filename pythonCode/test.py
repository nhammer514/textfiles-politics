import os

workingDir = os.getcwd()
CollPath = os.path.join(workingDir, '../regexConsp')
insideDir = os.listdir(CollPath)
print(insideDir)