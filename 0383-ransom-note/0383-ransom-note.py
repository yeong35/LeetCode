class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = {}
        magazine_dict = {}

        for i in ransomNote:
            if i not in ransomNote_dict:
                ransomNote_dict[i] = 1
            else:
                ransomNote_dict[i] = 1 + ransomNote_dict[i]

        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else:
                magazine_dict[i] = 1 + magazine_dict[i]

        for key, value in ransomNote_dict.items():
            if key not in magazine or magazine_dict[key] < value:
                return False
        return True