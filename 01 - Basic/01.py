"""
Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
"""

def mult_sum(n1, n2):
    mult = n1 * n2
    sum = n1 + n2
    if mult <= 1000:
        return mult
    else:
        return sum

result = mult_sum(3,5)
print(f'Result = {result}')
result2 = mult_sum(10,30)
print(f'Result = {result2}')