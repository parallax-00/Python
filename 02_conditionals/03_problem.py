score = int(input("Enter the Score of Student:"))

if score<60:
    print("Grade assigned:'F'")
elif 60<=score<=69:
    print("Grade assigned:'E")
elif 70<=score<=79:
    print("Grade assigned:'C")
elif 80<=score<=89:
    print("Grade assigned:'B")
elif 90<=score<=100:
    print("Grade assigned:'A")
else: print("Enter score from 0 to 100")