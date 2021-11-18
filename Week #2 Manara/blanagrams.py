""""
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
solution(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
solution(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
solution(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
solution(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string word1

A string consisting of lowercase letters.

Guaranteed constraints:
1 ≤ word1.length ≤ 100.

[input] string word2

A string consisting of lowercase letters.

Guaranteed constraints:
word2.length = word1.length.

[output] boolean

Return true if word1 and word2 are blanagrams of each other, otherwise return false.
"""


def solution(word1, word2):
    dict_word1 = {}

    for item in word1:
        if item in dict_word1:
            dict_word1[item] = dict_word1[item] + 1
        else:
            dict_word1[item] = 1

    number_of_diff = 0
    for item in word2:
        if item in dict_word1 and dict_word1[item] > 0:
            dict_word1[item] = dict_word1[item] - 1
        else:
            number_of_diff += 1

    print(number_of_diff)
    if number_of_diff == 0 or number_of_diff > 1:
        return False
    return True


