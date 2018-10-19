import shutil
import os

#디렉토리 path변경
os.chdir("C:/Users/owner/PycharmProjects/MakePerson/mr")

#현재 path 출력
print(os.getcwd())

#현재 path에서 파일 생성
f = open('testhhhhhhhhhhhhhhhhhhhhhhh.txt' , "wt")
f.write("test")
f.close()
