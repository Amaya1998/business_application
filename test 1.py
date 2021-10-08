print("Python program intended to compute the roots of the quadratic equation ax2+bx +c=0 provided that b2 − 4ac >=0 , given integers a, b and c")
a = int(input("Enter a :))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
delta = b*b - 4*c
if delta < 0:
print("complex roots !")
else:
t= math.sqrt(delta)
r1= (-b -t) / (2*a)
r2= (-b +t) / (2*a)
print("Roots are: ", r1, r2) # display the roots
