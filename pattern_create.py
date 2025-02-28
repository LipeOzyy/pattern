import itertools

def cria_padrao(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    pattern = []
    combinations = itertools.permutations(chars, 3) 

    for combo in combinations:
        if len(pattern) + 3 > length:
            break
        pattern.append("".join(combo))

    return "".join(pattern)[:length]


pattern_length = 600
pattern = cria_padrao(pattern_length)
print(pattern)