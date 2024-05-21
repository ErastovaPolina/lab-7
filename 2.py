def is_palindrome(data):
    return data == data[::-1]


if is_palindrome(input()):
    print("YES")
else:
    print("NO")
