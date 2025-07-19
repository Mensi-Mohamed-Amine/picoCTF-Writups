#!/usr/bin/env python3 
import gdb

gdb.execute('file ./otp')
gdb.execute('bp 0x0000555555400630') # breakpoint at strncmp@plt

hexa = list('0123456789abcdef')
guess = ''
cmp = 'lfmhjmnahapkechbanheabbfjladhbplbnfaijdajpnljecghmoafbljlaamhpaheonlmnpmaddhngbgbhobgnofjgeaomadbidl'
i = 0

while i != 100:
    found = False
    for val in hexa:
        gdb.execute('run ' + guess + (val * (100 - i)))
        run = gdb.execute('x/s 0x7fffffffdad0', to_string=True) # our input
        run = run[17:117]
        if cmp[i] == run[i]:
            found = True
            guess += val
            break
    i += 1
    if not found:
        guess += '0'
    print(guess)
print(guess)
