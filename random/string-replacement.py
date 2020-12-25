def replace(text, replacements):
    offset,result = 0,[]
    for replacement in replacements:
        start,before,after = replacement.values()
        
        if start != 0: result.append(text[offset:start])
        
        result.append(after)
        offset = start + len(before)
    
    result.append(text[offset:])
    return ''.join(result)

r = replace('num Foo', [
    {'start': 0, 'before': 'num', 'after': 'String'},
    {'start': 4, 'before': 'Foo', 'after': 'bar'}
])

print(r)

>>> String bar
