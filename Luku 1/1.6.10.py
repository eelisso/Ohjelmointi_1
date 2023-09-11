class Solution:
    euro_denominations = {
        50000: "five hundred-euro notes",
        20000: "two hundred-euro notes",
        10000: "one hundred-euro notes",
        5000: "fifty-euro notes",
        2000: "twenty-euro notes",
        1000: "ten-euro notes",
        500: "five-euro notes",
        200: "two-euro coins",
        100: "one-euro coins",
        50: "50 cent coins",
        20: "20 cent coins",
        10: "10 cent coins",
        5: "5 cent coins",
        2: "2 cent coins",
        1: "1 cent coins"
    }

    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coin_used = {0: {}}

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0 and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1
                    coin_used[a] = coin_used[a - c].copy()
                    coin_used[a][c] = coin_used[a].get(c, 0) + 1

        if dp[amount] == float('inf'):
            return -1, {}
        else:
            return dp[amount], coin_used[amount]

    def printCoinsUsed(self, coins_used):
        for coin, count in coins_used.items():
            if coin in self.euro_denominations:
                print(f"{count} {self.euro_denominations[coin]}")


p1 = Solution()
price = float(input("Purchase price: ")) * 100
amount_paid = float(input("Paid amount of money: ")) * 100
amount_rounded = round(amount_paid - price)
amount = (amount_rounded // 5) * 5
print(amount_rounded)
print(amount)

if amount < 0:
    print("Not enough funds.")
elif amount == 0:
    print("No change needed.")
else:
    result, coins_used = p1.coinChange(
        [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000], amount)
    if result == -1:
        print("It's impossible to give exact change.")
    else:
        print("Offer change:")
        p1.printCoinsUsed(coins_used)
