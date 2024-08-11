from lv_1 import number_to_alphabet, make_next_line, print_web

# lv_1.py에서 if __name__ == '__main__' 밖에서 실행하는 것이 많기 때문에 lv_1.py에서 실행하는 것들이 같이 찍혀 나올 것 

# --------------------------------------------
# 1. 패턴 찍는 함수들 만들어보기 
# 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid1를 짜 보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

n = 5

# write your code here 
def pyramid1(n):
    space = ' '
    star = '*'
    lines = []

    for i in range(n):
        lines.append(space * (n-i-1) + star * (2*i+1))

    return '\n'.join(lines)

# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid2를 짜 보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 
def pyramid2(n):
    space = ' '
    star = '*'
    lines = []

    for i in range(n):
        lines.append(space * (n-i-1) + (star+space) * (i+1))

    return '\n'.join(lines)

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid3를 짜 보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 
def pyramid3(n):
    space = ' '
    star = '*'
    lines = []

    for i in range(n):
        line = ''
        line += space * (n-i-1)
        for j in range(i+1):
            line += number_to_alphabet[j+1][1] + space
        lines.append(line)

    return '\n'.join(lines)


# -------------------------------------------- 
# 4) 피라미드 찍어보기 - 4 
# 
# 다음과 같은 패턴의 높이를 받아, 다음 패턴을 프린트하는 함수 pyramid4를 짜 보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

def pascal(n):
    def generate_next_line(last_line):
        n = len(last_line) + 1
        
        next_line = [last_line[0]]

        for i in range(n-2):
            next_line.append(last_line[i] + last_line[i+1])

        next_line.append(last_line[n-2])

        return next_line
    
    lines = [[1], [1,1]]
    
    while len(lines) != n:
        lines.append(generate_next_line(lines[-1]))

    space = ' '

    def fill(number, digits, fill_with = '0'):
        number_digit = get_digit(number)
        return (digits - number_digit) * fill_with + str(number)

    def get_digit(number):
        # int(log_10(n))
        # 123 
        digit = 1
        
        while True:
            if number < 10:
                break 
            else:
                digit += 1 
                number = number // 10 
        
        return digit 

    # print(fill(123, 4)) # 0123
    # print(fill(123, 5)) # 00123
    # print(fill(123, 4, '|')) # |123

    max_number = max(lines[-1])
    max_digit = get_digit(max_number)


    space = ' ' * max_digit
    res_lines = []
    
    for idx, line in enumerate(lines):
        res_lines.append((n-1-idx)*space + space.join([\
            fill(e, max_digit, ' ') for e in line]))
    
    return '\n'.join(res_lines)



# write your code here 
def pyramid4(n):
    return pascal(n)

# --------------------------------------------
# 5) 다음 패턴을 찍는 함수 sierpinski_triangle을 짜 보세요. 
# 
# n = 2
#         *
#        * *
#       *   *
#      * * * *
#     *       * 
#    * *     * *
#   *   *   *   * 
#  * * * * * * * * 
# 
# n = 3 
#                 *
#                * *
#               *   *
#              * * * *
#             *       * 
#            * *     * *
#           *   *   *   * 
#          * * * * * * * *
#         *               *   
#        * *             * *  
#       *   *           *   * 
#      * * * *         * * * *
#     *       *       *       *  
#    * *     * *     * *     * *
#   *   *   *   *   *   *   *   * 
#  * * * * * * * * * * * * * * * *
# --------------------------------------------

# write your code here 

def triangle():
    lines = [\
      '   *    ',
      '  * *   ',
      ' *   *  ',
      '* * * * ',
    ]
    return lines 

def lstsum(l, r):
    assert len(l) == len(r)
    
    res = []
    for i in range(len(l)):
        res.append(l[i] + r[i])

    return [(a+b) for a, b in zip(l, r)]

def big_triangle():
    res = []
    res += [' ' * 4 + line + ' ' * 4 for line in triangle()]
    
    res += lstsum(triangle(), triangle())
    
    return res 

def big_big_triangle():
    res = []
    res += [' ' * 8 + line for line in big_triangle()]
    
    res += lstsum(big_triangle(), big_triangle())
    
    return res 

