def print_dp_table(dp, rows=None, cols=None):
    if rows is None:
        rows = len(dp)
    if cols is None:
        cols = len(dp[0]) if dp else 0
    for i in range(rows):
        print(" ".join(f"{dp[i][j]:3}" for j in range(cols)))