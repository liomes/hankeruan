print("**************************************")
print("*           12月份一份销售数据         *")
print("日期  服装   价格/件   库存数量 销售量/每日")
print("1  羽绒服   253.6    500    10")
print("2  牛仔裤    86.3    600    60")
print("3   风衣     96.8    335     43")
print("4   皮草    135.9     855    63")
print("5  T血     65.8     632     63 ")
print("6   衬衫    49.3      562    120")
print("7   牛仔裤    86.3    600    72")
print("8   羽绒服    253.6    500    69")
print("9   牛仔裤    86.3    600     90")
print("10   羽绒服   253.6    500    140")
print("11   牛仔裤    86.3     600   35")
print("12   皮草    135.69    855    24")
print("13    T血    65.8      632   129")
print("14   羽绒服   253.6      500   10")
print("15   牛仔裤    86.3     600    43")
print("16   T血      65.8     632     63")
print("17   牛仔裤    86.3     600    60")
print("18   风衣     96.8       335   60")
print("19   T血      65.8      632    63")
print("20   牛仔裤    86.3      600    60")
print("21  皮草     135.9      855    63")
print("22   风衣      96.8       335    43")
print("23  T血      65.8        632   58")
print("24  牛仔裤     86.3      600    140")
print("25    T血       65.8     632      48")
print("26    风衣      96.8      335    43")
print("27   皮草       135.9     855    57")
print("28   羽绒服      253.6     500     10")
print("29   T血        65.8      632    63")
print("30   风衣        96.8      335     78")
print("*               林海旺               *")
t = 10+69+140+10+10            #羽绒服的总销售额，单价为253.6
q = 43+25+43+60+43+78          #风衣的总销售额，单价为96.8
w = 120                         #衬衫的总销售额，单价为49.3
e = 60+72+35+90+60+60+140       #牛仔裤的总销售额，单价为86.3
r = 63+45+129+63+58+48+63       #T血的总销售额，单价为65.8
y = 63+24+63+57                #皮草的总销售额，单价为135.9
sum = (t*253.6+q*96.8+w*49.3+e*86.3+r*65.8+y*135.9)
print("12月份总销售额", round(sum, 2))
total=(t+q+w+e+r+y)
print("12月份平均每日销售额:%.2f" %((total) / 30))
print("羽绒服的月销售占比:{:.0%}".format(t/total))
print("风衣的月销售占比:{:.0%}".format(q/total))
print("衬衫的月销售占比:{:.0%}".format(w/total))
print("牛仔裤的月销售占比:{:.0%}".format(e/total))
print("T血的月销售占比:{:.0%}".format(r/total))
print("皮草的月销售占比:{:.0%}".format(y/total))
