def get_card_brand(card_number: str) -> str:
    card_number = card_number.replace(' ', '').replace('-', '')

    def starts_with(prefixes):
        return any(card_number.startswith(str(p)) for p in prefixes)

    def in_range(start, end, length=None):
        prefix = int(card_number[:len(str(start))])
        return start <= prefix <= end and (length is None or len(card_number) == length)

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

if __name__ == "__main__":
    print(get_card_brand("5120 9773 9076 0075"))  # MasterCard
    print(get_card_brand("4532 8407 7823 2445"))  # Discover    
    print(get_card_brand("3425 503587 54886"))  # Visa          
    print(get_card_brand("3006 779398 6202"))  # Discover
    print(get_card_brand("6011 9047 4079 6930"))  # Discover
    print(get_card_brand("2014 1336798 4939"))  # Discover
    print(get_card_brand("3537 3592 4052 1944"))  # Discover
    print(get_card_brand("86992 3288 25361 3"))  # Discover
    print(get_card_brand("6062 8252 2044 6027"))  # Discover  
    print(get_card_brand("5079 9286 9123 1226"))  # Discover  