# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:52:16 2018

@author: admin
"""

import numpy as np
import cv2
import pyautogui




cap = cv2.VideoCapture(0)
count=0

while(1):
    
    ## Read the image
    ret, frame = cap.read()
    
    ## Do the processing
    frame = cv2.flip(frame,1)
    
    
    global cx
    global cy
    global old_area,new_area
    old_area,new_area=0,0
    #for yellow color idenitfiaction in frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([14,141,140])#change this hsv values if yellow color as per your lighting condition
    upper_yellow = np.array([84,255,255])#same as above    
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    blur = cv2.medianBlur(mask, 15)
    blur = cv2.GaussianBlur(blur , (5,5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    
    cv2.imshow("mask",mask)
    #find contours in frame
    _,contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
            
    #function to determine which key is pressed based on the center of the contour(yellow paper)
    def key_deter(cx,cy):
        if cy>50 and cy<100:
            if cx>50 and cx<100:
                print("1")
                pyautogui.press("1")
            elif cx>100 and cx<150:
                print("2")
                pyautogui.press("2")
            elif cx>150 and cx<200:
                print("3")
                pyautogui.press("3")
            elif cx>200 and cx<250:
                print("4")
                pyautogui.press("4")
            elif cx>250 and cx<300:
                print("5")
                pyautogui.press("5")
            elif cx>300 and cx<350:
                print("6")
                pyautogui.press("6")
            elif cx>350 and cx<400:
                print("7")
                pyautogui.press("7")
            elif cx>400 and cx<450:
                print("8")
                pyautogui.press("8")
            elif cx>450 and cx<500:
                print("9")
                pyautogui.press("9")
            elif cx>500 and cx<550:
                print("0")
                pyautogui.press("0")
        elif cy>100 and cy<150:
            if cx>50 and cx<100:
                print("q")
                pyautogui.press("q")
            elif cx>100 and cx<150:
                print("w")
                pyautogui.press("w")
            elif cx>150 and cx<200:
                print("e")
                pyautogui.press("e")
            elif cx>200 and cx<250:
                print("r")
                pyautogui.press("r")
            elif cx>250 and cx<300:
                print("t")
                pyautogui.press("t")
            elif cx>300 and cx<350:
                print("y")
                pyautogui.press("y")
            elif cx>350 and cx<400:
                print("u")
                pyautogui.press("u")
            elif cx>400 and cx<450:
                print("i")
                pyautogui.press("i")
            elif cx>450 and cx<500:
                print("o")
                pyautogui.press("o")
            elif cx>500 and cx<550:
                print("p")
                pyautogui.press("p")
        elif cy>150 and cy<200:
            if cx>50 and cx<100:
                print("a")
                pyautogui.press("a")
            elif cx>100 and cx<150:
                print("s")
                pyautogui.press("s")
            elif cx>150 and cx<200:
                print("d")
                pyautogui.press("d")
            elif cx>200 and cx<250:
                print("f")
                pyautogui.press("f")
            elif cx>250 and cx<300:
                print("g")
                pyautogui.press("g")
            elif cx>300 and cx<350:
                print("h")
                pyautogui.press("h")
            elif cx>350 and cx<400:
                print("j")
                pyautogui.press("j")
            elif cx>400 and cx<450:
                print("k")
                pyautogui.press("k")
            elif cx>450 and cx<500:
                print("l")
                pyautogui.press("l")
        elif cy>200 and cy<250:
            if cx>50 and cx<100:
                print("z")
                pyautogui.press("z")
            elif cx>100 and cx<150:
                print("x")
                pyautogui.press("x")
            elif cx>150 and cx<200:
                print("c")
                pyautogui.press("c")
            elif cx>200 and cx<250:
                print("v")
                pyautogui.press("v")
            elif cx>250 and cx<300:
                print("b")
                pyautogui.press("b")
            elif cx>300 and cx<350:
                print("n")
                pyautogui.press("n")
            elif cx>350 and cx<400:
                print("m")
                pyautogui.press("m")
        elif cy>250 and cy<300:
            if cx>100 and cx<450:
                print("space")
                pyautogui.press("space")
            elif cx>450 and cx<550:
                print("Backspace")
                pyautogui.press("backspace")
    
    cv2.drawContours(frame,contours,-1,(0,255,0),2)
    
    
    

    
    if len(contours)>0:
        cnt=max(contours,key=cv2.contourArea)
        if cv2.contourArea(cnt)>600 and cv2.contourArea(cnt)<1200:
             M = cv2.moments(cnt)
             cx = int(M['m10']/M['m00'])
             cy = int(M['m01']/M['m00'])
             #print ("Centroid = ", cx, ", ", cy)
             new_area=cv2.contourArea(cnt)
             #print("new area ",new_area)
             cv2.circle(frame,(cx,cy),1,(0,0,255),2)
             if count==0:
                 old_area=new_area
                 #print("in count==0   ",count)
                 
             count=count+1
             #print(count)
             if count==20:
                 count=0
                 diff_area=new_area-old_area
                 if diff_area>500 and diff_area<1200:
                    print("diff- ",diff_area)
                    key_deter(cx,cy)
                
        
        
    #display the keyboard in the screen        
    def keyboard_layout():   
        x=50
        y=50
        
        for i in range(1,10):
            cv2.rectangle(frame,(x,y),(x+50,100),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        cv2.rectangle(frame,(500,50),(500+50,100),(0,255,0),2)
        cv2.putText(frame,'0',(x+7,90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        list_1="q w e r t y u i o p"
        list_1=list_1.split(" ")
        x=50
        for i in list_1:
            y=150
            cv2.rectangle(frame,(x,y),(x+50,100),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        list_2='a s d f g h j k l '
        list_2=list_2.split(" ")
        x=50
        for i in list_2:
            y=200
            cv2.rectangle(frame,(x,y),(x+50,150),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        
        
        list_3='z x c v b n m   '
        list_3=list_3.split(" ")
        x=50
        for i in list_3:
            y=250
            cv2.rectangle(frame,(x,y),(x+50,200),(0,255,0),2)
            cv2.putText(frame,str(i),(x+7,90+140),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
            x=x+50
        
        
        
        x=100
        y=300
        cv2.rectangle(frame,(x-50,y),(x+350,250),(0,255,0),2)
        
        cv2.rectangle(frame,(x+350,250),(x+450,300),(0,255,0),2)
        cv2.putText(frame,"<--",(x+357,285),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    keyboard_layout()
    cv2.imshow('image',frame)
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
