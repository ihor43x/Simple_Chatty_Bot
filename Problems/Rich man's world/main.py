initial_deposit = int(input())
deposit = initial_deposit
months = 0
while deposit < 195000:
    deposit *= 1 + 0.08855 / 12
    deposit += initial_deposit
    months += 1
    print(f"month: {months}  cash:{deposit}")
print(months / 12)
