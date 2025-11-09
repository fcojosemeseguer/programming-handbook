## Find max of a list using a Divide and Conquer Algorithm
def FindMaximumElement(lst):
    if len(lst) == 0:
        return None
    return FindMax(0, len(lst) - 1, lst)


def FindMax(i, j, lst):
    if i == j:
        return lst[i]

    mid = (i + j) // 2

    return max(FindMax(i, mid, lst), FindMax(mid + 1, j, lst))


# Example
if __name__ == "__main__":
    lst = [1, 5, 2, 7, 3, 9, 6, 3, 6]
    max_el = FindMaximumElement(lst)
    print(max_el)
