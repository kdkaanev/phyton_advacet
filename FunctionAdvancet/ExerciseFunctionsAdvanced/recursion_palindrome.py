def palindrome(word, indx):
    if indx >= len(word) // 2:
        return f"{word} is a palindrome"
    left_chr = word[indx]
    right_chr = word[-1 - indx]
    if left_chr != right_chr:
        return f"{word} is not a palindrome"
    return palindrome(word, indx + 1)


print(palindrome("abcba", 0))