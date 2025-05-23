def get_card_brand(card_number: str) -> str:
    card_number = card_number.replace(' ', '').replace('-', '')

    def starts_with(prefixes):
        return any(card_number.startswith(str(p)) for p in prefixes)

    def in_range(start, end, digits=None):
        prefix = int(card_number[:len(str(start))])
        return start <= prefix <= end and (digits is None or len(card_number) == digits)

    length = len(card_number)

    if card_number.startswith('4') and length in [13, 16]:
        return 'Visa'
    if (in_range(51, 55, 16) or in_range(2221, 2720, 16)):
        return 'MasterCard'
    if (starts_with(['34', '37']) and length == 15):
        return 'American Express'
    if ((in_range(300, 305, 14) or starts_with(['36', '38', '39'])) and length == 14):
        return 'Diners Club'
    if ((card_number.startswith('6011') or card_number.startswith('65') or in_range(644, 649)) and length == 16):
        return 'Discover'
    if (starts_with(['2014', '2149']) and length == 15):
        return 'enRoute'
    if (in_range(3528, 3589, 16)):
        return 'JCB'
    if (card_number.startswith('8699') and length == 15):
        return 'Voyager'
    if ((card_number.startswith('384100') or card_number.startswith('60') or card_number.startswith('637095')) and 13 <= length <= 19):
        return 'Hipercard'
    if (card_number.startswith('50') and length == 16):
        return 'Aura'
    return 'Desconhecida'


tests = [
    ("Test 1", "5229 8369 1850 9028"),  # Visa
    ("Test 2", "4916 1525 7993 1605"),  # MasterCard
    ("Test 3", "3737 129403 48047"),  # Discover
    ("Test 4", "3029 477398 1132"),   # American Express
    ("Test 5", "6011 4182 2960 3954"),  # Diners Club
    ("Test 6", "2149 6062622 1615"),  # Discover
    ("Test 7", "3560 8160 3647 7235"),  # JCB
    ("Test 8", "86993 6611 94606 7"),  # Voyager
    ("Test 9", "6062 8284 0333 5603"),  # Hipercard
    ("Test 10", "5028 2532 0555 2690"), # Aura

    ("Test 11", "5362 7447 7297 9401"), # Visa
    ("Test 12", "4916 9961 8731 2495"), # MasterCard
    ("Test 13", "3785 713463 91356"), # Discover
    ("Test 14", "3028 448407 3980"), # American Express
    ("Test 15", "6011 3363 3617 9645"), # Diners Club
    ("Test 16", "2149 5306202 0641"), # JCB
    ("Test 17", "3538 9495 8372 2882"), # Voyager
    ("Test 18", "86990 3970 24040 9"), # Hipercard
    ("Test 19", "6062 8206 8711 3848"), # Aura
    ("Test 20", "5005 6328 8584 1050"), # Correção: faltava vírgula

    ("Test 21", "5520 6906 2517 9385"), # Visa
    ("Test 22", "4929 3710 8624 9336"), # MasterCard
    ("Test 23", "3771 846678 52682"), # Discover
    ("Test 24", "3004 312029 5039"), # American Express
    ("Test 25", "6011 8658 5136 3564"), # Diners Club
    ("Test 26", "2014 4120168 9323"), # JCB
    ("Test 27", "3582 7925 6848 4325"), # Voyager
    ("Test 28", "86998 0637 53421 8"), # Hipercard
    ("Test 29", "6062 8276 5308 8490"), # Aura
    ("Test 30", "5098 7124 1042 0840"), # Visa         
]

resultados = []
for nome, numero in tests:
    resultado = f"{nome}: {get_card_brand(numero)}"
    print(resultado)
    resultados.append(resultado)

with open("results/test_results.txt", "w", encoding="utf-8") as f:
    for linha in resultados:
        f.write(linha + "\n")
