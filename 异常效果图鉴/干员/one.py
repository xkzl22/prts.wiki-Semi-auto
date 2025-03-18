import cl,time
gy=['麒麟R夜刀']
gjc=['沉睡']
wl=1
for a in gy:
    if wl==0:
        break
    print(a)
    wl=cl.cx(cl.fg2(cl.fg(cl.hq(a))),gjc,1)
if wl==1:
    input('ok')
