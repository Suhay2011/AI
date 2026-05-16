import cv2

#load the image
image = cv2.imread(r"C:\Users\27783\Desktop\Python AI\therock.jpg")

image = cv2.imread(r"https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQrLSjM2VSvpjDTN3fwQg9TjT6hOQW13YL2VkjOATLf8WOFDheZD-TYM2A0MuW5Tue18jZSymJJmmeW29vocILSqiNun2GYzTbhqn2Q0Y1oIIpzpOsEJ7lqx55VOqdtHUxutg0jsyNx6gA&s=19")

image = cv2.imread(r"https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcTsRYNBDVtYk-2Y9Gy2V5lNUeym2hVE7AuxbDhsMsa3lmjI2zmz4toC0XFe2chZ_gRvbR4i-_6ASHaNrK1SAiFEdAWZ1uIJz5dUZRytL81JMmzmEp5YeKi7BxamMFH5HIDBxEUMYVMP8-1P&s=19")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image',800, 500)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800, 500)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800, 500)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"image DImentions: {image.shape}")
