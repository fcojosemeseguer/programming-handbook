def coin_changing(L, amount):
    denomination = []
    i = 0
    while i < len(L):
        num = int(amount / L[i])  # Same as amount // L[i]
        amount = amount - num * L[i]
        denomination.append(num)
        i += 1
    return denomination


if __name__ == "__main__":
    L = [500, 100, 50, 20, 10, 5, 2, 1]
    den = coin_changing(L, 657)
    print(den)

    """
    The preceding is an example of a Greedy approach, since at each step, the “best 
    option at that point” is selected, and we proceed further. The approach is good but 
    might not lead to an optimal solution always.
    """
