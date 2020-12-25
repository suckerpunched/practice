from itertools import combinations
input_data = [int(x) for x in open('input').read().split('\n')]
print([ a*b for a,b in combinations(input_data, 2) if a+b == 2020 ][0])