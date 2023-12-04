def countCharacters( words, chars) -> int:
        def isAnagram(s: str, t: str) -> bool:
            sl = len(s)
            counter=[0]*26
            for i in range(len(t)):
                if i<sl:
                   # print(s[i])
                    counter[ord(s[i])-ord('a')]+=1
                counter[ord(t[i])-ord('a')]-=1
            for i in counter:
                if not (i==0 or i<= -1):
                    return False
            return True 

        sums = 0
        for i in words:
            if(isAnagram(i,chars)):
                print("here")    
                sums+=len(i)
        return sums 

print(countCharacters(["hello","world","leetcode"],"welldonehoneyr"))