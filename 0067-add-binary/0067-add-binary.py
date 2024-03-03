class Solution:
    def addBinary(self, a: str, b: str) -> str:
        indexA, indexB = len(a) - 1, len(b) - 1
        iterA, iterB = True, True
        res = ""
        add = False
        while indexA > -1 or indexB > -1 or add:
            num = "0"
            valueA = a[indexA] if indexA > -1 else "0"
            valueB = b[indexB] if indexB > -1 else "0"

            if valueA != valueB:
                if add:
                    num = "0"
                    add = True
                else:
                    num = "1"
                    add = False
            else:
                if valueA == "1":
                    if add: 
                        num = "1"
                    else:
                        num = "0"
                    add = True
                else:
                    if add:
                        num = "1"
                    add = False
            indexA -= 1
            indexB -= 1
            res = num + res
        return res
                        
                        
                
      