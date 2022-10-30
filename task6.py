print("----------------Prime and Non-Prime numbers Lists -------------------")
L = [int(num) for num in input("Enter any Number:\n ").split(',')]
PL = [] # Prime list
NPL = [] # Non Prime List

for number in L:
    count = 0
    for j in range(1,number):
        if number %j ==0:
            count += 1
    if count == 1:
         PL.append(number)
    else:
        NPL.append(number)

print("\n here are the prime numbers: ")
print(*PL, sep = ", ")
print("  ")
print("\n here are the Non-prime Numbers: ")
print(*NPL,sep = ", "  )
