def is_palindrome(s):
    r = s[::-1]
    if s == r:
        return True
    else:
        return False
