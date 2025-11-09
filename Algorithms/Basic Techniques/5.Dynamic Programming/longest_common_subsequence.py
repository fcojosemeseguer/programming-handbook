import numpy as np

# Time complexity : O(m * n)

def LCS(string1, string2):
    m, n = len(string1), len(string2)
    table = np.zeros((m + 1, n + 1))  # Initialize DP table

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:  # Match found
                table[i][j] = table[i - 1][j - 1] + 1
            else:  # No match, take max from previous values
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table


if __name__ == "__main__":
    string1 = "abcdefghi"
    string2 = "cdgi"
    table = LCS(string1, string2)
    print(table)
