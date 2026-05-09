import cv2

image = cv2.imread(r"C:\Users\27783\Desktop\Python AI\therock.jpg")

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(grey_image, (224, 224))
cv2.imshow("Processed Image", resized_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('grayscale.jpg', resized_image)

    print("Image Saved as GrayScale.jpg")

else:
    print("Image Not Saved")

cv2.destroyAllWindows()

print(f"processed Image Dimentions: {resized_image.shape}")
