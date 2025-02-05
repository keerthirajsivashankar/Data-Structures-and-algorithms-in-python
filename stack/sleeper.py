n = int(input("Enter the seat number : "))
if n % 8 == 0:
    print("side upper")
elif n % 8 == 7:
    print("side lower")
elif n % 8 == 1 or n % 8 == 4 :
    print("Lower")
elif n % 8 == 2 or n % 8 == 5 :
    print("Middle")
elif n % 8 == 3 or n % 8 == 6 :
    print("upper")
    