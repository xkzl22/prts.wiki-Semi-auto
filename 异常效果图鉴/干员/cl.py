from requests import *
import pyperclip
def xz():
    d=[]
    b=get('https://prts.wiki/w/%E9%A6%96%E9%A1%B5/%E4%BA%AE%E7%82%B9%E5%B9%B2%E5%91%98/%E8%BF%91%E6%9C%9F%E6%96%B0%E5%A2%9E')
    a=b.text
    a=a[a.index('<span>',a.index('::before')+6):]
    a=a[:a.index('</div>')]
    while a.find('title="')!=-1:
        a=a[a.find('title="')+7:]
        c=a[:a.find('>')-1]
        d.append(c)
    return d
#print(xz())
def hq(gy):
    while 1:
        b=get('https://prts.wiki/index.php?title='+gy+'&action=edit')
        if b.status_code!=200:
            d=input('出错了'+str(b.status_code))
            if d=='q':
                return 0
        else:
            break
    a=b.text
    while a.find('&lt;')!=-1:
        a=a[:a.find('&lt;')]+'<'+a[a.find('&lt;')+4:]
    try:
        a=a[a.index('干员页面名')-2:a.index('{{干员导航}}')+8]
    except:
        input('出错了\n'+a)
    c=[gy,a]
    return c
#print(hq('红'))
def fg(sj):
    if sj==0:
        return 0
    gy=sj[0]
    sj=sj[1]
    fh=[gy]
    fh.append(sj[sj.index('==天赋=='):sj.index('==',sj.index('==天赋==')+6)])
    fh.append(sj[sj.index('==技能=='):sj.index('==',sj.index('==技能==')+6)])
    a1=sj.find('==模组==')
    if a1!=-1:
        a2=a1+6
        while 1:
            a2=sj.index('==',a2)
            if sj.find('===',a2)==a2:
                a2+=3
            else:
                fh.append(sj[a1:a2])
                break
    else:
        fh.append('无模组')
    return fh
'''a=fg(hq('煌'))
print(a[0],a[1],a[2],a[3],sep='\n')'''
def fg2(sj):
    if sj==0:
        return 0
    gy=sj[0]
    tf=[]
    jn=[]
    mz=[]
    pd=sj[1].find('{{天赋列表')
    while pd!=-1:
        zc=sj[1].find('{{天赋列表',pd+6)
        tf.append(sj[1][pd:zc].strip())
        sj[1]=sj[1][zc:]
        pd=sj[1].find('{{天赋列表')
    pd=sj[2].find("'''技能")
    while pd!=-1:
        zc=sj[2].find("'''技能",pd+5)
        jn.append(sj[2][pd:zc].strip())
        sj[2]=sj[2][zc:]
        pd=sj[2].find("'''技能")
    pd=sj[3].find("===")
    while pd!=-1:
        zc=sj[3].find("\n===",pd+3)
        mz.append(sj[3][pd:zc].strip())
        sj[3]=sj[3][zc:]
        pd=sj[3].find("===")
    return [gy,tf,jn,mz]
'''a=fg2(fg(hq('煌')))
for b in a:
    for c in b:
        print(c+'\n\n')'''
