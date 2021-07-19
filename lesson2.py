n = int (input())
name1 = 'Часы'
x = n // 3600
name2 = 'Минуты'
y = (n - x * 3600)//60
name3 = 'Секунды'
c = (n - (x * 3600+y*60))
temp = f'{name1} {x} {name2} {y} {name3} {c}'
print (temp)