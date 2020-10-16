def loselose(s):
    hash = 0
    for ch in s:
        hash = hash + ord(ch)
    return hash


def rs(s):
    hash = 0
    a = 63689
    b = 378551

    for ch in s:
        hash = hash * a + ord(ch)
        a = a*b
    return hash


def djb2(s):
    hash_seed = 5381
    hashCode = hash_seed
    hash_mask = 0x7FFFFFFF
    hash_multiplier = 33
    for ch in s:
        hashCode = hash_multiplier * hashCode + ord(ch)
    return hashCode & hash_mask


def sdbm(s):
    hash = 0
    for ch in s:
        hash = ord(ch) + (hash << 6) + (hash << 16) -hash
    return hash


def main():
    first = loselose('Unicode')
    print('Resultado LoseLose Hash: {}'.format(first))
    print(hex(first))
    second = rs('Unicode')
    print('Resultado RS Hash: {}'.format(second))
    print(hex(second))
    third = djb2('Unicode')
    print('Resultado DJB2 Hash: {}'.format(third))
    print(hex(third))
    fourth = sdbm('Unicode')
    print('Resultado SDBM Hash: {}'.format(fourth))
    print(hex(fourth))


if __name__ == '__main__':
    main()
