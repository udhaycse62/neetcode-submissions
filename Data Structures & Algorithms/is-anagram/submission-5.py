class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        S_map, T_map= {}, {}

        for ele in s:
            S_map[ele] = 1 + S_map.get(ele,0)
        for ala in t:
            T_map[ala] = 1 + T_map.get(ala,0)
        
        return S_map == T_map


        


