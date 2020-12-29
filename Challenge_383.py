# Challenge #383 - "Same Necklace"
#
# Imagine a necklace with lettered beads that can slide along the string. 
# For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.
# Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, 
# attach them to the end in their original ordering, and get the other string. 
# Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.
#
# Write a function that returns whether two strings describe the same necklace.



def same_necklace(base_word, alt_word):
    for i in range(0, len(base_word)):
        if base_word == alt_word:
            return True
        else:
            base_word = base_word[1:]+base_word[0]
        
    return False
    
    
print(same_necklace("nicole", "icolen"))
print(same_necklace("nicole", "lenico"))
print(same_necklace("nicole", "coneli"))
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
print(same_necklace("abc", "cba"))
print(same_necklace("xxyyy", "xxxyy"))
