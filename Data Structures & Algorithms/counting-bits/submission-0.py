class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            i_bin=bin(i)
            result.append(i_bin.count("1"))
        return result    

        