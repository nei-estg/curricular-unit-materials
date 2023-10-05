import re

input3="Ana Maria de Almeida e Santos"
input2="Joao Pedro de Sousa"
input1="Marinela Santos Ferreira e Silva de Sousa"

pattern=re.compile(r'[A-Z][a-z]+')
arr=[]
str=""
for match in re.finditer(pattern, input2):
   s = match.start()
   e = match.end()
   arr.append(input2[s:e])

print(arr)
str+=arr[0].lower()+"."
str+=arr[len(arr)-2][0].lower()+"."
str+=arr[len(arr)-1].lower()+"@contocontigo.pt"
print(str)