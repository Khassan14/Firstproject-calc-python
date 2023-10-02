num1 = int(input("enter first number " ))
num2 = int(input("enter second number "))

print("choose calulation: \n"
      "add \n"
      "subtract \n"
      "divide \n"
      "multiply")
calc = input()
if calc == "Add" or "add":
      ans = num1 + num2
elif calc == "Subtract" or "subtract":
      ans = num1 - num2
elif calc == "Divide" or "divide":
      ans = num1/num2
elif calc == "Multiply" or "multiply":
      ans = num1*num2
else:
      print ("unable to identify input please try using numbers")
print(ans)
