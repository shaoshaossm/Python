file = open("README", "a+")
text = file.read()
file.write("aaa")
print(text)
file.close()
