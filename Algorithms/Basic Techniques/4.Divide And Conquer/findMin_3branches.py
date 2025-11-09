# Find Minimum Element of a List breaking problem by 3 branches


def FindMinElement(lst):
    if not lst:
        return None
    return FindMin(0, len(lst) - 1, lst)


def FindMin(i, j, lst):
    if i == j:
        return lst[i]
    if j - i == 1:
        return min(lst[i], lst[j])
    if j - i == 2:
        return min(lst[i], lst[i + 1], lst[j])

    # Divide the range into three roughly equal parts
    third = (j - i + 1) // 3
    mid_1 = i + third - 1
    mid_2 = mid_1 + third

    # Ensure mid_2 doesn't exceed j
    mid_2 = min(mid_2, j - 1)

    return min(
        FindMin(i, mid_1, lst),
        FindMin(mid_1 + 1, mid_2, lst),
        FindMin(mid_2 + 1, j, lst),
    )


# Example

if __name__ == "__main__":
    lst = [3, 5, 6, 8, 2, 8, 1, 4, 7, 9]
    el_min = FindMinElement(lst)
    print(el_min)