def sierpinski_triangle_list(n):
    if n == 1:
        return triangle()
    else:
        res = [' '*2**n + line + ' '*2**n for line in sierpinski_triangle_list(n-1)]
        res += lstsum(sierpinski_triangle_list(n-1), sierpinski_triangle_list(n-1))
        return res 

def sierpinski_triangle(n):
    return '\n'.join(sierpinski_triangle_list(n))


# --------------------------------------------
# 2. 여러 리스트 관련 함수들 구현해보기 
#
# 아래 함수들은 대부분 itertools에 있는 함수들임. 
# itertools를 쓰지 말고 구현해 볼 것.  
#
# 1) accumulate(lst, function = lambda x, y : x+y)
# 
# lst의 각 원소들에 대해서, function을 누적하여 적용한 리스트를 반환. 
# lst -> [lst[0], f(lst[0], lst[1]), f(lst[2], f(lst[1], lst[0])), ...] 
# --------------------------------------------

# write your code here 
def accumulate(lst, function = lambda x, y: x+y):
    if lst == []:
        return lst 
    
    res = [lst[0]]

    for e in lst[1:]:
        res.append(function(res[-1], e))

    return res 

# --------------------------------------------
# 2) batched(lst, n)
# 
# lst의 원소들을 n개의 인접한 원소들끼리 묶은 리스트를 반환. 
# ex) batched([1,2,3,4,5], 2) 
#     >> [(1,2), (3,4), (5,)]
# ex) batched(['a', 'b', 1, 3, 6, 1, 3, 7], 3) 
#     >> [('a', 'b', 1), (3, 6, 1), (3, 7)]
# --------------------------------------------

# write your code here 
def batched(lst, n):
    res = []
    
    for idx in range(len(lst)-n-1):
        res.append(tuple(lst[idx:idx+n]))

    return res 

# --------------------------------------------
# 3) product(args)
# 
# list들의 list args를 받아서, 각각의 리스트에서 하나씩의 원소를 뽑은 튜플들의 리스트를 반환. 
# ex) product([[1,2,3], [4,5,6]])
#     >> [(1,4), (1,5), (1,6), 
#         (2,4), (2,5), (2,6), 
#         (3,4), (3,5), (3,6),] 
# --------------------------------------------

# write your code here 
def product(args):
    if len(args) == 1 and isinstance(args[0], list):
        return [(e,) for e in args[0]]
    else:
        res = []
        lst = product(args[1:])

        for e in args[0]:
            for f in lst:
                res.append(tuple([e] + list(f)))

        return res 

# --------------------------------------------
# 4) permutations(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 permutation의 리스트를 반환. 
# permutation이란, 순서를 가지면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 다르고, 1,1은 허용되지 않음. 
# ex) permutations([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,1), (2,3), (2,4), (2,5), 
#         (3,1), (3,2), (3,4), (3,5), 
#         (4,1), (4,2), (4,3), (4,5), 
#         (5,1), (5,2), (5,3), (5,4),]
# --------------------------------------------

def have_dupliace(lst):
    return len(lst) != len(set(lst))

# write your code here 
def permutations(lst, r):
    args = [lst for _ in range(r)]
    res = []
    
    for e in product(args):
        if not have_dupliace(e):
            res.append(e) 

    return res 

# --------------------------------------------
# 5) combination(lst, r) 
#
# lst 안의 원소들 r개로 이루어진 combination의 리스트를 반환. 
# combination이란, 순서를 가지지 않으면서 중복을 허용하지 않는 부분집합을 의미함. 
# 즉 여기서는 1,2와 2,1은 같고, 1,1은 허용되지 않음. 
# ex) combination([1,2,3,4,5], 2)
#     >> [(1,2), (1,3), (1,4), (1,5), 
#         (2,3), (2,4), (2,5), 
#         (3,4), (3,5), 
#         (4,5), ]
# --------------------------------------------

def have_same_combination(l, res):
    return set(l) in [set(r) for r in res]

# write your code here 
def combination(lst, r):
    args = [lst for _ in range(r)]
    res = []
    
    for e in product(args):
        if not have_dupliace(e) and not have_same_combination(e, res):
            res.append(e) 

    return res 

