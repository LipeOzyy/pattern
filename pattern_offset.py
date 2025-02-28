import sys
import string

def cyclic_pattern(length):
    charset = string.printable
    pattern = (charset * (length // len(charset) + 1))[:length]
    return pattern.encode()  

def find_offset(value, pattern_length=8192):
    pattern = cyclic_pattern(pattern_length)
    
    try:
        value_bytes = bytes.fromhex(value)
    except ValueError:
        print("Valor não é um hexadecimal válido.")
        sys.exit(1)
    
    try:
        offset = pattern.index(value_bytes)
        return offset
    except ValueError:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pattern_offset.py <valor em hexadecimal>")
        sys.exit(1)

    value = sys.argv[1]
    
    if not all(c in string.hexdigits for c in value):
        print("O valor precisa ser um número hexadecimal.")
        sys.exit(1)
    
    offset = find_offset(value)

    if offset is not None:
        print(f"Offset encontrado: {offset}")
    else:
        print("Valor não encontrado no padrão.")
