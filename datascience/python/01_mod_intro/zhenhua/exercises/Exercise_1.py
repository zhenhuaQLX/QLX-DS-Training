# Hello World - variable & One Variable, Two Messages
msg = 'Hello World from Zhenhua!'
print(msg)

msg = 'Hellp World from Zhenhua in the US!'
print(msg)

# Someone Said
quote = "Bill Gates once said:'To be a good professional engineer, \
always start to study late for exams because it teaches you \
how to manage time and tackle emergencies.'"
print(quote)

# First Name Cases
name = 'zhenhua sang'
print(name.lower(),'/', name.title(), '/', name.upper())

# Full Name
fname = 'Zhenhua'
lname = 'Sang'
print(fname + ' ' + lname)

# About This Person
name1 = 'Bill'
name2 = 'Gates'
print(name1 + ' ' + name2 + ' is an American business magnate, \
software developer, investor, and philanthropist.')
print('{} {} is an American business magnate, \
software developer, investor, and philanthropist.'.format(name1, name2))

# Name Strip
stripName = '    \nZhenhua Sang \n\t'
print('|',stripName,'|')
print('|',stripName.lstrip(),'|')
print('|',stripName.rstrip(),'|')
print('|',stripName.strip(),'|')

# Arithmetic
def basicOperatorCal(a,b):
    """Basic operations between a and b.
    Return results following order: addition, \
subtraction, multiplication, division, and exponents."""
    res_add = a + b
    res_sub = a - b
    res_mul = a * b
    res_div = a / b
    res_exp = a ** b
    return print("Input numbers: {} and {} \n'+':{} \n'-':{} \n'*':{} \n'/':{} \n\
'**':{}".format(a, b, res_add, res_sub, res_mul, round(res_div,2), res_exp))

basicOperatorCal(2,3)

# Order of Operations
mul_operations = 15/3+2
print(mul_operations)
mul_operations = 15/(3+2)
print(mul_operations)

# Long Decimals
num_list = [i/10 for i in range(1,10)]
for i in range(len(num_list)):
    num1 = num_list[i]
    for j in range(len(num_list)):
        num2 = num_list[j]
        if num1+num2 > round(num1+num2,1):
            print(num1, num2)
            break

# Python 2 or Python 3?
def versionChk(int1,int2):
    """ Python 2 takes result of '/' as integer rounding value to floor, \
but Python 3 takes it as float without rounding value."""
    try:
        assert int1/int2 == round(int1/int2,0)
        res = 'Python version is 2.x.'
    except AssertionError:
        res = "Python version is 3.x."
    return print(res)

versionChk(3,2)