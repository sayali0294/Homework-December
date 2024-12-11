#print numbers 1 to 10
for i in range(1,11):
    print(i)


#Print first 10 even numbers
for i in range(2,21,2):
     print(i)

#print first 10 odd numbers
for i in range (1,20,2):
     print(i)

#table of 5
for i in range(1,11):
    print(i)

#sum of Numbers 1 to 10
total=0
for i in range(1,11):
     total+=i
     print(total)

#reverse a string
text="hello"
reversed_text=""
for char in text:
     reversed_text=char+ reversed_text
     print(reversed_text)

#print each character of string
for char in "Python":
     print (char)

#check if a number is prime
num=7
is_prime=True
for i in range (2, num):
     if num%i==0:
          is_prime=False
          break
     print("prime"if is_prime else "Not prime")

#count vowels in string
text="hello World"
count=0
for char in text:
     if char in "AEIOUaeiou":
          count+=1
          print("vowel Count: ", count)


#find the largest number in list
numbers=[3,5,2,8,6]
largest=numbers[0]
for num in numbers:
     if num> largest:
          largest=num
          print("largest")



#Sum of elements in list
numbers=[1,2,3,4,5,6]
total =0
for num in numbers:
     total+=num
     print(total)


          