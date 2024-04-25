class Solution(object):
    def isValid(s:str)->bool:
        leftsymbols=[]
        for c in s:
            if c in['(','{' ,'[']:
                lesftsymbols.append(c)
            elif c==')' and len(leftsymbols)!=0 and leftsymbols[-1]=='(':
                leftsymbols.pop()
            elif c=='}' and len(leftsymbols)!=0 and leftsymbols[-1]=='{':
                leftsymbols.pop()
            elif c==']' and len(leftsymbols)!=0 and leftsymbols[-1]=='[':
                leftleftsymbols.pop()
            else:
                return False
            return leftsymbols==[]

              
    



  

