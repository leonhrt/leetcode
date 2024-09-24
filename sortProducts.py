def sortProducts(order: str, productCodes):
    alphabet = {}
    dictProductCodes = {}
    count = 0

    for char in order:
        alphabet[char] = count
        count += 1

    for string in productCodes:
        addition = 0
        for char in string:
            addition += alphabet[char]
        dictProductCodes[string] = addition

    return sorted(dictProductCodes, key=dictProductCodes.get)

def test_case_1():
    order = "abcdefghijklmnopqrstuvwxyz"
    productCodes = ["adc", "abc"]
    expected = ["abc", "adc"]
    result = sortProducts(order, productCodes)
    assert result == expected, f"Expected {expected}, but got {result}"

test_case_1()

def test_case_2():
    order = "zyxwvutsrqponmlkjihgfedcba"
    productCodes = ["adc", "abc"]
    expected = ["adc", "abc"]
    result = sortProducts(order, productCodes)
    assert result == expected, f"Expected {expected}, but got {result}"

test_case_2()

def test_case_3():
    order = "abcdefghijklmnopqrstuvwxyz"
    productCodes = ["abc", "dbc", "bbc"]
    expected = ["abc", "bbc", "dbc"]
    result = sortProducts(order, productCodes)
    assert result == expected, f"Expected {expected}, but got {result}"

test_case_3()

def test_case_4():
    order = "abcdefghijklmnopqrstuvwxyz"
    productCodes = ["abc", ""]
    expected = ["", "abc"]
    result = sortProducts(order, productCodes)
    assert result == expected, f"Expected {expected}, but got {result}"

test_case_4()

def test_case_5():
    order = "abcdefghijklmnopqrstuvwxyz"
    productCodes = []
    expected = []
    result = sortProducts(order, productCodes)
    assert result == expected, f"Expected {expected}, but got {result}"

test_case_5()

def test_case_6():
    order = "abc"
    productCodes = ["adc", "abc"]
    try:
        result = sortProducts(order, productCodes)
        assert False, "Expected a KeyError but did not get one"
    except KeyError:
        pass

test_case_6()