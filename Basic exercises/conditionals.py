
score = float(input("Input your score:"))

if 10 >= score >= 9:
    letter = "A"
elif 9 > score >= 7:
    letter = "B"
elif 7 > score >= 5:
    letter = "C"
elif 5 > score >= 3:
    letter = "D"
elif 3 > score >= 0:
    letter = "F"
else:
    letter = None

if letter == None:
    print("Score outside of grading range")
else:
    print("Score:", score, "-->", letter)
