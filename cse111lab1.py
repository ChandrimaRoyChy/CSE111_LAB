# -*- coding: utf-8 -*-
"""CSE111Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jMrrQDGrLe5lgjEnQDbnxC4fQNv2TxNL
"""

#str1
str1=input('Enter a string:')
upper=0
lower=0

for i in str1:
  x=ord(i)
  if x>=65 and x<=90:
    upper+=1
  elif x>=97 and x<=122:
    lower+=1
if upper>lower:
  print(str1.upper())
else:
  print(str1.lower())

#str2
number=0
word=0
str1=input('Enter a string:')

for i in str1:
  x=ord(i)
  if x>=48 and x<=57:
    number+=1
  elif x>=65 and x<=90 or x>=97 and x<=122:
    word+=1
if word>=1 and number>=1:
  print('MIXED')
elif word==0:
  print('NUMBER')
elif number==0:
  print('WORD')

#str3
str1=input('Enter a string:')
loop=False
new_str=''

for i in str1:
    if loop== True:
      if i>=65 or i<=90 :
        loop=False
        new_str= new_str[::-1]
      else:
        new_str+= i
    else:
       if i is str1 and (i>=65 or i<=90):
         loop=True
print(new_str)

#str4
str1=input("Enter the first string:")
str2=input("Enter the second string:")
new_str=''
count=0
for idx1 in range(len(str1)):
  if str1[idx1] in str2:
    new_str+=str1[idx1]
    count+=1
for idx2 in range(len(str2)):
    if str2[idx2] in str1:
      new_str+=str2[idx2]
      count+=1
if count>0:
  print(new_str)
else:
  print("Nothing in common.")

#str5
password = input("Enter a passoword: ")
specialchacters = "@#$_"
upper = 0
lower = 0
digit= 0
special = 0
for index in password:
  x=ord(index)
  if index in specialchacters:
    special+=1
  elif x>=65 and x<=90:
    upper += 1
  elif x>=97 and x<=122:
    lower += 1
  elif x>=48 and x<=57:
    digit += 1
list = []
if lower == 0:
 list.append('Lowercase character missing')
else:
 pass
if upper == 0:
 list.append('Uppercase character missing')
else:
 pass
if digit == 0:
 list.append('Digit missing')
else:
 pass
if special == 0:
 list.append('Special character missing')
else:
 pass
length=len(list)
if length==0:
 print('OK')
else:
 list1=','.join(list)
 print(list1)

#list1
all_list = []
new_list = []

while True:
 number = input("Enter the number: ")
 if number == "STOP":
   break
 else:
   all_list.append(number)
   if number not in new_list:
     new_list.append(number)
for char in new_list:
 print( char,"-",all_list.count(char),"times")

#list2
lst=[]
final_lst=[]
sum=0

lst_len=int(input("Enter the numbers of lists:"))

for i in range(lst_len):
  list1=input("Enter the numbers:").split(" ")
  add=0
  for j in list1:
    lst.append(int(j))
    add=add+(int(j))

  if add>sum:
    sum=add
    #for k in list1:
      #inal_lst.append(int(k))
    final_lst=list1

print(sum)
print(final_lst)

#list3
list1 = []
while True: 
 user=input("Enter your list here: ")
 if user!= "STOP":
   list1.append(user)
 else:
   break
for count in list1:
 list1=count.split(" ")
 list2= []
 for x in range(len(list1)-1): 
   difference= int(list1[x])-int(list1[x+1])
   if difference<0:
     list2.append((difference*-1))
   else:
    list2.append(difference)
 ub_jumper = True
 for count in range(1,len(list1)):
   if count in list2:
     pass
   else:
     ub_jumper = False
 if ub_jumper == True:
   print("UB Jumper")
 else:
   print("Not UB Jumper")

#list4
n,k=[int(i) for i in input("Enter the value of n and k:").split( )]
members=input("enter the team members:").split(' ')
lst=[]
for i in range(len(members)):
  if int(members[i])<=(5-k):
    lst.append(int(members[i]))
