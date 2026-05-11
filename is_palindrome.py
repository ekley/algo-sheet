def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum(): # if s='......,/.' left keeps moving to the right and eventually gets out of bound, that is why we do nested check left < right
            left += 1

        while left < right and not s[right].isalnum(): # if s='......,/.' right keeps moving to the left and eventually gets out of bound, that is why we do nested check left < right
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

is_it = is_palindrome('a.o.a')
print(is_it)