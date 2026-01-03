#Take input from user
num1 = float(input(" Please Enter the First value Num1 : "))
num2 = float(input(" Please Enter the Second value Num2 : "))

#calculate the HCF of user entered numbers
while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1
#display the result
print("HCF of num1 and num2 is",hcf)
