"""
Problem : Find the largest subseq of number grater than a number X

Example:
    -Input-
    S = [1, 6, 7, 4, 5, 6, 8, 9, 2, 10]
    X = 5

    -Output-
    [4 [5, 6, 8, 9]]

"""


def short(p, q):
    return p == q


def direct_solution(s, p, q, X):
    if s[p] >= X:
        return 1, p, q
    return 0, None, None


def divide(p, q):
    return (p + q) // 2


def combine(lista, sol1, sol2, m, X):
    c_left, p_left, q_left = sol1
    c_right, p_right, q_right = sol2

    # Case 1 : Direct Union. The border is continiuos
    if c_left != 0 and c_right != 0 and q_left == (p_right - 1):
        return c_left + c_right, p_left, q_right

    # Case 2 : NO Direct Union

    else:
        c_middle, p_middle, q_middle = 0, m, m

        # 2.1 We extend left to right
        if q_left == m:
            i = m + 1
            while lista[i] >= X:
                c_left += 1
                q_left = i
                i += 1

        # 2.2 We extend right to left
        elif p_right == m + 1:
            i = m
            while lista[i] >= X:
                c_right += 1
                p_right = i
                i -= 1

        # 2.3 We look for a greater concatenation at the border.
        elif lista[m] >= X:
            c_middle += 1

            i = m - 1
            while i >= 0 and lista[i] >= X:
                c_middle += 1
                p_middle = i
                i -= 1

            i = m + 1
            while i < len(lista) and lista[i] >= X:
                c_middle += 1
                q_middle = i
                i += 1

    # We compare the 3 different result, in order to get the longest
    if c_left > c_right:
        if c_left >= c_middle:
            return c_left, p_left, q_left
        else:
            return c_middle, p_middle, q_middle
    else:
        if c_right >= c_middle:
            return c_right, p_right, q_right
        else:
            return c_middle, p_middle, q_middle


def divide_and_conquer_longest_subseq_grather_than_X(s, p, q, X):
    if short(p, q):
        sol = direct_solution(s, p, q, X)
    else:
        m = divide(p, q)
        sol = combine(
            s,
            divide_and_conquer_longest_subseq_grather_than_X(s, p, m, X),
            divide_and_conquer_longest_subseq_grather_than_X(s, m + 1, q, X),
            m,
            X,
        )
    return sol


if __name__ == "__main__":

    lista = [1, 6, 7, 4, 5, 6, 8, 9, 2, 10]

    inicio = 0
    final = len(lista) - 1
    X = 5

    l, p, q = divide_and_conquer_longest_subseq_grather_than_X(lista, inicio, final, X)

    if l > 0:
        print(l, lista[p : q + 1])
    else:
        print("No solution")
