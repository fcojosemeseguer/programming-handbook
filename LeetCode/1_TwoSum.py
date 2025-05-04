def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        h[num] = i

    for i, num in enumerate(nums):
        desired = target - num
        if desired in h and h[desired] != i:
            return f"Values: {num, desired} \nIndexes:{i, h[desired]}"  # values and indexes


if __name__ == "__main__":
    lista = [3, 6, 2, 5, 9, 12]
    sol = twoSum(lista, 8)
    print(sol)
