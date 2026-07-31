class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=''
        for i in s:
            if i.isalnum():
                temp+=i
        if temp.lower()==temp[::-1].lower():
            return True
        else:
            return False            

                


        