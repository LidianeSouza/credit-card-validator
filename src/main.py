def validar_bandeira(numero: str) -> str:
    numero = numero.replace(' ', '').replace('-', '')
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

# Exemplo de uso:
if __name__ == "__main__":
    print(get_card_brand("4111 1111 1111 1111"))  # Visa
    print(get_card_brand("5500 0000 0000 0004"))  # MasterCard
    print(get_card_brand("6011 0000 0000 0004"))  # Discover