from itertools import combinations
input_data = [int(x) for x in open('input').read().split('\n')]
print([ a*b*c for a,b,c in combinations(input_data, 3) if a+b+c == 2020 ][0])