def validar_bandeira(numero: str) -> str:
    numero = numero.replace(' ', '').replace('-', '')
    
    if not numero.isdigit():
        return 'Inválido'

    tamanho = len(numero)

    if numero.startswith('4') and tamanho in [13, 16]:
        return 'Visa'
    if (51 <= int(numero[:2]) <= 55 or 2221 <= int(numero[:4]) <= 2720) and tamanho == 16:
        return 'MasterCard'
    if numero[:2] in ['34', '37'] and tamanho == 15:
        return 'American Express'
    if (300 <= int(numero[:3]) <= 305 or numero.startswith(('36', '38', '39'))) and tamanho == 14:
        return 'Diners Club'
    if (numero.startswith('6011') or numero.startswith('65') or 644 <= int(numero[:3]) <= 649) and tamanho == 16:
        return 'Discover'
    if numero[:4] in ['2014', '2149'] and tamanho == 15:
        return 'enRoute'
    if 3528 <= int(numero[:4]) <= 3589 and tamanho == 16:
        return 'JCB'
    if numero.startswith('8699') and tamanho == 15:
        return 'Voyager'
    if (numero.startswith('384100') or numero.startswith('60') or numero.startswith('637095')) and 13 <= tamanho <= 19:
        return 'Hipercard'
    if numero.startswith('50') and tamanho == 16:
        return 'Aura'
    return 'Desconhecida'

testes = [
    ("Teste 1", "5229 8369 1850 9028"),  # Visa
    ("Teste 2", "4916 1525 7993 1605"),  # MasterCard
    ("Teste 3", "3737 129403 48047"),  # Discover
    ("Teste 4", "3029 477398 1132"),   # American Express
    ("Teste 5", "6011 4182 2960 3954"),  # Diners Club
    ("Teste 6", "2149 6062622 1615"),  # Discover
    ("Teste 7", "3560 8160 3647 7235"),  # JCB
    ("Teste 8", "86993 6611 94606 7"),  # Voyager
    ("Teste 9", "6062 8284 0333 5603"),  # Hipercard
    ("Teste 10", "5028 2532 0555 2690"), # Aura

    ("Teste 11", "5362 7447 7297 9401"), # Visa
    ("Teste 12", "4916 9961 8731 2495"), # MasterCard
    ("Teste 13", "3785 713463 91356"), # Discover
    ("Teste 14", "3028 448407 3980"), # American Express
    ("Teste 15", "6011 3363 3617 9645"), # Diners Club
    ("Teste 16", "2149 5306202 0641"), # JCB
    ("Teste 17", "3538 9495 8372 2882"), # Voyager
    ("Teste 18", "86990 3970 24040 9"), # Hipercard
    ("Teste 19", "6062 8206 8711 3848"), # Aura
    ("Teste 20", "5005 6328 8584 1050"), # Correção: faltava vírgula

    ("Teste 21", "5520 6906 2517 9385"), # Visa
    ("Teste 22", "4929 3710 8624 9336"), # MasterCard
    ("Teste 23", "3771 846678 52682"), # Discover
    ("Teste 24", "3004 312029 5039"), # American Express
    ("Teste 25", "6011 8658 5136 3564"), # Diners Club
    ("Teste 26", "2014 4120168 9323"), # JCB
    ("Teste 27", "3582 7925 6848 4325"), # Voyager
    ("Teste 28", "86998 0637 53421 8"), # Hipercard
    ("Teste 29", "6062 8276 5308 8490"), # Aura
    ("Teste 30", "5098 7124 1042 0840"), # Visa         
]

resultados = []
for nome, numero in testes:
    resultado = f"{nome}: {validar_bandeira(numero)}"
    print(resultado)
    resultados.append(resultado)

with open("results/test_results.txt", "w", encoding="utf-8") as f:
    for linha in resultados:
        f.write(linha + "\n")