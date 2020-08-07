def romanToInt(s):
    dict = {}
    dict["I"] = 1
    dict["V"] = 5
    dict["X"] = 10
    dict["L"] = 50
    dict["C"] = 100
    dict["D"] = 500
    dict["M"] = 1000

    decimal = 0

    for val in s:
        decimal += dict[val]

    if "IV" in s or "IX" in s:
        decimal -= 2
    if "XL" in s or "XC" in s:
        decimal -= 20
    if "CM" in s or "CD" in s:
        decimal -= 200

    return decimal