# --------------------------------------------
# 6) combination_with_duplicate(lst, r)
#
# lst 안의 원소들 r개로 이루어진 중복을 허용하는 combination의 리스트를 반환. 
# ex) combination_with_duplicate([1,2,3,4,5], 2)
#     >> [(1,1), (1,2), (1,3), (1,4), (1,5), 
#         (2,2), (2,3), (2,4), (2,5), 
#         (3,3), (3,4), (3,5), 
#         (4,4), (4,5),
#         (5,5), ]
# --------------------------------------------

# write your code here 
def combination_with_duplicate(lst, r):
    args = [lst for _ in range(r)]
    res = []
    
    for e in product(args):
        if not have_same_combination(e, res):
            res.append(e) 

    return res 

    
if __name__ == '__main__':

    assert pyramid1(5).split('\n') == ['    *', '   ***', '  *****', ' *******', '*********']
    assert pyramid2(5).split('\n') == ['    * ', '   * * ', '  * * * ', ' * * * * ', '* * * * * ']
    assert pyramid3(5).split('\n') == ['    A ', '   A B ', '  A B C ', ' A B C D ', 'A B C D E ']
    assert pyramid4(5).split('\n') == ['    1', '   1 1', '  1 2 1', ' 1 3 3 1', '1 4 6 4 1']
    assert sierpinski_triangle(5).split('\n') == ['                                                               *                                                                ', '                                                              * *                                                               ', '                                                             *   *                                                              ', '                                                            * * * *                                                             ', '                                                           *       *                                                            ', '                                                          * *     * *                                                           ', '                                                         *   *   *   *                                                          ', '                                                        * * * * * * * *                                                         ', '                                                       *               *                                                        ', '                                                      * *             * *                                                       ', '                                                     *   *           *   *                                                      ', '                                                    * * * *         * * * *                                                     ', '                                                   *       *       *       *                                                    ', '                                                  * *     * *     * *     * *                                                   ', '                                                 *   *   *   *   *   *   *   *                                                  ', '                                                * * * * * * * * * * * * * * * *                                                 ', '                                               *                               *                                                ', '                                              * *                             * *                                               ', '                                             *   *                           *   *                                              ', '                                            * * * *                         * * * *                                             ', '                                           *       *                       *       *                                            ', '                                          * *     * *                     * *     * *                                           ', '                                         *   *   *   *                   *   *   *   *                                          ', '                                        * * * * * * * *                 * * * * * * * *                                         ', '                                       *               *               *               *                                        ', '                                      * *             * *             * *             * *                                       ', '                                     *   *           *   *           *   *           *   *                                      ', '                                    * * * *         * * * *         * * * *         * * * *                                     ', '                                   *       *       *       *       *       *       *       *                                    ', '                                  * *     * *     * *     * *     * *     * *     * *     * *                                   ', '                                 *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *                                  ', '                                * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *                                 ', '                               *                                                               *                                ', '                              * *                                                             * *                               ', '                             *   *                                                           *   *                              ', '                            * * * *                                                         * * * *                             ', '                           *       *                                                       *       *                            ', '                          * *     * *                                                     * *     * *                           ', '                         *   *   *   *                                                   *   *   *   *                          ', '                        * * * * * * * *                                                 * * * * * * * *                         ', '                       *               *                                               *               *                        ', '                      * *             * *                                             * *             * *                       ', '                     *   *           *   *                                           *   *           *   *                      ', '                    * * * *         * * * *                                         * * * *         * * * *                     ', '                   *       *       *       *                                       *       *       *       *                    ', '                  * *     * *     * *     * *                                     * *     * *     * *     * *                   ', '                 *   *   *   *   *   *   *   *                                   *   *   *   *   *   *   *   *                  ', '                * * * * * * * * * * * * * * * *                                 * * * * * * * * * * * * * * * *                 ', '               *                               *                               *                               *                ', '              * *                             * *                             * *                             * *               ', '             *   *                           *   *                           *   *                           *   *              ', '            * * * *                         * * * *                         * * * *                         * * * *             ', '           *       *                       *       *                       *       *                       *       *            ', '          * *     * *                     * *     * *                     * *     * *                     * *     * *           ', '         *   *   *   *                   *   *   *   *                   *   *   *   *                   *   *   *   *          ', '        * * * * * * * *                 * * * * * * * *                 * * * * * * * *                 * * * * * * * *         ', '       *               *               *               *               *               *               *               *        ', '      * *             * *             * *             * *             * *             * *             * *             * *       ', '     *   *           *   *           *   *           *   *           *   *           *   *           *   *           *   *      ', '    * * * *         * * * *         * * * *         * * * *         * * * *         * * * *         * * * *         * * * *     ', '   *       *       *       *       *       *       *       *       *       *       *       *       *       *       *       *    ', '  * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *     * *   ', ' *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  ', '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ']


    assert product([[1,2,3], [4,5,6]]) == [\
        (1, 4), (1, 5), (1, 6),
        (2, 4), (2, 5), (2, 6), 
        (3, 4), (3, 5), (3, 6),]
    
    assert product([[1,2,3], [4,5,6], [7,8,9]]) == [\
        (1, 4, 7), (1, 4, 8), (1, 4, 9), 
        (1, 5, 7), (1, 5, 8), (1, 5, 9), 
        (1, 6, 7), (1, 6, 8), (1, 6, 9), 
        (2, 4, 7), (2, 4, 8), (2, 4, 9), 
        (2, 5, 7), (2, 5, 8), (2, 5, 9), 
        (2, 6, 7), (2, 6, 8), (2, 6, 9), 
        (3, 4, 7), (3, 4, 8), (3, 4, 9), 
        (3, 5, 7), (3, 5, 8), (3, 5, 9), 
        (3, 6, 7), (3, 6, 8), (3, 6, 9),]
    
    assert permutations([1,2,3,4,5], 2) == [\
        (1, 2), (1, 3), (1, 4), (1, 5), 
        (2, 1), (2, 3), (2, 4), (2, 5), 
        (3, 1), (3, 2), (3, 4), (3, 5), 
        (4, 1), (4, 2), (4, 3), (4, 5), 
        (5, 1), (5, 2), (5, 3), (5, 4),]
    
    assert permutations([1,2,3,4,5], 3) == [\
        (1, 2, 3), (1, 2, 4), (1, 2, 5), 
        (1, 3, 2), (1, 3, 4), (1, 3, 5), 
        (1, 4, 2), (1, 4, 3), (1, 4, 5), 
        (1, 5, 2), (1, 5, 3), (1, 5, 4), 
        (2, 1, 3), (2, 1, 4), (2, 1, 5), 
        (2, 3, 1), (2, 3, 4), (2, 3, 5),
        (2, 4, 1), (2, 4, 3), (2, 4, 5), 
        (2, 5, 1), (2, 5, 3), (2, 5, 4), 
        (3, 1, 2), (3, 1, 4), (3, 1, 5), 
        (3, 2, 1), (3, 2, 4), (3, 2, 5), 
        (3, 4, 1), (3, 4, 2), (3, 4, 5), 
        (3, 5, 1), (3, 5, 2), (3, 5, 4), 
        (4, 1, 2), (4, 1, 3), (4, 1, 5), 
        (4, 2, 1), (4, 2, 3), (4, 2, 5), 
        (4, 3, 1), (4, 3, 2), (4, 3, 5), 
        (4, 5, 1), (4, 5, 2), (4, 5, 3), 
        (5, 1, 2), (5, 1, 3), (5, 1, 4), 
        (5, 2, 1), (5, 2, 3), (5, 2, 4), 
        (5, 3, 1), (5, 3, 2), (5, 3, 4), 
        (5, 4, 1), (5, 4, 2), (5, 4, 3),]

    assert combination([1,2,3,4,5], 2) == [\
        (1, 2), (1, 3), (1, 4), (1, 5), 
        (2, 3), (2, 4), (2, 5), 
        (3, 4), (3, 5), 
        (4, 5)]

    assert combination_with_duplicate([1,2,3,4,5], 2) == [\
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), 
        (2, 2), (2, 3), (2, 4), (2, 5), 
        (3, 3), (3, 4), (3, 5), 
        (4, 4), (4, 5), 
        (5, 5)]