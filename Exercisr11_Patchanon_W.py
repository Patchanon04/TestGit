number = int(input("Enter a number : "))
for i in range(number):
    gap = " "*(number-(i+1))
    asterisk = "*"*((i*2)+1)
    print(gap,asterisk)
