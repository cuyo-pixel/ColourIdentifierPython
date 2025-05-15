 # -*- coding: utf-8 -*-
import cv2
import numpy as np

darkness_threshold = 60; #Lower limit of brightness
light_threshold = 100; #Upper limit of brightness
   
#Upper and lower color discrimination limit
low_blue = np.array([100,150,150])  
high_blue = np.array([125,255,255])
    
low_green = np.array([45,100,100])
high_green = np.array([99,255,255]) 
    
low_pink = np.array([130,120,120])
high_pink = np.array([170,255,255]) 

low_red = np.array([171,120,120])
high_red = np.array([255,255,255]) 

low_orange = np.array([5,120,120])
high_orange = np.array([21,255,255]) 

low_yellow = np.array([22,120,120])
high_yellow = np.array([44,255,255]) 

#Angle of gradients by color
a = np.radians(0) 
b = np.radians(45)
c = np.radians(90)
e = np.radians(15)
f = np.radians(65)
d = np.radians(30)

cap = cv2.VideoCapture(0) #Capture image from camera 

#Default values for texture size, texture type and color activation
tamLineas=1
textura=1
azulActi=1
verdeActi=1
rosaActi=1
amarilloActi=1
naranjaActi=1
rojoActi=1

def tam(x):
    pass

#Picture window and options
cv2.namedWindow('Imagen')
cv2.namedWindow('Selector')

#Selection bars of options
cv2.createTrackbar('Tama','Imagen',0,2,tam)
cv2.createTrackbar('Textura', 'Imagen',0,1,tam)
cv2.createTrackbar('ActiAzul','Selector',0,1,tam)
cv2.createTrackbar('ActiVerde','Selector',0,1,tam)
cv2.createTrackbar('ActiRosa','Selector',0,1,tam)
cv2.createTrackbar('ActiNaranja','Selector',0,1,tam)
cv2.createTrackbar('ActiRojo','Selector',0,1,tam)
cv2.createTrackbar('ActiAmarillo','Selector',0,1,tam)

