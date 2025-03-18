import cl,time
gy=cl.xz()
input(gy)
gjc=['晕眩','眩晕','不死','推动','击退','推开','拖拽','牵引','弹开','特殊能力','束缚','迷彩','浮空','沉睡','寒冷','冻结','冰冻','停止攻击','不低于']
wl=1
for a in gy:
    if wl==0:
        break
    print(a)
    wl=cl.cx(cl.fg2(cl.fg(cl.hq(a))),gjc,1)
    time.sleep(2)
if wl==1:
    input('ok')
