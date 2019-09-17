

def count_letters(s):

    unique = set(s)
    result = ''
    for letter in unique:
        if s.count(letter) > 1:
            result += letter
    return result

#assert sorted(count_letters('rtoplkghrtlkrtsazcvbcxwqx')) == ['c', 'k', 'l', 'r', 't', 'x']


s = input()

print(count_letters(s))


