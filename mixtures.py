def mixtures(colors):
    n = len(colors)
    dp = [[0] * n for _ in range(n)]
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + colors[i]) % 100

    def sum_range(i, j):
        """ Segédfüggvény a keverék színének kiszámításához. """
        return (prefix_sum[j + 1] - prefix_sum[i]) % 100

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + sum_range(i, k) * sum_range(k + 1, j)
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

if __name__ == "__main__":
    colors = list(map(int, input("Add meg a keverék színeit (szóközzel elválasztva): ").split()))
    print("A minimális keverési költség:", mixtures(colors))
