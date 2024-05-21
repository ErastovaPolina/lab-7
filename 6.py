def punctuation_(data):
    punctuation = '.,!?;:()[]"'
    cleaned_data = ''.join([char for char in data if char not in punctuation])
    return cleaned_data


print(punctuation_(input()))
