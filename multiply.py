print("enter operand 1: ")
o1 = int(input())
print("enter operand 2: ")
o2 = int(input())
print("enter operator: ")
oper = input()

if oper == "*":
    print(str(o1) + " * " + str(o2) + " = " + str(o1*o2))
else:
    print("Invalid operator")