# Crie um programa em PYTHONque, dada uma linha como a indicada no “Input”, escreva num ficheiro de saída um endereço por
# linha (como indicado no Output). Deverá utilizar expressões regulares
import re

emails = "jpm@estgf.ipp.pt,mmo@aulas.pt,abc@gmail.com,abd@gmail.com"
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
with open('emails.txt', 'w') as fp:
    for email in re.findall(pattern, emails):
        fp.write(email + "\n")
    # s = match.start()
    # e = match.end()
    # fp.write(emails[s:e] + "\n")
fp.close()
