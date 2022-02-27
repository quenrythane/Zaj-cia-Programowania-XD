import requests
import policz_flagi_pl, policz_flagi_samo_com, policz_literki_a, najdluzsza_najkrotsza_domena

# surowy tekst
link = "https://zajecia-programowania-xd.pl/flagi"
flagi_raw = requests.get(link).text[1683:]
counter_zawislo = flagi_raw[15:19]  # 803 tyle ile policzył łukasz

# flagi stringi
flagi = flagi_raw[:17129]  # to co na stronie jest od Flagi: do Flagi oczekujące na rejestrację:
flagi_oczekujace = flagi_raw[17264:]  # to co na stronie jest od Flagi oczekujące na rejestrację:
wszystkie_flagi = flagi + flagi_oczekujace

# flagi zamienione na listy
flagi_lista = [flaga[5:] for flaga in flagi.split('</p>')][:-1]
flagi_oczekujace_lista = [flaga[3:] for flaga in flagi_oczekujace.split('</p>')][:-1]
wszystkie_flagi_lista = flagi_lista + flagi_oczekujace_lista

# wykonanie
print('ilość flag.pl:', policz_flagi_pl.policz_flagi_pl(wszystkie_flagi_lista))
print('ilość flag.com:', policz_flagi_samo_com.policz_flagi_samo_com(wszystkie_flagi_lista))
print('ilość liter a w nazwach flag:', policz_literki_a.policz_literki_a(wszystkie_flagi_lista))
print('najkrótsze domeny:', najdluzsza_najkrotsza_domena.najdluzsza_najkrotsza_domena(wszystkie_flagi_lista)[0])
print('najdłuższe domeny:', najdluzsza_najkrotsza_domena.najdluzsza_najkrotsza_domena(wszystkie_flagi_lista)[1])




