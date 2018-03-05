names_file = open("names.txt", encoding="utf-8") #파일을 열어서
data = names_file.read()	#내용을 읽고 쓴다음에
names_file.close()	#안쓰니까 닫자

print(data)