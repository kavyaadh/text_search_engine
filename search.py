import frequency


def search(sword):
    words1 = frequency.find_freq("f1_clean.txt")
    words2 = frequency.find_freq("f2_clean.txt")
    f1 = False
    f2 = False

    if sword in words1:
        f1 = True

    if sword in words2:
        f2 = True

    freq1 = words1.get(sword, 0)
    freq2 = words2.get(sword, 0)

    return f1, freq1, f2, freq2
