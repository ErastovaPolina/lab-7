def is_palindrome(data):
    pass


def test_is_palindrome():
    data = ["dad", "level", "hello", "madam", "12321"]
    results = [True, True, False, True, True]

    for i in range(len(data)):
        if is_palindrome(data[i]) != results[i]:
            print("NO")
            return
    print("YES")


test_is_palindrome()
