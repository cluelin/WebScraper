import re

p = re.compile("ca.e") 
# . : 하나의 문자를 의미한다. 
# ^ (^de) : 문자열의 시작.  > desk, destination 이렇게 되는거지. 
# $ (se$) : 문자열의 끝. > case , base


def print_match(m):
    if m:
        print("m.group() : " , m.group()) #일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열 반환
    else:
        print("매치되지않음")

m = p.match("case") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

m = p.search("careless") #search : 주어진 문자열중에 일치하는게 있는지 확인. 
print_match(m)


