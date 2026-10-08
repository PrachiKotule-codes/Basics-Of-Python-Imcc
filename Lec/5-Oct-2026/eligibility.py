role=input("Are you a student ? (Yes/No): ")
age = int (input ("Enter your age : "))
eligible =(role == "Yes") and (age < 21)
print("eligible : ", eligible)