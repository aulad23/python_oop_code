def balanced_string(Str):
    result = []
    count_L = 0
    count_R = 0
    sub_string = ""
    for char in Str:
        if char == 'L':
            count_L += 1
        else:
            count_R += 1
        sub_string += char
        if count_L == count_R:
            result.append(sub_string)
            sub_string = ""
    return result

S = input().strip()
result = balanced_string(S)
print(len(result))
for sub_string in result:
    print(sub_string)
