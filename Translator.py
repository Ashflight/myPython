# The vowel code is a code language that replaces all vowels with a consonant, tyically in a way to make it look like the test no longer makes sense.
# In this translator, I will make the replacement consonant "g".
# For example, it will turn "cat" into "cgt".
'''Side Note, 3 single quotation marks can also make comments, like this.'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase to translate: ")))