def tf(gy,wb,gjc,ks=0):
    fx=1
    qn=''
    bz=''
    yw=wb
    jy='0'
    cxpd=0
    pd=wb.find('<references')
    if pd!=-1:
        wb=wb[:pd].strip()
        #fx=3
    pd=wb.rfind('=潜能')
    if pd!=-1:
        qn=wb[pd+3]
        cxpd=1
        cx=wb[wb.rindex('天赋',0,pd):wb.rindex('条件',0,pd)]
    pd=wb.find('|潜能增强=')
    if pd!=-1:
        qn=wb[pd+6]
        cxpd=2
    pd=wb.find('|备注=')
    if pd!=-1:
        bz='\n\n\n'+wb[pd:-3]
        wb=wb[:pd]+wb[-3:]
    pd=wb.rfind('模组')
    if pd!=-1:
        pd=wb.rindex('模组2',0,pd)
        if wb.rfind('精英2',0,pd-5)!=-1:
            jy='2'
            pd=wb.rindex('精英2',0,pd-5)
        elif wb.rfind('精英1',0,pd-5)!=-1:
            jy='1'
            pd=wb.rfind('精英1',0,pd-5)
        else:
            fx=2
    else:
        if wb.rfind('精英2')!=-1:
            jy='2'
        elif wb.rfind('精英1')!=-1:
            jy='1'
        pd=wb.rfind('条件=')
        if pd==-1:
            fx=0
        else:
            pd+=3
    if cxpd!=1:
        print
        cx=wb[wb.rindex('天赋',0,pd):wb.rindex('条件',0,pd)]
    cxzc=wb.rindex(cx)
    if fx==1:
        pd=wb.index('效果=',wb.rindex(cx+'效果='))
        ms=wb[pd+3:wb.index('\n',pd)].strip()
        if ms.find(gjc)==-1 and bz.find(gjc)==-1:
            if ks==0:
                print('未发现'+gjc)
        else:
            mc=wb[wb.index('=',wb.rindex(cx+'='))+1:wb.index('\n|',wb.rindex(cx+'='))]
            while ms.find('{{术语')!=-1:
                pd=ms.index('{{术语')
                ms0=ms[:pd]
                pd=ms.index('|',pd+6)
                zc=ms.index('}}',pd)
                sy=ms[pd+1:zc]
                ms=ms0+sy+ms[zc+2:]
            while ms.find('{{异常效果')!=-1:
                pd=ms.index('{{异常效果')
                zc=ms.index('}}',pd)
                sy=ms[pd+7:zc]
                ms=ms[:pd]+sy+ms[zc+2:]
            while bz.find('{{术语')!=-1:
                pd=bz.index('{{术语')
                bz0=bz[:pd]
                pd=bz.index('|',pd+6)
                zc=bz.index('}}',pd)
                sy=bz[pd+1:zc]
                bz=bz0+sy+bz[zc+2:]
            while bz.find('{{异常效果')!=-1:
                pd=bz.index('{{异常效果')
                zc=bz.index('}}',pd)
                sy=bz[pd+7:zc]
                bz=bz[:pd]+sy+bz[zc+2:]
            fh='{{异常状态作用范围/干员\n|干员='+gy+'\n|类型=天赋|名称='+mc+'\n|精英='+jy
            if qn!='':
                fh+='|潜能='+qn
            fh+='\n|描述='+ms+'\n}}'
            print('\n'+gjc+'\n\n'+fh+bz)
            pyperclip.copy(fh)
            input()
    return fx
def yytf(wb,gjc,ks=0):
    mzcw=0
    if wb==0:
        print('请检查网络连接')
        return
    gy=wb[0]
    if len(wb[1])==0:
        print('*无天赋')
    for wb0 in wb[1]:
        for gjc0 in gjc:
            pd=tf(gy,wb0,gjc0,ks=ks)
            if pd==2:
                mzcw=1
            elif pd==3:
                mzcw=2
            elif pd==0:
                mzcw=3
        if mzcw==2:
            print(wb0)
            input('\n错误：有注释\n')
        elif mzcw==1:
            print(wb0)
            if ks==0:
                input('\n错误：可能为模组新增天赋\n')
            else:
                print('\n错误：可能为模组新增天赋\n')
        elif mzcw==3:
            print(wb0)
            input('\n错误：疑似无文本\n')
        if ks==0:
            input('已完成\n')
    return 1
