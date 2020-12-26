def is_valid(line):
    r,t,s = line.split(' ')
    r = r.split('-')
    return [
        s[int(r[0])-1] == t.strip(':'), 
        s[int(r[1])-1] == t.strip(':'),
    ].count(True) == 1

print(sum([ is_valid(x) for x in open('input').read().split('\n') ]))