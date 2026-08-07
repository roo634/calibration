from renderer import Renderer

import cv2


frame = cv2.imread("C:/Users/Student/Downloads/1280x720 image.jpg")

renderer = Renderer()

frame = renderer.process(frame)

cv2.imshow('image',frame)
cv2.waitKey(0)