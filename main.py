import random

def JustNumber():
  code = random.randint(0000, 9999)
  print("Code: " + str(code))
  codeD = 0000
  find = 1
  while find:
    if codeD == code:
      print("Code as been find\nThe code is " + str(codeD))
      find = 0
    else:
      codeD += 1
      
JustNumber()
