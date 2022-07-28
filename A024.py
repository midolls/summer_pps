class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        check = True
        if bills[0]>5:
            check =False
        else:
            for i in bills:
                if i == 5:
                    cnt1 +=1
                elif i ==10:
                    if cnt1 >= 1:
                        cnt2+=1
                        cnt1-=1
                    else:
                        check = False
                elif i ==20:
                    cnt3+=1
                    if cnt2>=1 and cnt1>=1:
                        cnt2-=1
                        cnt1-=1
                    elif cnt2 >=1 and cnt1 ==0:
                        check =False
                    elif cnt2 ==0 and cnt1 >=3 :
                        cnt1-=3
                    elif cnt2 ==0 and cnt1 <3 :
                        check =False

        return check