while True:
    ret, frame = cap.read()
    
    #Medium image brightness 
    result = cv2.mean(frame)

    if (ret>0) :
        #Change image size
        frame = cv2.resize(frame, (640,480))
        #Conversion to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Masks for each color, using the maximum and minimum values for each color
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
        
        pink_mask = cv2.inRange(hsv_frame, low_pink, high_pink)
        pink = cv2.bitwise_and(frame, frame, mask=pink_mask) 
        
        orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
        orange = cv2.bitwise_and(frame, frame, mask=orange_mask) 
        
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask) 
        
        yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
        yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask) 
        
        #BLUE
        #If it's on 
        if(azulActi==1):
            #Fill 0 with an image of x*y
            blueLines = np.zeros((480,640), np.uint8) 
            #If the texture is gradient lines
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        #8 is the length of each line
                        #dx and dy will be for the tilt, that is, the second point
                        dx,dy = 8*np.cos(a), 8*np.sin(a) 
                        #Draw the line on the empty picture
                        cv2.line(blueLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                #Image obtained with the blue mask
                blue2d = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
                #We multiply by the image containing the lines
                lineasAzul = blue2d*blueLines
            #If the textures are char
            else:
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        cv2.putText(blueLines,"*", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                        
                blue2d = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
                lineasAzul = blue2d*blueLines
        #If it is not activated
        else:
            blue2d=0
            blueLines=0
        
        #AYELLOW
        if(amarilloActi==1):
            yellowLines = np.zeros((480,640), np.uint8) 
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        dx,dy = 8*np.cos(d), 8*np.sin(d) 
                        cv2.line(yellowLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                        
                yellow2d = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)
                lineasyellow = yellow2d*yellowLines
            else:
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        cv2.putText(yellowLines,"!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                        
                yellow2d = cv2.cvtColor(yellow, cv2.COLOR_BGR2GRAY)
                lineasAmarillo = yellow2d*yellowLines
        else:
            yellow2d=0
            yellowLines=0
        
        #ORANGE
        if(naranjaActi==1):
            orangeLines = np.zeros((480,640), np.uint8) 
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        dx,dy = 8*np.cos(e), 8*np.sin(e) 
                        cv2.line(orangeLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                            
                orange2d = cv2.cvtColor(orange, cv2.COLOR_BGR2GRAY)
                lineasNaranja = orange2d*orangeLines
            else:
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        cv2.putText(orangeLines,".", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                            
                orange2d = cv2.cvtColor(orange, cv2.COLOR_BGR2GRAY)
                lineasNaranja = orange2d*orangeLines        
        else:
            orange2d=0
            orangeLines=0
            
        #RED
        if(naranjaActi==1):
            redLines = np.zeros((480,640), np.uint8)
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        dx,dy = 8*np.cos(f), 8*np.sin(f)
                        cv2.line(redLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                            
                red2d = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
                lineasRojo = red2d*redLines
            else:
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        cv2.putText(redLines,"-", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                            
                red2d = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
                lineasRojo = red2d*redLines     
        else:
            red2d=0
            redLines=0
    
        #GREEN
        if(verdeActi==1):
            greenLines = np.zeros((480,640), np.uint8)
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        dx,dy = 8*np.cos(b), 8*np.sin(b)
                        cv2.line(greenLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                        
                green2d = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
                lineasVerde = green2d*greenLines
            else:
               for x in range(0,640,15) :
                for y in range(0,480,15) :
                    cv2.putText(greenLines,"+", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                    
            green2d = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
            lineasVerde = green2d*greenLines     
        else:
            green2d=0
            greenLines=0
        
        #PINK
        if(rosaActi==1):
            pinkLines = np.zeros((480,640), np.uint8) 
            if(textura==1):
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        dx,dy = 8*np.cos(c), 8*np.sin(c)
                        cv2.line(pinkLines,(x,y),(x+int(dx),y+int(dy)),255,tamLineas,1)
                        
                pink2d = cv2.cvtColor(pink, cv2.COLOR_BGR2GRAY)
                lineasMagenta = pink2d*pinkLines + green2d*greenLines + blue2d*blueLines
            else:
                for x in range(0,640,15) :
                    for y in range(0,480,15) :
                        cv2.putText(pinkLines,"o", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), tamLineas)
                        
                pink2d = cv2.cvtColor(pink, cv2.COLOR_BGR2GRAY)
                
        else:
            pink2d=0
            pinkLines=0
            
        #Multiplication of each processed image
        lineasMagenta = pink2d*pinkLines + green2d*greenLines + blue2d*blueLines + orange2d*orangeLines + red2d*redLines + yellow2d*yellowLines
        
        frameSinColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Sum of the images with the lines according to the masks of each color 
        #with the original image in two diems to get the full picture
        frameSinColor += lineasMagenta
        
        # cv.mean() will return 3 numbers, one for each channel:
        #      0=hue
        #      1=saturation
        #      2=value (brightness)
        
        #LIGHT QUANTITY RECOMMENDATION MESSAGE
        if (result[2] < darkness_threshold):
              cv2.putText(frameSinColor, "Recomendado aumentar luz", (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), 2)
        if (result[2] > light_threshold):
              cv2.putText(frameSinColor, "Recomendado disminuir luz", (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255, 255), 2)

        #CAPTION.
        if(cv2.getTrackbarPos('Textura','Imagen') >= 1):
            #Case where the texture is a char.
            if(azulActi==1):
                cv2.putText(frameSinColor, "azul: * ", (10,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
            if(verdeActi==1):
                cv2.putText(frameSinColor, "verde: + ", (10,470), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
            if(rosaActi==1):
                cv2.putText(frameSinColor, "rosa: o ", (130,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
            if(naranjaActi==1):
                cv2.putText(frameSinColor, "naranja: . ", (130,470), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
            if(rojoActi==1):
                cv2.putText(frameSinColor, "rojo: - ", (250,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
            if(amarilloActi==1):
                cv2.putText(frameSinColor, "amarillo: ! ", (270,470), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
        else:
            if(verdeActi==1):
                #Case where the texture is a gradient line.
                cv2.putText(frameSinColor, "verde: ", (10,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                #dx and dy will be for the tilt, i.e. the second point.
                dz,dv = 10*np.cos(b), 10*np.sin(b) 
                cv2.line(frameSinColor,(95,430),(95+int(dz),430+int(dv)),255,3,1)
            if(azulActi==1):
                cv2.putText(frameSinColor, "azul: ", (130,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                db,dk = 10*np.cos(a), 10*np.sin(a)
                cv2.line(frameSinColor,(200,435),(200+int(db),435+int(dk)),255,3,1)
            if(rosaActi==1):
                cv2.putText(frameSinColor, "rosa: ", (10,465), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                db,dk = 10*np.cos(c), 10*np.sin(c) 
                cv2.line(frameSinColor,(90,455),(90+int(db),455+int(dk)),255,3,1)
            if(naranjaActi==1):
                cv2.putText(frameSinColor, "naranja: ", (130,465), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                db,dk = 10*np.cos(e), 10*np.sin(e) 
                cv2.line(frameSinColor,(240,455),(240+int(db),455+int(dk)),255,3,1)
            if(rojoActi==1):
                cv2.putText(frameSinColor, "rojo: ", (250,440), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                db,dk = 10*np.cos(f), 10*np.sin(f) 
                cv2.line(frameSinColor,(320,432),(320+int(db),432+int(dk)),255,3,1)
            if(amarilloActi==1):
                cv2.putText(frameSinColor, "amarillo: ", (270,465), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255, 255), 2)
                db,dk = 10*np.cos(d), 10*np.sin(d) 
                cv2.line(frameSinColor,(390,455),(390+int(db),455+int(dk)),255,3,1)
        
        #Image to show processed
        cv2.imshow("Imagen", frameSinColor)
        
        #Selection bars
        if(cv2.getTrackbarPos('Tama','Imagen') >= 0):
            tamLineas = cv2.getTrackbarPos('Tama','Imagen') + 1
        textura = cv2.getTrackbarPos('Textura', 'Imagen') + 1
        azulActi = cv2.getTrackbarPos('ActiAzul', 'Selector') + 1
        verdeActi = cv2.getTrackbarPos('ActiVerde', 'Selector') + 1
        rosaActi = cv2.getTrackbarPos('ActiRosa', 'Selector') + 1
        naranjaActi = cv2.getTrackbarPos('ActiNaranja', 'Selector') + 1
        rojoActi = cv2.getTrackbarPos('ActiRojo', 'Selector') + 1
        amarilloActi = cv2.getTrackbarPos('ActiAmarillo', 'Selector') + 1
    
        #Close the program with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()