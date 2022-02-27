# zad 3. Ile jest literek 'a' we wszstkich domenach razem.
def policz_literki_a(domeny: list) -> int:
    return ''.join(domeny).count('a')
