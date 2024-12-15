def coin_combinations(n, coins):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, n + 1):
            dp[amount] = (dp[amount] + dp[amount - coin]) % MOD
    return dp[n]

if __name__ == "__main__":
    n = int(input("Add meg a célösszeget: "))
    coins = list(map(int, input("Add meg a pénzérmék értékeit (szóközzel elválasztva): ").split()))
    print(f"A(z) {n} összeget {coin_combinations(n, coins)} különböző módon lehet előállítani.")