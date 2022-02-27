# zad 1. Ile jest domen które mają '.pl' (nie ważne czy mają '.edu.pl')
def policz_flagi_pl(domeny_pl: list) -> int:
    return sum([1 if flaga[-3:] == '.pl' else 0 for flaga in domeny_pl])
