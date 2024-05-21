def is_correct_mobile_phone_number_ru(number):
    pass


cases = ["+7(900)1234567", "54457", "89001234567", "12345678901"]
results = [True, False, True, False]

all_passed = True
for case, result in zip(cases, results):
    if is_correct_mobile_phone_number_ru(case) != result:
        all_passed = False

if all_passed:
    print("YES")
else:
    print("NO")
