'''
print ("hello")
x=5
y=6
if x==1:
    print (x)
elif x==5:
    print (y)


print (y)
hello = "hello"

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

print (str(x) + " "+ str(y)+" " + hello)
# So i will create a name template using special characters
name="Ruben"
age=18
print ("Hello my name is %s and I am %s years old" %(name,age))
#reverse a string
print (name[::-1])
#loops
chocolateBars=["vanilla","dark","milk"]

for bars in chocolateBars:
    print (bars)

#using else with loops
count =0
while(count<5):
    
    count +=1
else:
    print("count value reached %d" %(count))
if (count==5):
    print ("count reached")

'''
print ("hello my dawg")