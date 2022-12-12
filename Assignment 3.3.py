score = input("Enter Score: (Between 0.0 and 1.0)")
score = float(score)

if score < 0:
    print("ERROR: Is the score actually negative?")
elif score > 1:
    print("ERROR: Is the score actually that high?")
else:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
