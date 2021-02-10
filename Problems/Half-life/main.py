amount = int(input())
end_amount = int(input())
periods = 0
while amount >= end_amount:
    amount /= 2
    periods += 1
print(periods * 12)