
def symbols_counter(text):
    counter = {'symbols': {}, 'amount': 0}

    for symbol in text:
        if symbol in counter.get('symbols'):
            counter['symbols'][symbol] += 1
            counter['amount'] += 1
        else:
            counter['symbols'][symbol] = 1
            counter['amount'] += 1

    return counter


def combination(init_counter):
    counter = {k: v for k, v in sorted(init_counter['symbols'].items(), key=lambda item: item[1])}

    tree = []

    for key in counter:
        tree.append({'amount': counter.get(key), 'symbol': key})

    while len(tree) > 1:
        elem1 = tree[0]
        elem2 = tree[1]
        tree.pop(0)
        tree.pop(0)

        if elem1.get('amount') > elem2.get('amount'):
            tree.append({'amount': elem1.get('amount') + elem2.get('amount'), 'elms': [elem2, elem1]})
        else:
            tree.append({'amount': elem1.get('amount') + elem2.get('amount'), 'elms': [elem1, elem2]})

        tree = sorted(tree, key=lambda d: d['amount'])

    return tree


def get_all_codes(tree, codes=None, way=""):
    if codes is None:
        codes = {}

    if 'symbol' in tree:
        codes[tree.get('symbol')] = way
    else:
        get_all_codes(tree.get('elms')[0], way=way + '0', codes=codes)
        get_all_codes(tree.get('elms')[1], way=way + '1', codes=codes)


def hash_text(text, codes):
    hashed_text = ""

    for symbol in text:
        hashed_text += codes.get(symbol)

    return hashed_text


def dict_find_key(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key


def unHash_text(hashed_text, codes):
    bits = ""
    text = ""

    for bit in hashed_text:
        bits += bit

        if bits in codes.values():
            text += dict_find_key(codes, bits)
            bits = ""

    return text



text = "Мы могли бы с той же простотой взять символ длиной в 16 бит (то есть, состоящий из двух печатных знаков), " \
       "равно как и 10 бит, 20 и так далее. Размер символа выбирается, исходя из строки ввода, которую мы ожидаем " \
       "встретить. Например, если бы я собрался кодировать сырые видеофайлы, я бы приравнял размер символа к размеру " \
       "пикселя. Помните, что при уменьшении или увеличении размера символа меняется и размер кода для каждого " \
       "символа, потому что чем больше размер, тем больше символов можно закодировать этим размером кода. Комбинаций " \
       "нулей и единичек, подходящих для восьми бит, меньше, чем для шестнадцати. Поэтому вы должны подобрать размер " \
       "символа, исходя из того по какому принципу данные повторяются в вашей последовательности. "


counter = symbols_counter(text)
tree = combination(symbols_counter(text))
codes = {}
get_all_codes(tree[0], codes=codes)
hashed_text = hash_text(text, codes)
text = unHash_text(hashed_text, codes)

print(counter, end='\n\n\n')
print(tree, end='\n\n\n')
print(codes, end='\n\n\n')
print(hashed_text, end='\n\n\n')
print(text, end='\n\n\n')





