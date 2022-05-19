import cv2


# Reading the image
image = cv2.imread('C:/Users/alann/Desktop/images/messi.jpg')


# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
print(image.shape[:2])
# get the center coordinates of the image to create the 2D rotation matrix
# center = (width/2, height/2)

# # using cv2.getRotationMatrix2D() to get the rotation matrix
# rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)

# # rotate the image using cv2.warpAffine
# rotated_image = cv2.warpAffine(
#     src=image, M=rotate_matrix, dsize=(width, height))

dim = (width*2, height*2)
  
# resize image
rotated_image = cv2.resize(image, dim)
# rotated_image = cv2.resize(rotated_image, dsize=(width*2, he))
print(rotated_image.shape[:2])
# rotated_image = image.rotate(image, rotateCode= 0)

cv2.imshow('Original image', image)
cv2.imshow('Rotated image', rotated_image)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# save the rotated image to disk
cv2.imwrite('rotated_image.jpg', rotated_image)
