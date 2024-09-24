def partitioningString(s: str) -> int:
    dic = {}
    count = 1
    for char in s:
        if char in dic:
            count += 1
            dic = {}
        dic[char] = 1

    return count

s = "ssssss"

print(partitioningString(s))