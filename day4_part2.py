import re

range_min = 278384
range_max = 824795
pwd = [2, 7, 8, 3, 8, 4]

def increase():
  global pwd
  
  for i in reversed(range(6)):
    pwd[i] += 1
    if pwd[i] == 10:
      pwd[i] = 0
    else:
      break

def check1():
  global pwd

  for i in range(5):
    if pwd[i+1] < pwd[i]:
      return False
  return True

def check2():
  global pwd

  for i in range(1,5):
    if (pwd[i] == pwd[i-1]) or (pwd[i] == pwd[i+1]):
      return True
  return False

def check3(test):
  global pwd
  
  #pattern = re.compile("(\d)\1\1")
  
  #if pattern.search(test):
  if re.search(r"(\d)\1\1+", test):
    return True
  else:
    return False


combinations = range_max - range_min
valid_pwd = 0
list_valid = []
num_valid = []

for i in range(combinations+1):
  if check1() and check2():
    list_valid.append(pwd[:])
  increase()

for p in list_valid:
  s = [str(i) for i in p]
  temp =  "".join(s)
  print(temp)
  if not check3(temp):
    valid_pwd += 1
    num_valid.append(temp)

#print(num_valid)
#print(valid_pwd)
