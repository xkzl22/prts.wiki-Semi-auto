from requests import *
import pyperclip,html,time
def xz():
    url='https://prts.wiki/w/%E5%88%86%E7%B1%BB:%E6%95%8C%E4%BA%BA'
    sj=''
    xh=1
    while xh:
        response=get(url)
        wb=html.unescape(response.text)
        pd=wb.index('上一页')
        if wb.find('（下一页）<div',pd)!=-1:
            xh=0
        else:
            pd=wb.index('<a href="',pd)+9
            zc=wb.index('" title=',pd)
            url='https://prts.wiki'+wb[pd:zc]
        pd=wb.index('<li>',pd)
        zc=wb.index('上一页',pd)
        zc=wb.rindex('</li>',0,zc)+5
        sj+=wb[pd:zc]
    return sj
'''with open('cs.txt','w',encoding='utf-8') as cs:
    cs.write(xz())
    cs.close()'''
def dq():
    fgf='|%|'
    try:
        with open('sj\\sj.txt','r',encoding='utf-8') as ywb:
            wb=ywb.read()
        pd=wb.index('|&|')
        cd=int(wb[:pd])
        wb=wb[pd+3:]
        pd=wb.index('|*|')
        rq=wb[:pd]
        wb=wb[pd+3:]
        sj=wb.split(fgf)
        return [rq,cd,sj]
    except FileNotFoundError:
        return None
#print(dq())
def gx(xwb,qzgx=0):
    fgf='|%|'
    sj=[]
    zj=[]
    js=[]
    bl=[]
    de=[]
    sr=dq()
    bc=None
    fh=None
    gxpd=0
    hcpd=0
    while 1:
        pd=xwb.find('title="')
        if pd==-1:
            break
        zc=xwb.index('">',pd)
        sj.append(xwb[pd+7:zc])
        xwb=xwb[xwb.index('</li>')+5:]
    cd=len(sj)
    rq=time.strftime("%y%m%d")
    if sr==None:
        rzsc=rq+' '+str(cd)+'\n已创建\n'
        gxpd=1
        bc=[1,'无数据，已保存本次读取的数据']
    else:
        yrq=sr[0]
        ycd=sr[1]
        ysj=sr[2]
        if ycd==cd and qzgx==0:
            bc=[0,'初步检查未更新']
        else:
            for a in sj:
                if not a in ysj:
                    zj.append(a)
            if int(ycd)+len(zj)>cd:
                print(ycd,len(zj),cd)
                for a in ysj:
                    if not a in sj:
                        js.append(a)
                for xh,a in enumerate(js):
                    while 1:
                        if len(zj)!=0:
                            print('增加的敌人:')
                            for b in zj:
                                print(b)
                            print()
                        xz=input(a+' 删除(d)/保留(r)').strip()[0]
                        if xz=='d' or xz=='r':
                            break
                    if xz=='r':
                        sj.append(a)
                        de.append(xh)
                        print('已保留')
                    elif xz=='d':
                        print('已删除')
                for xh,a in enumerate(de):
                    del js[a-xh]
                for a in bl:
                    js.append(a)
                jspd=len(js)
                rzsc=rq+' '+str(len(sj))+'更新:\n'
                if jspd!=0:
                    rzsc+='*删除\n\n'
                for a in js:
                    rzsc+=a+'\n'
                if jspd!=0 and len(zj)!=0:
                    rzsc+='\n'
                if len(zj)!=0:
                    rzsc+='*增加\n\n'
                for a in zj:
                    rzsc+=a+'\n'
                if jspd!=0 and len(zj)==0:
                    gxpd=1
                    bc=[3,'有删除']
                elif jspd!=0:
                    gxpd=1
                    hcpd=1
                    fh=zj
                    bc=[4,'有删除与更新']
                else:
                    gxpd=1
                    hcpd=1
                    fh=zj
                    bc=[2,'有更新']
            elif len(zj)!=0 and int(ycd)+len(zj)==cd and qzgx==0:
                rzsc=rq+' '+str(len(sj))+'更新:\n增加\n'
                for a in zj:
                    rzsc+=a+'\n'
                gxpd=1
                hcpd=1
                fh=zj
                bc=[2,'有更新']
            elif len(zj)==0:
                bc=[0,'已确认无更新']
            else:
                bc=[-1,'列表比对出错']
                fh=[ysj,zj,sj]
    if gxpd==1:
        sjsc=str(len(sj))+'|&|'
        sjsc+=rq+'|*|'
        sjsc+=sj[0]
        for a in sj[1:]:
            sjsc+=fgf+a
        with open('sj\\sj.txt','w',encoding='utf-8') as sjwj:
            sjwj.write(sjsc)
        with open('sj\\日志.txt','a',encoding='utf-8') as rz:
            rz.write(rzsc)
    if hcpd==1:
        with open('sj\\hc.txt','w',encoding='utf-8') as hcwj:
            hcsc=zj[0]
            for a in zj[1:]:
                hcsc+=fgf+a
            hcwj.write(hcsc)
    return [bc,fh]
