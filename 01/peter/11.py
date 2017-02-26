list_num=[14686, 98259, 22884, 95795, 59961, 50760, 57134, 65016, 24004, 70019, 1608, 59894, 67975, 1677, 60617, 87739, 61754, 20229, 93120, 64838, -1, -2]
max_num1=0
max_mum2=0
for i in list_num:
    if max_num1 > max_mum2 and  max_mum2 < i:
        max_mum2=i
    elif max_num1 < i:
        max_num1 = i
print max_num1,max_mum2
