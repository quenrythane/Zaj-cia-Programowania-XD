# zad 4. Jaka jest najdłuższa i najkrótsza domena w liście flag
def najdluzsza_najkrotsza_domena(domeny: list) -> tuple:
    sort_domains = sorted(domeny, key=len)
    shortest = [flaga for flaga in sort_domains if len(flaga) == len(sort_domains[0])]
    longest = [flaga for flaga in sort_domains[::-1] if len(flaga) == len(sort_domains[::-1][0])]
    # return sort_domains[0], sort_domains[-1]  <- zwraca 1 najdłuższą i 1 najkrótszą
    return shortest, longest  # zwraca wszystkie najkrótsze jeśli jest więcej niż 1 i tak samo z najdłuższą
