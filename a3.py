n1= int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))

while(n2 !=0):
    t=n2
    n2=n1%n2
    n1=t
hcf=n1
print("HCF of the numbers are:", hcf)