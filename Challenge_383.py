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