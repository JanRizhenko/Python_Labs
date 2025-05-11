variant = 18
step = variant / 40
start = variant
end = -variant

x = start
while x >= end:
    print(round(x, 2), end="; ")
    x -= step
