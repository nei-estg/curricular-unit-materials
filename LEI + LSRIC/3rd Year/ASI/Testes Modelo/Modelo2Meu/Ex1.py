import re

input= "jpm@estgf.ipp.pt,mmo@aulas.pt,abc@gmail.com,abd@gmail.com"

pattern=re.compile(
    r'[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[A-Za-z-.]+'
)
with open('emails.txt','w')as fp:
    for email in re.findall(pattern, input):
        fp.write(email+"\n")
fp.close()