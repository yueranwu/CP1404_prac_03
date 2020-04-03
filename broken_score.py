"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent;
50 or more is a pass; below 50 is bad.
"""
score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif 50 <= score < 90:
    print("Passable")
elif score >= 90:
    print("Excellent")
else:
    print("Bad")
