import sys

def hvlcs(A, B, values):
    n, m = len(A), len(B)
    dp = []

    for i in range(n + 1):
        row = []
        for j in range(m + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[A[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    subseq = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            subseq.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    subseq.reverse()
    return dp[n][m], ''.join(subseq)

def read_input(filename):
    with open(filename, 'r') as f:
        K = int(f.readline().strip())
        values = {}

        for _ in range(K):
            ch, val = f.readline().split()
            values[ch] = int(val)

        A = f.readline().strip()
        B = f.readline().strip()
    return A, B, values

if __name__ == "__main__":
    filename = sys.argv[1]
    A, B, values = read_input(filename)
    max_val, subseq = hvlcs(A, B, values)
    print(max_val)
    print(subseq)