a = True
b = False

c = "Ninjas"
print(type(b))

#relational operator
a = 10
b =20
print(a > b)   # a is greater than b
print(a < b)   # a is less than b
print(a >= b)  # a is greter than or equal to b 
print(a <= b)  # a is less than or equal to b 
print(a == b)  # a is equal to b
print(a != b)  # a is not equal to b

#logical oprator
c1 = a > 10
c2 = b > 10
r1 = c1 and c2
r2 = c1 or c2
r3 = not(c1)
print(r1)
print(r2)
print(r3)


#if else statement
a = True or False
if a:
    print("If Block")
    print("Woohoo!")
else:
    print("Else Block")
