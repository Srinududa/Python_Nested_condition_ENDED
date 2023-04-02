a = 6
Group_A = (a % 2 == 1)
Group_B = a % 2 == 0
if Group_A:
    print("Group A")
elif Group_B:
    print("Group B")
else:
    print("Group B")

Result==>>>
Group B




a = 16
one_rupee = a % 5
five_rupee = int((a-one_rupee) / 5)
print('5:{}'.format(five_rupee))
print('1:{}'.format(one_rupee))

result=>>
5:3
1:1



h = 1543
a = int( h / 500)
b = int((h - (500*a)) / 50)
c = int((h -((500*a)+(50*b))) / 10)
d  = int((h - ((500*a)+(50*b)+(10*c))) / 1)

print('500: {}'.format(a),'50: {}'.format(b),'10: {}'.format(c),'1: {}'.format(d))

result==>> 500: 3 50: 0 10: 4 1: 3




a = 6

if a ==1 or a == 2:
    print("Week Start")
elif a == 3 or a == 4 or a == 5:
    print("Midweek")
else:
    print("Weekend")

result==>> Weekend


h = 120
if h<=50:
    print(h*3+100)
elif h>50 and h<=100:
    print(50*3 + ((h-50)*5)+100)
elif h>100 and h<=200:
    print(50*3 + 50*5 + ((h-100)*6) +100)
elif h>200:
    print(50*3 + 50*5 + 100*6 + ((h-200)*10)+100)

result==>>620




A = 370
a = int(A/100)
b = int((A-(100*a))/50)
c = int((A-((100*a)+(50*b)))/20)
d = int((A-((100*a)+(50*b)+(20*c)))/10)
print("100 Notes: "+str(a))
print("50 Notes: "+str(b))
print("20 Notes: "+str(c))
print("10 Notes: "+str(d))

result==>>
100 Notes: 3
50 Notes: 1
20 Notes: 1
10 Notes: 0


j = int(input())
a = int(j / 2000)
b = int((j-(2000*a)) / 500)
c = int((j -((2000*a)+(500*b))) / 200)
d = int((j-((2000*a)+(500*b)+(200*c))) / 50)
e = int((j-((2000*a)+(500*b)+(200*c)+(50*d))) / 20)
f = int((j-((2000*a)+(500*b)+(200*c)+(50*d)+(20*e))) / 5)
g = int(((j-((2000*a)+(500*b)+(200*c)+(50*d)+(20*e)+(5*f)))) / 2)
h = int(((j-((2000*a)+(500*b)+(200*c)+(50*d)+(20*e)+(5*f)+(2*g))) / 1))
print('2000:%s'%(a),'500:%s'%(b),'200:%s'%(c),'50:%s'%(d),'20:%s'%(e),'5:%s'%(f),'2:%s'%(g),'1:%s'%(h) )

result==>> 2000:1 500:0 200:1 50:1 20:0 5:1 2:1 1:0




a = 29

Group_A = a % 6 == 1
Group_B = a % 6 == 2
Group_C = a % 6 == 3
Group_D = a % 6 == 4
Group_E = a % 6 == 5
Group_F = a % 6 == 0
if Group_A:
    print("Group 1")
elif Group_B:
    print("Group 2")
elif Group_C:
    print("Group 3")
elif Group_D:
    print("Group 4")
elif Group_E:
    print("Group 5")
elif Group_F:
    print("Group 6")
else:
    print("Group 6")
    

Result==>>>Group 5





a = 70
if a<=40:
    print(a*2+50)
elif a>40 and a<=60:
    print(40*2 + ((a-40)*4) + 50)
elif a>60 and a<=120:
    print(40*2 + 20*4 + ((a-60)*6) + 50)
elif a>120:
    print(40*2 + 20*4 + 60*6 + ((a-120)*8) + 50)
else:
    print(40*2 + 20*4 + 60*6 + ((a-120)*8) + 50)

Result==>> 270