#print(gx(xz()))
def dqhc():
    fgf='|%|'
    try:
        with open('sj\\hc.txt','r',encoding='utf-8') as hc:
            wb=hc.read()
        sj=wb.split(fgf)
        return [sj]
    except FileNotFoundError:
        return None
#print(dqhc())
def hq(dr):
    url='https://prts.wiki/index.php?title='+dr+'&action=edit'
    while 1:
        dx=get(url)
        if dx.status_code!=200:
            xw=input('出错了'+str(b.status_code))
            if xw=='q':
                return None
        else:
            break
    wb=html.unescape(dx.text)
    return [dr,wb]
#print(hq('源石虫'))
def fg(sj):
    if sj==None:
        return None
    dr=sj[0]
    wb=sj[1]
    pd=wb.find('<textarea')
    if pd==-1:
        input(wb+'\n出错了')
        return None
    pd=wb.index('>',pd)
    zc=wb.index('</textarea>',pd)
    fh=wb[pd+1:zc]
    return [dr,fh]
#print(fg(hq('杜卡雷，“君主之红”')))
def fg0(sj):
    if sj==None:
        return None
    dr=sj[0]
    wb=sj[1]
    zfh=[]
    while 1:
        fh=[]
        pd=wb.find('==级别')
        if pd==-1:
            break
        pd=wb.index('{{敌人信息/level',pd)
        zc=wb.index('\n}}',pd)
        sj0=wb[pd:zc+3]
        yw=sj0
        wb=wb[zc+3:]
        pd=sj0.index('|index=')
        fh.append(sj0[pd+7])
        fh0=[]
        while 1:
            pd=sj0.find('|技能')
            if pd==-1:
                break
            dj=sj0[pd+3]
            pd=sj0.index('效果=')
            zc=sj0.find('\n|',pd)
            zc0=sj0.find('\n}}',pd)
            if zc==-1:
                zc=zc0
            elif zc0!=-1 and zc>zc0:
                zc=zc0
            elif zc!=-1:
                pass
            else:
                input(sj0+'\n\n'+'敌人分割错误')
                return 0
            fh0.append([dj,sj0[pd+3:zc]])
            sj0=sj0[zc:]
        fh.append(fh0)
        pd=sj0.find('|天赋=')
        if pd==-1:
            fh.append(None)
        else:
            zc=sj0.index('\n}}')
            fh.append(sj0[pd+4:zc])
        fh.append(yw)
        zfh.append(fh)
    return [dr,zfh]
#print(fg0(fg(hq('杜卡雷，“君主之红”'))))
def find(zsj,gjc):
    if zsj==None:
        print('请检查网络连接')
        return None
    dr=zsj[0]
    sj=zsj[1]
    pd=0
    for a in sj:
        dj=a[0]
        for b in a[1]:
            if b[1].find(gjc)!=-1:
                pd=1
                jn=b[0]
                fh='{{异常状态作用范围/敌人\n|敌人='+dr+'\n|类型=技能\n'+'|等级='+dj+'\n|技能='+jn+'\n}}'
                print('\n技能 '+gjc+'\n\n'+fh)
                pyperclip.copy(fh)
                input()
        if a[2]==None:
            pass
        elif a[2].find(gjc)!=-1:
            pd=1
            fh='{{异常状态作用范围/敌人\n|敌人='+dr+'\n|类型=天赋\n'+'|等级='+dj+'\n}}'
            print('\n天赋 '+gjc+'\n\n'+fh)
            pyperclip.copy(fh)
    if pd==0:
        print('未发现'+gjc)
    return pd
#find(fg0(fg(hq('杜卡雷，“君主之红”'))),'晕眩')
def cx(dr,gjc):
    print(dr+'\n')
    sj=fg0(fg(hq(dr)))
    for a in gjc:
        find(sj,a)
#cx('杜卡雷，“君主之红”',['晕眩','寒冷'])
def yy(dr,gjc):
    for a in dr:
        cx(a,gjc)
    print('已完成')
        


