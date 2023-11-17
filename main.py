b = 3
a = 5
s = ""
o = "o "

for i in range(b):
  s += o
s += "\n"
for i in range(a-2):
  s += o
  for i in range(b-2):
    s += "  "
  s += o + "\n"
if a>1: 
  for i in range(b):
    s += o

print(s)