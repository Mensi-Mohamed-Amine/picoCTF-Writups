# Keygenme - Writeup

## Description

![Alt text](img/1.png)

## solving process

![Alt text](gif/Keygenme.gif)

## solution

In this challenge we have a binary named Keygenme that takes a license key from user input which is the flag and check if it valid or not .

![Alt text](img/2.png)

## solver

u can execute this gdb script to get the flag ,, use this command

```bash
gdb -x solver.gdb ./need-for-speed
```

```gdb
main
b* set_timer+70
c
set $rdi=50
c
```

## flag

```
picoCTF{br1ng_y0ur_0wn_k3y_19836cd8}
```
