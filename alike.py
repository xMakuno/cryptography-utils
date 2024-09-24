correct = input("Enter the correct string:\n")
wrong = input("Enter the wrong string:\n")

points = 0
for i in range(len(correct)):
    if correct[i] == wrong[i]:
        points+=1
print(f"This is your score: {points}")