import math

def max_num(a, b, c):
    list_nums = [a, b, c]
    return max(list_nums)

print(max_num(10, 20, 30))

def max_num2(*argv):
    return max(argv)

print(max_num2(10, 20, 30, 40, 50))

def mult_list(list_input):
    result = 1
    for i in list_input:
        result *= i
    return result

print(mult_list([1, 2, 3]))

#  This version is recursive and inspired by my classmate, William Busby's work:
#  https://github.com/Wubsy/python-function-practice-part-4/blob/main/main.py
#  See his recur_mult_list function.  My version is not a replication of his, but my own take on recursion

def mult_list2(list_input):
    if len(list_input) > 1:
        list_input[0] = list_input[0] * list_input[1]
        del list_input[1:2]
        mult_list2(list_input)
    return list_input[0]

print(mult_list2([1, 2, 3]))

def rev_string(str_input):
    return_string = ""
    for i in range(len(str_input) - 1, -1, -1):
        return_string += str_input[i]
    return return_string

print(rev_string("This is my test string."))

def num_within(num, begin, end):
    return_value = False
    for i in range(begin, end + 1):
        if num == i:
            return_value = True
    return return_value

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# For the pascal function, I utilized the factorial method inside a loop, embedded within another.
# The outside loop is for the rows (number of rows if the parameter, "n")
# The inner loop is for the columns
# My references for the algorithm are:
# https://www.codesdope.com/blog/article/pascal-triangle-algorithm/#:~:text=In%20a%20Pascal%20Triangle%2C%20every,(n%E2%88%92k)!
# and https://www.geeksforgeeks.org/factorial-in-python/

def pascal(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            result = int(math.factorial(i) / (math.factorial(i - j) * math.factorial(j)))
            print(result, " ", end="")
        print()

pascal(5)
