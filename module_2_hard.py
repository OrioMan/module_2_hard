def get_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


print(get_password(9))
print(get_password(20))
