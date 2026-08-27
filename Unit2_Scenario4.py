n = int(input("Number of houses: "))

houses = []

for i in range(n):
    amount = int(input(f"Amount in house {i + 1}: "))
    houses.append(amount)

if n == 0:
    print("Maximum possible amount: 0")

elif n == 1:
    print("Maximum possible amount:", houses[0])

else:
    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    print("Maximum possible amount:", dp[n - 1])
