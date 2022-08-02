#A037
#범위 내 수들 중 각 자릿수로 나눠떨어지는 숫자의 개수를 반환

def selfDividingNumbers(left, right):

    def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True

    out = []
    for n in range(left, right + 1):
        if self_dividing(n):
            out.append(n)

    return out