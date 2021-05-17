def is_palindrome(str):
    return str == str[::-1]

str = "abccba"
print(is_palindrome(str))