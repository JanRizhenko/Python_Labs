variant = 18
step = variant / 20
start = -variant
end = variant

x = start
while x <= end:
    print(round(x, 1), end=", ")
    x += step
