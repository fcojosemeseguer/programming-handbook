def insert_beg(arr, item, max=None):
    n = len(arr)
    arr.append(0)

    if max is not None and n >= max:
        print("Overflow")

    else:
        i = n - 1
        while i >= 0:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = item
        n += 1


if __name__ == "__main__":
    lista = [
        54,
        23,
        12,
        20,
    ]
    insert_beg(lista, 1)
    print(lista)