#yytf(fg2(fg(hq('古米'))),['冻结','寒冷','晕眩','眩晕'])
def jn(gy,wb,gjc):
    cwdm=0
    fx=1
    pd=wb.find('<references')
    if pd!=-1:
        yw=wb
        wb=wb[:pd].strip()
        cwdm=1
    bz=''
    pd=wb.find('|备注=')
    if pd!=-1:
        bz='\n\n\n'+wb[pd:-3]
        wb=wb[:pd]+wb[-3:]
    while bz.find('{{术语')!=-1:
        pd=bz.index('{{术语')
        bz0=bz[:pd]
        pd=bz.index('|',pd+6)
        zc=bz.index('}}',pd)
        sy=bz[pd+1:zc]
        bz=bz0+sy+bz[zc+2:]
    while bz.find('{{异常效果')!=-1:
        pd=bz.index('{{异常效果')
        zc=bz.index('}}',pd)
        sy=bz[pd+7:zc]
        bz=bz[:pd]+sy+bz[zc+2:]
    pd=wb.find(gjc)
    if pd!=-1 or bz.find(gjc)!=-1:
        pd=wb.find('技能名=')
        if pd==-1:
            fx=0
        else:
            mc=wb[pd+4:wb.index('\n|',pd+4)]
            pd=wb.index('类型1=')
            zc=wb[pd+4:wb.index('\n|',pd+4)].strip()
            if zc=='被动':
                cf='\n|触发='+zc
                pd=wb.rindex('持续=')
                cx=wb[pd+3:wb.index('\n}}',pd+3)].strip()
                pd=wb.rindex('描述=')
                ms=wb[pd+3:wb.index('\n|',pd+3)]
                while ms.find('{{术语')!=-1:
                    pd=ms.index('{{术语')
                    ms0=ms[:pd]
                    pd=ms.index('|',pd+6)
                    zc=ms.index('}}',pd)
                    sy=ms[pd+1:zc]
                    ms=ms0+sy+ms[zc+2:]
                while ms.find('{{异常效果')!=-1:
                    pd=ms.index('{{异常效果')
                    zc=ms.index('}}',pd)
                    sy=ms[pd+7:zc]
                    ms=ms[:pd]+sy+ms[zc+2:]
                fh='{{异常状态作用范围/干员\n|干员='+gy+'\n|类型=技能|名称='+mc+cf
                if cx!='':
                    fh+='|持续='+cx
                fh+='\n|描述='+ms+'\n}}'
            else:
                hf=zc
                pd=wb.index('类型2=')
                cf=wb[pd+4:wb.index('\n|',pd+4)]
                pd=wb.rindex('初始=')
                cs=wb[pd+3:wb.index('\n|',pd+3)]
                pd=wb.rindex('消耗=')
                xh=wb[pd+3:wb.index('\n|',pd+3)]
                pd=wb.rindex('持续=')
                cx=wb[pd+3:wb.index('\n}}',pd+3)].strip()
                pd=wb.rindex('描述=')
                ms=wb[pd+3:wb.index('\n|',pd+3)]
                while ms.find('{{术语')!=-1:
                    pd=ms.index('{{术语')
                    ms0=ms[:pd]
                    pd=ms.index('|',pd+6)
                    zc=ms.index('}}',pd)
                    sy=ms[pd+1:zc]
                    ms=ms0+sy+ms[zc+2:]
                while ms.find('{{异常效果')!=-1:
                    pd=ms.index('{{异常效果')
                    zc=ms.index('}}',pd)
                    sy=ms[pd+7:zc]
                    ms=ms[:pd]+sy+ms[zc+2:]
                fh='{{异常状态作用范围/干员\n|干员='+gy+'\n|类型=技能|名称='+mc+'\n|回复='+hf+'|触发='+cf
                if cs!='0' and cs!='':
                    fh+='|初始='+cs
                fh+='|消耗='+xh
                if cx!='':
                    fh+='|持续='+cx
                fh+='\n|描述='+ms+'\n}}'
            if cwdm==1:
                print(yw+'\n错误：有注释')
            print('\n'+gjc+'\n\n'+fh+bz)
            pyperclip.copy(fh)
            input()
    else:
        if ks==0:
            print('未发现'+gjc)
    return fx
def yyjn(wb,gjc,ks=0):
    if wb==0:
        print('请检查网络连接')
        return
    gy=wb[0]
    if len(wb[2])==0:
        print('*无技能')
    for wb0 in wb[2]:
        for gjc0 in gjc:
            pd=jn(gy,wb0,gjc0,ks=ks)
            if pd==0:
                mzcw=1
        if mzcw==1:
            print(wb0)
            input('\n错误：疑似无文本\n')
        if ks==0:
            input('已完成\n')
    return 1
