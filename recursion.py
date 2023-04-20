# n = 4
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def fact_iter(n):
    product = 1
for i in range(n):
    product = product * (i+1)
return product

def fact_recursive(n)
    return n * fact_recursive(n-1)

f = fact_recursive(3)
print(f)