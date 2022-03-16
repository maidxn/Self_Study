def FlippingBits(decimalString):
    decimal = int(decimalString)
    binary = bin(decimal)
    binary = binary.replace('0b', '')
    add = "0" * (32 - len(binary))
    binaryString = add + binary
    exponent = 31
    res = 0
    for bit in binaryString:
        res = res + pow(2, exponent) if bit == '0' else res
        exponent -= 1
    return res


numberOfQueries = int(input())

for each in range(numberOfQueries):
    query = input()
    print(FlippingBits(query))



