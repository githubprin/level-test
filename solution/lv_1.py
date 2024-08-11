all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

# write your code here 

a = (1, 2, 3) 
b = []

for c in all_smallcase_letters:
    b.append(c) 

# equivalent to b = list(all_smallcase_letters)

# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
# 2) lower_to_upper
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 
# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1
# 
# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
# --------------------------------------------

# write your code here 

upper_to_lower = {}
lower_to_upper = {}
alpha_to_number = {}
number_to_alphabet = {}

for idx, c in enumerate(b):
    upper_to_lower[c.upper()] = c 
    lower_to_upper[c] = c.upper() 
    alpha_to_number[c] = idx + 1 
    number_to_alphabet[idx + 1] = (c, c.upper())

# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
#  
# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요. 
# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요. 
# --------------------------------------------

a = 'absdf123SAFDSDF'

a_prime1, a_prime2, a_prime3, a_prime4 = '', '', '', True

for c in a:
    if c in upper_to_lower:
        a_prime1 += c 
        a_prime2 += upper_to_lower[c]
        a_prime3 += upper_to_lower[c]
    elif c in lower_to_upper:
        a_prime1 += lower_to_upper[c] 
        a_prime2 += c 
        a_prime3 += lower_to_upper[c]
    else:
        a_prime1 += c 
        a_prime2 += c 
        a_prime3 += c 
        a_prime4 = False 

# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

n = 5

space = ' '
star = '*'

# write your code here 

for i in range(n):
    print(space * (n-i-1) + star * (2*i+1))

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 

for i in range(n):
    print(space * (n-i-1) + (star+space) * (i+1))


# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 

for i in range(n):
    print(space * (n-i-1), end = '')
    for j in range(i+1):
        print(number_to_alphabet[j+1][1] + space, end = '')
    print()

# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

# write your code here 

def make_next_line(lst):
    res = [lst[0]]

    for i in range(len(lst)-1):
        res.append(lst[i] + lst[i+1])

    res.append(lst[-1])

    return res 

lst = [1] 

for i in range(n):
    print(space * (n-i-1), end = '')
    
    for j in range(i+1):
        print(str(lst[j]) + space, end = '')
    lst = make_next_line(lst)
    
    print()



# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         * 
#   *       *       *   
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------

# write your code here 

star = '* '
space = '  '

def print_web(n):
    top = []
    for i in range(n+1):
        top.append(space * i + star + space * (n-i) + star + space * (n-i) + star + space * i)

    mid = [star * (n+1) + star + star * (n+1), ]
    bottom = []

    for e in top:
        bottom = [e] + bottom

    print('\n'.join(top + mid + bottom))

print_web(n)