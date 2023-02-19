# -*- coding: utf-8 -*-
"""pliki_tekstowe_zapis_do_nowego_pliku_w_postaci_kodu_HTML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFaNcsfdQDFI24QYK6gIT9TeZtcRzUg2

Napisać funkcję, której zadaniem jest odczytanie danych tabelarycznych z pliku
tekstowego, a następnie zapisanie ich do nowego pliku w postaci kodu HTML.

Przykład:

Wejście:

"Waga" "Wzrost" "BMI" "Nadwaga"

70 1,8 21,6 "NIE"

67 1,77 21,39 "NIE"

85 1,7 29,41 "TAK"

100 1,92 27,13 "TAK"

Wynik:

<html><body>

<table>

<tr><td>"Waga"</td><td>"Wzrost"</td><td>"BMI"</td><td>"Nadwaga"

</td></tr>

<tr><td>70</td><td>1,8</td><td>21,6</td><td>"NIE"

</td></tr>

<tr><td>67</td><td>1,77</td><td>21,39</td><td>"NIE"

</td></tr>

<tr><td>85</td><td>1,7</td><td>29,41</td><td>"TAK"

</td></tr>

<tr><td>100</td><td>1,92</td><td>27,13</td><td>"TAK"</td></tr>

</table>

</body></html>
"""

def record_text_to_HTML(fileText):

    lines = open(fileText).readlines()

    new_file_with_code_HTML = open("nowy_plik_HTML.txt", "w")

    new_file_with_code_HTML.write(str("<html><body>\n<table>\n"))

    for line in lines:
        line = line.split()
        new_file_with_code_HTML.write(str(f"<tr><td>{line[0]}</td><td>{line[1]}</td><td>{line[2]}</td><td>{line[3]}</td></tr>\n"))
    new_file_with_code_HTML.write(str("</table>\n</body></html>\n"))


record_text_to_HTML("pracownicy.txt")