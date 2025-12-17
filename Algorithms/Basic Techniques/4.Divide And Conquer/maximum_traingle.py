"""
Maximum triangle

We are asked to find, in a sequence S of n numbers indexed by i=0..n-1,
the triplet tmax of consecutive numbers (if, if+1, if+2) where if+1 is greater than
both if and if+2 and whose sum, if + if+1+ if+2, is maximum.

Example :
    - Input -
    S = [4, 5, 4, 6, 7, 7, 6, 8, 3, 6, 8, 5, 4, 5]

    - Output-
    (19, 9, 11)
    19 = S[9] + S[10] + S[11] = 6 + 8 + 5

"""


def pequeno(p, q):
    return q - p < 2  # menos de 3 elementos → imposible formar triángulo


def solucion_directa(s, p, q):
    if p <= 0 or q >= len(s) - 1:
        return 0, None, None

    if s[p - 1] < s[p] > s[p + 1]:
        return s[p - 1] + s[p] + s[p + 1], p - 1, p + 1

    return 0, None, None


def dividir(p, q):
    return (p + q) // 2


def combinar(s, sol_izq, sol_der, p, m, q):
    c_izq, pi, qi = sol_izq
    c_der, pd, qd = sol_der

    # Triángulo cruzando el medio (solo hay UNO posible)
    c_med, pm, qm = 0, None, None

    if p < m < q:
        if s[m - 1] < s[m] > s[m + 1]:
            c_med = s[m - 1] + s[m] + s[m + 1]
            pm, qm = m - 1, m + 1

    # Elegimos el máximo
    if c_izq >= c_der and c_izq >= c_med:
        return sol_izq
    elif c_der >= c_izq and c_der >= c_med:
        return sol_der
    else:
        return c_med, pm, qm


def divideyvenceras_triangulo_max(s, p, q):
    if pequeno(p, q):
        return 0, None, None

    if p == q:
        return solucion_directa(s, p, q)

    m = dividir(p, q)

    sol_izq = divideyvenceras_triangulo_max(s, p, m)
    sol_der = divideyvenceras_triangulo_max(s, m + 1, q)

    return combinar(s, sol_izq, sol_der, p, m, q)


if __name__ == "__main__":
    S = [4, 5, 4, 6, 7, 7, 6, 8, 3, 6, 8, 5, 4, 5]

    inicio = 0
    fin = len(S) - 1
    print(S)
    print(divideyvenceras_triangulo_max(S, inicio, fin))
