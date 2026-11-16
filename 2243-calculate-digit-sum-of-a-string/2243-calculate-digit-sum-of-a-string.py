class Solution:
    def digitSum(self, s: str, k: int) -> str:
        Strlist = list(s)
        while(len(Strlist)>k):
            newstr = ""
            for i in range(0,len(Strlist),k):
                group = Strlist[i:i+k]
                groupsum  = sum(int(dights) for dights in group)

                newstr += str(groupsum)

            Strlist = list(newstr)

        return "".join(Strlist)


