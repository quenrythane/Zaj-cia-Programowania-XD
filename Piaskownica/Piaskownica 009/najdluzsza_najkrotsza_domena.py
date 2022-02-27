# zad 4. Jaka jest najdłuższa i najkrótsza domena w liście flag
def najdluzsza_najkrotsza_domena(domeny: list) -> str:
    sorted_by_len_asc = sorted(domeny, key=lambda x: len(x))[1:]
    sorted_by_len_desc = sorted(domeny, key=lambda x: len(x), reverse=True)
    shortest = [flaga for flaga in sorted_by_len_asc if len(flaga) == len(sorted_by_len_asc[0])]
    longest = [flaga for flaga in sorted_by_len_desc if len(flaga) == len(sorted_by_len_desc[0])]
    return f'najkrótsze({len(shortest[0])} znaków): {shortest}\n' \
           f'najdłuższe({len(longest[0])} znaków): {longest}'
