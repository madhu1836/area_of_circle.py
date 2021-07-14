#area of circle
a=float(input()) 
pi=3.14
area= pi*a*a 
print(area)

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
