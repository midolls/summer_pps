#A055

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        check = 0
        for s in S:
            if s == "(" :
                check += 1
                if check > 1 :  # checking if it starts new paren or already added to "res" list
                    res.append(s)


            if s == ")":
                check -= 1
                if check >= 1:
                    res.append(s)

        return "".join(res)