
def count_palindrome(n):
    sum_p = 0
    for i in range(1, n+1):
        s = str(i)
        pal = True
        for w in range((len(s)+1)//2):
            if s[w] != s[-w-1]:
                pal = False
                break
        if pal:
            sum_p += 1
    return sum_p

# assert count_palindrome(1) == 1
# assert count_palindrome(7) == 7
# assert count_palindrome(50) == 13
# assert count_palindrome(170) == 25
# assert count_palindrome(3553) == 134
# assert count_palindrome(35753) == 456

s = input()

print(count_palindrome(int(s)))
