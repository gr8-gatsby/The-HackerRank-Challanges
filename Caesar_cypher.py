def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    orig = list('abcdefghijklmnopqrstuvwxyz')
    modif = []
    for i in range(len(orig) - k):
        modif.append(orig[k + i])
    for i in range(k):
        modif.append(orig[i])

    crypted = ""
    for i in range(len(s)):
        if (s[i]).isalpha() and (s[i].islower()):
            crypted = crypted + modif[orig.index(s[i])]
            print(crypted)
        elif (s[i]).isalpha() and (s[i].isupper()):
            crypted = crypted + (modif[orig.index(s[i].lower())]).upper()
        else:
            crypted = crypted + s[i]

    return crypted

# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
#
# Example
#
# The alphabet is rotated by , matching the mapping above. The encrypted string is
#
# .
#
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
#
# Function Description
#
# Complete the caesarCipher function in the editor below.
#
# caesarCipher has the following parameter(s):
#
#     string s: cleartext
#     int k: the alphabet rotation factor
#
# Returns
#
#     string: the encrypted string
#
# Input Format
#
# The first line contains the integer,
# , the length of the unencrypted string.
# The second line contains the unencrypted string, .
# The third line contains
#
# , the number of letters to rotate the alphabet by.
#
# Constraints
#
#
#
# is a valid ASCII string without any spaces.
#
# Sample Input
#
# 11
# middle-Outz
# 2
#
# Sample Output
#
# okffng-Qwvb
#
# Explanation
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab
#
# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b
#
# Language
# Python 3
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# Line: 20 Col: 15
# Test against custom input
# Congratulations
# You solved this challenge. Would you like to challenge your friends?
# Compiler Message
#
# Success
#
# Input (stdin)
#
#     12
#
#     Hello_World!
#
#     4
#
# Expected Output
#
#     Lipps_Asvph!
#
# Hidden Test Case
#
# Use print or log statements to debug why your hidden test cases are failing. Hidden test cases are used to evaluate if your code can handle different scenarios, including corner cases.
#
#     Cont