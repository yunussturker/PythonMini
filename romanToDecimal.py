# Convert to Decimal
romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def RomanNumToDecimal(romanNum):
    sum = 0
    for i in range(len(romanNum) - 1):
        left = romanNum[i]
        right = romanNum[i+1]
        if romans[left] < romans[right]:
            sum -= romans[left]
        else:
            sum += romans[left]
    sum += romans[romanNum[-1]]
    return sum



