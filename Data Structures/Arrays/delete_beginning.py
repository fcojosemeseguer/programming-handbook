def del_beg(arr):
    n = len(arr)

    if n != 0:
        i = 1
        while i <= n - 1:
            arr[i - 1] = arr[i]
            i += 1
        arr[i - 1] = 0
    else:
        print("Underflow")


if __name__ == "__main__":
    lista = [
        54,
        23,
        12,
        20,
    ]
    print(f"Before: {lista}")
    del_beg(lista)
    print(f"After: {lista}")
