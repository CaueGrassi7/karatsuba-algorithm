import math

def karatsuba(u, v, n=None):
    # Se o número de dígitos (n) não for fornecido, calcula-o a partir dos números u e v.
    if n is None:
        n = max(len(str(u)), len(str(v)))

    # Caso base: se n ≤ 3, usa multiplicação direta.
    if n <= 3:
        return u * v

    # Linha 3: Calcula m = ⌈n/2⌉
    m = math.ceil(n / 2)

    # Divide u e v em partes altas e baixas
    p = u // (10 ** m)  # Parte alta de u
    q = u % (10 ** m)  # Parte baixa de u
    r = v // (10 ** m)  # Parte alta de v
    s = v % (10 ** m)  # Parte baixa de v

    # Chamadas recursivas para as multiplicações das partes
    pr = karatsuba(p, r, m)
    qs = karatsuba(q, s, m)

    # Chamada recursiva para calcular (p + q) * (r + s)
    y = karatsuba(p + q, r + s, m + 1)

    # Combinação dos resultados
    return pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs


# Exemplo de uso:
if __name__ == "__main__":
    # Testa o algoritmo com dois números grandes
    u = 12345678
    v = 87654321
    resultado = karatsuba(u, v)
    print("Resultado:", resultado)
    print("Resultado esperado:", u * v)