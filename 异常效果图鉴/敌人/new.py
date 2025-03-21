import cl
gjc=['眩晕','晕眩','不死','免疫失衡','失衡免疫','沉默','束缚','寒冷','冻结','隐匿免疫','迷彩','浮空','沉睡']
a=cl.gx(cl.xz())
if len(a[1])==0:
    input(a[0][0])
else:
    while 1:
        print(a[0][0],a[1])
        b=input('数据已保存\n直接回车进行半自动化更新，输入"q"退出')
        if b=='':
            cl.yy(a[1],gjc)
            break
        elif b=='q':
            break
