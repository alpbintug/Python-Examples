a = 10
b = 6
#Arithmetic Operators
print(a/b) #Division, Output: 1.6666666666666667
print(a*b) #Multiplication, Output: 60
print(a%b) #Modulus, Output: 4
print(b**2) #Exponent, Output: 36
print(a//b) #Floor division, Output: 1
b**=0.5 #Short writing for b = b^(1/2)
print(b) #Output: 2.449489742783178
b**=2 # b = b^2
print(b)#Output: 5.999999999999999

#Logic operators
print(a!=b) #Not equal, Output: True
print(a==b) #Equal, Output: False

a = b = 5
print(a<b) #Output: False
print(a>b) #Output: False

a = "Hello"
b = "hello"
print(a==b) #Output: False

b = "Hello"
print(a == b) #Output: True

a+=b
print(a) #Output: HelloHello
