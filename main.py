a, b = map(int, input().split())
v = a * 60 + b
if v <= 680:
    print('подходящий рейс')
elif 680 < v <= 780:
    print('можно остановиться на этом варианте')
elif v == 727:
    print('неподходящий рейс')
else:
    print('неподходящий рейс')

