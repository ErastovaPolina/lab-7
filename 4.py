def is_correct_mobile_phone_number_ru(number):
    cleaned_number = "".join(filter(str.isdigit, number))

    if len(cleaned_number) != 11:
        return False

    if cleaned_number[0] == '8' or cleaned_number[:2] == '79':
        return True
    else:
        return False
