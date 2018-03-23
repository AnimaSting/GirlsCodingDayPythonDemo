# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 09:39:41 2018

@author: Thinkpad   T420
"""

import turtle
import math

#计算房子的主要参数
angle = float(input("请输入屋顶的角度："))
length = float(input("请输入屋顶斜坡长度："))
h = float(input("请输入房子高度："))
a1 = (180-angle)/2 #房顶两角角度
arca1 = a1*math.pi/180 #a1的弧度
l1 = 2*length*math.cos(arca1) #屋顶底边长
h2 = length*math.sin(arca1) #屋顶高度
w = 7*l1/8 #房屋宽度

#确定从哪里落笔
print('\n',"从屋顶尖尖开始画吧！")
x = float(input("请输入屋顶横坐标："))
y = float(input("请输入屋顶纵坐标："))

t1 = turtle.Turtle() #定义小乌龟

#重置画笔到原点
def sethome():
    t1.pu()
    t1.home()
    t1.seth(0)
    t1.pd()
    return

#放笔
def setpen(x,y):
    t1.pu()
    t1.goto(x,y)
    t1.seth(0)
    t1.pd()
    return

#画房顶
def droof ():
    setpen(x,y)    
    t1.rt(a1) #屋顶三角形
    t1.fd(length)
    t1.rt(180-a1)
    t1.fd(l1)
    t1.rt(180-a1)
    t1.fd(length)    
    len = length #画房顶的瓦
    for i in range(2):
        t1.seth(-angle-a1)
        t1.fd(len/6)
        t1.lt(90)
        t1.circle(len/6,extent=angle) 
        t1.lt(90)
        t1.fd(len/6)
        len *= 2    
    t1.seth(-a1) #画烟囱
    t1.fd(length/4)
    t1.seth(90)
    t1.fd(length/4*math.sin(arca1))
    t1.rt(90)
    t1.fd(length/8)
    t1.rt(90)
    t1.fd((length/4*math.cos(arca1)+length/8)*math.tan(arca1))
    sethome()
    return

#画房子主体
def body():
    #房子主体落笔点
    x0 = x+w/2 
    y0 = y-h2
    #门落笔点
    xm = x0-w/8 
    ym = y0-h
    #窗落笔点
    xc = x-w/12 
    yc = y0-h/12
    
    hm = h/2 #门高
    wm = w/4 #门宽
    ww = w/3 #窗宽高
    
    setpen(x0,y0)  #房子外框     
    for i in range(3): 
        if i%2 ==0:
            t1.rt(90)
            t1.fd(h)
        else:
            t1.rt(90)
            t1.fd(w)
            
    setpen(xm,ym) #门落笔点
    for i in range(3): #画门
        if i%2 ==0:
            t1.lt(90)
            t1.fd(hm)
        else:
            t1.lt(90)
            t1.fd(wm)
            
    setpen(xc,yc) #窗落笔点    
    for i in range(4):
        t1.rt(90)
        t1.fd(ww)
    setpen(xc,yc-ww/2) #横向窗棱落笔点
    t1.back(w/3)
    setpen(xc-ww/2,yc) #纵向窗棱落笔点    
    t1.rt(90)
    t1.fd(ww)
    sethome()
    return

def draw ():   
    droof()
    body()
    sethome()
    t1.hideturtle()
    return

draw()

turtle.done()