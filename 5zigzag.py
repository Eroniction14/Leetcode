class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s)==numRows or numRows==1 :
            return s
        
        res=[''] * numRows
        curr=0
        step=1

        for i in s:
            res[curr]=res[curr]+i

            if curr==0:
                step=1
            elif curr==numRows-1:
                step=-1
            

            curr= curr+step
        

        return ''.join(res)

        