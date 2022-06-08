def count_vowels(self, s):
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
    return count