print(len(lst)//3)

#dictionary&tuple1
dict1={}
dict2={}

user_input1=input("Enter the first dictionary:").split(",")
user_input2=input("Enter the second dictionary:").split(",")

for idx1 in user_input1:
  key1,value1=idx1.split(":")
  dict1[key1]=int(value1)
for idx2 in user_input2:
  key2,value2=idx2.split(":")
  dict2[key2]=int(value2)

new_dict=dict1

for key,value in dict2.items():
  if key not in dict1:
    new_dict[key]=value
  else:
    new_dict[key]+=value

print(new_dict)

list1=[]

for key,value in dict1.items():
  if value in list1:
    pass
  else:
    list1.append(value)
    
list2=sorted(list1)
tuple1=tuple(list2)

print("Values",tuple1)

#dictionary&tuple2
dict1={}
while True:
  user=input("Enter the numbers:")
  if user!='STOP':
    user=int(user)
    if user in dict1:
      dict1[user]+=1
    else:
      dict1[user]=1
  else:
      break

for key,value in dict1.items():
   print(key,"-",value,"times")

#dictionary&tuple3
dict1={}
user=input("Enter the dictionary:").split(",")

for idx1 in user:
  key1,value1=idx1.split(":")
  dict1[key1]=value1

final_dict={}

for keys,values in dict1.items():
  if final_dict.get(values)==None:
    final_dict[values]=[keys]
  else:
    final_dict[values].append(keys)

print(final_dict)

#dictionary&tuple4
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
dict1 = {}
dict2= {}
if len(str1) != len(str2) :
  print("Those strings are not anagrams.")
else:
  for i in str1:
    if dict1.get(i) == None:
      dict1[i] = 1
    else:
      dict1[i] = dict1[i] + 1
  for i in str2:
    if dict2.get(i) == None:
      dict2[i] = 1
    else:
      dict2[i] = dict2[i] + 1

  count=0
  for i in str1:
    if dict1.get(i)!=dict2.get(i):
      count = count + 1
    else:
      continue
  if count == 0:
    print("Those strings are anagrams.")
  else:
    print("Those strings are not anagrams.")

dict1={'1':'.,?!:','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ','0':'' }
str1=input("Enter a string:").upper()
for i in str1:
  for key,value in dict1.items():
    if i in value:
      count=value.find(i)
      for j in range(count+1):
        print(key,end='')

#function1
#height=float(input("Enter the height in cm: "))
#weight=float(input("Enter the weight in kg: "))

def BMI_Calculate(height,weight):
  BMI=round((weight/(height/100)**2),1)
  #BMI=round()
  print("Score is",BMI,end=".")
  if BMI<18.5:
    print("You are Underweight")
  elif BMI>=18.5 and BMI<=24.9:
    print("You are Normal")
  elif BMI>=25 and BMI<=30:
    print("You are Overweight")
  elif BMI>30:
    print("You are Obese")
 # return f"Score is{BMI:0.1f}.You are {result}"

#BMI_Calculate(height,weight)
BMI_Calculate(175,96)

#function2
def values(minimum,maximum,divisor):
  sum=0
  for i in range(maximum):
    if i<minimum:
      continue
    else:
      if i%divisor==0:
        sum+=i
  return sum
print(values(0,10,2))

#function3
def FoodOrder(menu,location="Mohakhali"):
  if location!="Mohakhali":
    delivery_charge=60
  else:
    delivery_charge=40

  if menu=="BBQ Chicken Cheese Burger":
    price=250
  elif menu=="Beef Burger":
    price=170
  elif menu=="Naga Drums":
    price=200
  else:
    return "Menu is not available"
  
  tax=price*(8/100)
  Total_Price=price+delivery_charge+tax
  return Total_Price

print(FoodOrder("Beef Burger","Dhanmondi"))

#function4
def replace_domain(email,domain,default_domain=""):
  idx=email.index("@")
  if email[idx:]==domain:
    result="Unchanged:"
  else:
    result="Changed:"
    
  new_id=email[:idx+1]
  new_id+=domain
  return result+new_id
#replace_domain("alice@kaaj.com","sheba.xyz","kaaj.com")
print(replace_domain("alice@kaaj.com","sheba.xyz","kaaj.com"))

#function5
def PalindrommeChecker(string_input):
  string=""#empty string
  for i in string_input:
    if i!=" ":
      string+=i
  if string==string[::-1]:
    return "Palindrome"
  else:
    return "Not Palindrome"

string_input=input().lower()
PalindrommeChecker(string_input)

#function6
def capitalize(st1):
  st2 = ''
  for a in range(len(st1)):
    if a == 0:
      st2 += chr(ord(st1[a])-32)
    elif st1[a-2] == "." or st1[a-2] == "!" or st1[a-2] == "?":
      st2 += chr(ord(st1[a])-32)
    elif st1[a] == "i" and st1[a-1] == " " and st1[a+1] == " ":
      st2 += chr(ord(st1[a]) - 32)
    else:
      st2 += st1[a]
      return st2

string = input('Enter a string: ')
print(capitalize(string))

def PunctuationChecker(Text):
 list1 = []
 str1 = ''
 for i in Text:
 str1 = str1 + i
 if i in '.!?':
 if str1[0] == ' ':
 str1 = str1[1:]
 list1.append(str1)
 str1 = ''
 list2 = []
 str2 = ''
 for i in list1:
 str2 = str2 + i[0].upper()
 for j in range(1, len(i)):
 str2 = str2 + i[j]
 list2.append(str2)
 str2 = ''
 list3 = []
 for i in list2:
 x = i.split()
 for j in x:
 if j == 'i' and len(j) == 1 or j == 'i.' and len(j) == 2:
 if j == 'i' and len(j) == 1:
 list3.append('I')
 else:
 list3.append('I.')
 elif j == 'i' and len(j) == 1 or j == 'i?' and len(j) == 2:
 if j == 'i' and len(j) == 1:
 list3.append('I')
 else:
 list3.append('I?')
 elif j == 'i' and len(j) == 1 or j == 'i!' and len(j) == 2:
 if j == 'i' and len(j) == 1:
 list3.append('I')
 else:
 list3.append('I!')
 else:
 list3.append(j)
6/25/2021 Assignment-2 - Jupyter Notebook
localhost:8888/notebooks/Assignment-2.ipynb 9/9
In [ ]:
Enter the string: my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily.do
you know my pet dog’s name? i love my pet very much.
My favourite animal is dog. A has sharp teeth so that can eat flesh very easily. Do you know my pet dog’s nam
e? I love much. 
 final_str=""
 for i in list3:
 if i not in final_str:
 final_str=final_str +i+" "
 return final_str
Text = input("Enter the string: ")
print(PunctuationChecker(Text)

def capitalizer(sentence):
  new_str=''
  for i in range(len(setence)):
    if i==0:
      new_str+=sentence[i].upper()
    elif sentence[i-2]=='.' or sentence[i-2]=='!' or sentence[i-2]=='?':
      new_str+=sentence[i].upper()
    elif sentence[i]=='i' and sentence[i-1]==' ' and sentence[i+1]==' ':
      new_str+=sentence[i].upper()
    else:
      new_str+=sentence[i]
  print(new_str)
capitalizer("my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily.do you know my pet dog’s name? i love my pet very much.")