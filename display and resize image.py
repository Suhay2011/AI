import cv2

#load the image
image = cv2.imread(r"C:\Users\27783\Desktop\Python AI\therock.jpg")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image',800, 500)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"image DImentions: {image.shape}")
