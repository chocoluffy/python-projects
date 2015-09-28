from graphics import *
from math import *
def gobangwin():
    win=GraphWin("this is a gobang game",400,400) #ÖÆ×÷21x21µÄÆåÅÌ
    win.setBackground("yellow")
    i1=0
     
    while i1<401:
        l=Line(Point(i1,0),Point(i1,400))
        l.draw(win)
        i1=i1+20
    i2=0
     
    while i2<401:
        l=Line(Point(0,i2),Point(400,i2))
        l.draw(win)
        i2=i2+20
    return win
     
 
def main():
    win = gobangwin()
 
     
    list1 = []
    list2 = []
    list3 = []
     
    change = 0
    g = 0
    m=0
    n=0
     
    while g == 0:
 
       if change%2 == 1:
        p1 = win.getMouse()
        if not ((round((p1.getX()+10)/20),round((p1.getY()+10)/20)) in list3):
              
             a1 = round((p1.getX()+10)/20)
             b1 = round((p1.getY()+10)/20)
             list1.append((a1,b1))
             list3.append((a1,b1))
 
             piece = Circle(Point(20*a1,20*b1),8) #´´½¨Æå×Ó
             piece.setFill('white')
             piece.draw(win)
             for m in range(21): #ÅÐ¶ÏÊäÓ®
                 for n in range(21):
                      
                         if n<17 and (m,n) in list1 and (m,n+1) in list1 and (m,n+2) in list1 and (m,n+3) in list1 and (m,n+4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1     #ÅÐ¶Ï°×ÆåÊúÐÐ
                         elif m<17 and  (m,n) in list1 and (m+1,n) in list1 and (m+2,n) in list1 and (m+3,n) in list1 and (m+4,n) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶Ï°×ÆåºáÐÐ
                         elif m<17 and n<17 and (m,n) in list1 and (m+1,n+1) in list1 and (m+2,n+2) in list1 and (m+3,n+3) in list1 and (m+4,n+4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1    #ÅÐ¶Ï°×ÆåÐ±ÐÐ
                         elif m<17 and n>3 and (m,n) in list1 and (m+1,n-1) in list1 and (m+2,n-2) in list1 and (m+3,n-3) in list1 and (m+4,n-4) in list1 :
                             message = Text(Point(100,100),"white win.")
                             message.draw(win)
                             g = 1     #ÅÐ¶Ï°×ÆåÐ±ÐÐ
                         else: change = change+1  #»»ºÚÆå×ß
             
       else:
        p2 = win.getMouse()
        if not ((round((p2.getX()+10)/20),round((p2.getY()+10)/20)) in list3):
               
               a2 = round((p2.getX()+10)/20)
               b2 = round((p2.getY()+10)/20)
               list2.append((a2,b2))
               list3.append((a2,b2))
                
               piece = Circle(Point(20*a2,20*b2),8)
               piece.setFill('black')
               piece.draw(win)
               for m in range(21):
                 for n in range(21):
                      
                         if n<17 and (m,n) in list2 and (m,n+1) in list2 and (m,n+2) in list2 and (m,n+3) in list2 and (m,n+4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1    #ÅÐ¶ÏºÚÆåÊúÐÐ
                         elif m<17 and  (m,n) in list2 and (m+1,n) in list2 and (m+2,n) in list2 and (m+3,n) in list2 and (m+4,n) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1  #ÅÐ¶ÏºÚÆåºáÐÐ
                         elif m<17 and n<17 and (m,n) in list2 and (m+1,n+1) in list2 and (m+2,n+2) in list2 and (m+3,n+3) in list2 and (m+4,n+4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶ÏºÚÆåÐ±ÐÐ
                         elif m<17 and n>3 and (m,n) in list2 and (m+1,n-1) in list2 and (m+2,n-2) in list2 and (m+3,n-3) in list2 and (m+4,n-4) in list2 :
                             message = Text(Point(100,100),"black win.")
                             message.draw(win)
                             g = 1   #ÅÐ¶ÏºÚÆåÐ±ÐÐ
                         else: change = change+1  #»»°×Æå×ß
                      
    message = Text(Point(100,120),"Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()
     
 
     
main()