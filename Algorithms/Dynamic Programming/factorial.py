def fact(n):
    fac_num = []
    if n == 1:
        fac_num.append(1)
    else:
        fac_num.append(1)

    for i in range(1, n):
        fac_num.append(fac_num[i - 1] * (i + 1))

    return fac_num[-1], fac_num


if __name__ == "__main__":
    factorial_20 = fact(5)
    print(factorial_20)
