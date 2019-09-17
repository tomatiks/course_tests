import time

low = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encript(s, decode=False):
    new_str = ''
    lw = longest_word(s)
    for letter in s:
        replaced_l = letter
        if letter.isalpha() and letter.isupper():
            index = up.index(letter)
            if decode:
                replaced_l = up[get_index(index, lw)]
            else:
                replaced_l = up[get_index(index, -lw)]
        elif letter.isalpha() and letter.islower():
            index = low.index(letter)
            if decode:
                replaced_l = low[get_index(index, lw)]
            else:
                replaced_l = low[get_index(index, -lw)]

        new_str += replaced_l
    return new_str



    
def get_index(i, l):
    index = i+l
    if index < 0:
        return -abs(index)%26
    elif index > 25:
        return index%26
    else:
        return index


def longest_word(s):
    lw = 0
    for word in s.split():
        w_len = 0
        for letter in word:
            if letter.isalpha() or letter == '-':
                w_len +=1
        if w_len > lw:
            lw = w_len
    return lw



s = input()
start = time.time()

#print(encript(s))
print(encript(s,True))

end = time.time()
ex_time = end - start
print(f'Execution time is : {ex_time}')