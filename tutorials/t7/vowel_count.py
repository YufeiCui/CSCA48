# Provided by Dr. Marzieh Ahmadzadeh & Nick Cheng. Edited by Yufei Cui


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def has_more_vowel(a_string, c_count, v_count):
    '''(str, int, int) -> int
    This recursive function determines if a given string has more vowels
    than consonants.
    c_count represent the number of consonant in a_string
    v_count represent the number of vowels in a_string'''
    if len(a_string) == 0:
        return v_count > c_count
    if a_string[0] in vowels:
        v_count += 1
    else:
        c_count += 1
    return has_more_vowel(a_string[1:], c_count, v_count)


def vowel_count(a_string, v_count):
    '''(str, str) -> int
    This recursive function returns the number of vowels in a_string.
    v_count represent the number of vowels in a_string'''
    if len(a_string) == 0:
        return v_count
    if a_string[0] in vowels:
        v_count += 1
    return vowel_count(a_string[1:], v_count)


# The way we did it in lecture, not requring the 2nd parameter

# def vowel_count(a_string):
#     '''(str, str) -> int
#     This recursive function returns the number of vowels in a_string.
#     v_count represent the number of vowels in a_string'''
#     if len(a_string) == 0:
#         return v_count
#     if a_string[0] in vowels:
#         return 1 + vowel_count(a_string[1:])
#     else:
#         return vowel_count(a_string[1:])

def letter_count(a_string, c_count, v_count):
    '''(str, int, int) -> int This recursive function returns the number of
    consonant and vowels in a_string. c_count represent the number of
    consonant in a_string v_count represent the number of vowels in a_string '''
    if len(a_string) == 0:
        return c_count, v_count
    if a_string[0] in vowels:
        v_count += 1
    else:
        c_count += 1
    return letter_count(a_string[1:], c_count, v_count)


print(has_more_vowel("TrAin", 0, 0))
print(has_more_vowel("Trainee", 0, 0))
print(vowel_count("Train", 0))
print(vowel_count("TrainEe", 0))
print(letter_count("Train", 0, 0))
print(letter_count("Trainee", 0, 0))
