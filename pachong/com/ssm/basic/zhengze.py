import re

key = "javapython1myslqpython1"

print(re.findall('python1', key)[1])

key = "<html><h1>hello world<h1></html>"
print(re.findall('<h1>(.*)<h1>', key))

string = "I like 170 girl"
print(re.findall('\d', string))

key = "http://www.baidu.com and https://www.shaoshaossm.github.io"
print(re.findall('https://', key))

key = 'am@shao.com'
print(re.findall('s.*?\.', key))

key = 'saas and asa and saaas'
print(re.findall('sa{1,2}s',key))