#yyjn(fg2(fg(hq('W'))),['冻结','寒冷','晕眩','眩晕'])
def mz(gy,wb,gjc,ks=0):
    bz=''
    if wb.find('|基础证章=yes')!=-1:
        return 2
    else:
        pd=wb.rfind('=天赋')
        if pd==-1:
            return 0
        tf=wb[pd+1:wb.index('\n|',pd+1)]
        if tf.find(gjc)!=-1:
            pd=wb.index('|天赋2=')
            tf0=wb[pd+5:wb.index('\n|',pd+1)]
            if tf0.find(gjc)!=-1 and tf0.find('新增天赋')!=-1:
                bz='\n|备注=2级后解锁'
            else:
                bz='\n|备注=2级后更新'
            pd=wb.index('|名称=')
            mc=wb[pd+4:wb.index('\n|',pd+4)]
            pd=wb.index('|类型=')
            lx=wb[pd+4:wb.index('\n|',pd+4)]
            while tf.find('{{术语')!=-1:
                pd=tf.index('{{术语')
                tf0=tf[:pd]
                pd=tf.index('|',pd+6)
                zc=tf.index('}}',pd)
                sy=tf[pd+1:zc]
                tf=tf0+sy+tf[zc+2:]
            while tf.find('{{异常效果')!=-1:
                pd=tf.index('{{异常效果')
                zc=tf.index('}}',pd)
                sy=tf[pd+7:zc]
                tf=tf[:pd]+sy+tf[zc+2:]
            fh='{{异常状态作用范围/干员\n|干员='+gy+'\n|类型=模组|名称='+mc+'|模组类型='+lx+'|模组等级=3\n|描述='+tf+bz+'\n}}'
            print('\n'+gjc+'\n\n'+fh)
            pyperclip.copy(fh)
            input()
        else:
            if ks==0:
                print('未发现'+gjc)
    return 1
def yymz(wb,gjc,ks=0):
    if wb==0:
        print('请检查网络连接')
        return
    gy=wb[0]
    if len(wb[3])==0:
        print('*无模组')
    for wb0 in wb[3]:
        for gjc0 in gjc:
            pd=mz(gy,wb0,gjc0,ks=ks)
            if pd==0:
                mzcw=1
            elif pd==2:
                mzcw=2
        if mzcw==1:
            input('\n新模组未规范化，请前往手动编辑规范\n')
        elif mzcw==2:
            print('\n*基础模组\n')
        if ks==0:
            input('已完成\n')
    return 1
#yymz(fg2(fg(hq('初雪'))),['冻结','寒冷','晕眩','眩晕'])
def cx(wb,gjc,ks=0):
    mzcw=0
    if wb==0:
        print('请检查网络连接')
        return 0
    gy=wb[0]
    tfz=wb[1]
    jnz=wb[2]
    mzz=wb[3]
    if len(tfz)==0:
        print('*无天赋')
    for tf0 in tfz:
        for gjc0 in gjc:
            pd=tf(gy,tf0,gjc0,ks=ks)
            if pd==2:
                mzcw=1
            elif pd==3:
                mzcw=2
            elif pd==0:
                mzcw=3
        if mzcw==2:
            print(tf0)
            input('\n错误：有注释\n')
        elif mzcw==1:
            print(tf0)
            input('\n错误：可能为模组新增天赋\n')
        elif mzcw==3:
            print(tf0)
            input('\n错误：疑似无文本\n')
    print('天赋已完成\n')
    if len(jnz)==0:
        print('*无技能')
    for jn0 in jnz:
        for gjc0 in gjc:
            pd=jn(gy,jn0,gjc0,ks=ks)
            if pd==0:
                mzcw=1
        if mzcw==1:
            print(jn0)
            input('\n错误：疑似无文本\n')
    print('技能已完成\n')
    if len(mzz)==0:
        print('*无模组')
    for mz0 in mzz:
        for gjc0 in gjc:
            pd=mz(gy,mz0,gjc0,ks=ks)
            if pd==0:
                mzcw=1
            elif pd==2:
                mzcw=2
        if mzcw==1:
            input('\n新模组未规范化，请前往手动编辑规范\n')
        elif mzcw==2:
            print('\n*基础模组\n')
    if ks==0:
        input('模组已完成\n')
    else:
        print('已完成\n')
    return 1
#cx(fg2(fg(hq('初雪'))),['冻结','寒冷','晕眩','眩晕'])
