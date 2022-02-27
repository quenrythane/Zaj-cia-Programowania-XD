# zad 2. Ile jest domen które mają samo '.com
def policz_flagi_samo_com(domeny_com: list) -> int:
    return sum([1 if flaga[-4:] == '.com' else 0 for flaga in domeny_com])
