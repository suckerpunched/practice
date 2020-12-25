def is_valid(line):
    r,t,s = line.split(' ')
    r = r.split('-')
    return int(r[0]) <= s.count(t.strip(':')) <= int(r[1])

print(sum([ is_valid(x) for x in open('input').read().split('\n') ]))