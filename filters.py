import cv2
img=cv2.imread(r"C:\Users\27783\Desktop\Python AI\therock.jpg")

if (img is None):
    print("Error")
else:
    print("R for red tint")
    print("I for increase red tint")
    print("d for decrease blue tint")
    print("g for green tint")
    print("q for quit")

    while True:
        new_img=img.copy()

        key=cv2.waitKey(0)

        if (key==ord("r")):
            new_img[:,:,0]=0
            new_img[:,:,1]=0

        elif (key==ord("g")):
             new_img[:,:,0]=0
             new_img[:,:,2]=0

        elif (key==ord("b")):
             new_img[:,:,1]=0
             new_img[:,:,2]=0
        
        elif (key==ord("i")):
             new_img[:,:,2]=cv2.add(new_img[:,:,2],50)

        elif (key==ord("d")):
            new_img[:,:,0]=cv2.subtract(new_img[:,:,0], 50)
        
        elif (key==ord("q")):
            break

        cv2.imshow("Filtered Image",new_img)

cv2.destroyAllWindows()
