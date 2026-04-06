import sys

def hvlcs(A, B, values):
    n, m = len(A), len(B)
    dp = []

    for i in range(n + 1): # Initialize array to 0. Includes empty string base case
        row = []
        for j in range(m + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1): # Recurrence Relation loop
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]: # Check if character is a match in both strings
                dp[i][j] = dp[i - 1][j - 1] + values[A[i - 1]] # Add value of the current character to the diagonal
            else: # Character does not match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # Take best value if we ignore character in string A/B

    # BACKTRACKING / POST-PROCESSING
    i, j = n, m
    subseq = [] # Holds characters as we go through table

    while i > 0 and j > 0: # Iterate backwards
        if A[i - 1] == B[j - 1]: # Check if characters are the same
            subseq.append(A[i - 1]) # Add character to the array
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]: # Check neighboring elements (up or left)
            i -= 1 # Move up
        else: 
            j -= 1 # Move left
    
    subseq.reverse() # Reverse string since we started at the end
    return dp[n][m], ''.join(subseq)

def read_input(filename): # Reading input as outlined in the spec
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