class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        output = []

        imp_dict = defaultdict(list)
        

        for i in strs:
            character_code = [0] * 26
            for v in i:
                character_code[ord(v) - ord('a')] += 1
            imp_dict[tuple(character_code)].append(i)

        for x in imp_dict.values():
            output.append(x)

        
        return output




            
        
