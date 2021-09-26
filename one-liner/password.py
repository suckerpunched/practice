from secrets import choice; print(''.join([ chr(choice([ *range(33,127,1) ])) for i in range(16) ]))
