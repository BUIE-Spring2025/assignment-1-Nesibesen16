def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    strg = ""
    a = 1000
    while num > 0 and a != 0:
        i = num // a
        if num >= 1000:
            strg += "M"*i
        elif 1000 > num >= 100 and i < 4:
            strg += "C"*i
        elif 1000 > num >= 100 and i == 4:
            strg += "CD"
        elif 1000 > num >= 100 and 9 > i >= 5:
            strg += "D" + "C"*(i-5)
        elif 1000 > num >= 100 and i == 9:
            strg += "CM"
        elif 100 > num >= 10 and i < 4:
            strg += "X"*i
        elif 100 > num >= 10 and i == 4:
            strg += "XL"
        elif 100 > num >= 10 and 9 > i >= 5:
            strg += "L" + "X"*(i-5)
        elif 100 > num >= 10 and i == 9:
            strg += "XC"
        elif 10 > num >= 0 and num < 4:
            strg += "I"*num
            break
        elif 10 > num >= 0 and num == 4:
            strg += "IV"
            break
        elif 10 > num >= 0 and 9 > num >= 5:
            strg += "V" + "I"*(num-5)
            break
        elif 10 > num >= 0 and num == 9:
            strg += "IX"
            break
        num = num - (i*a)
        a = a // 10
    return strg
