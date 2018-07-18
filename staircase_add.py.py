import cv2, sys
# Define constants
DEVICE_NUMBER = 0
# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)
# Check if the webcam works
if vc.isOpened():
 # Try to get the first frame
 retval, frame = vc.read()
else:
 # Exit the program
 sys.exit(1)
# Read in the next frame
retval, frame = vc.read()
# Show the frame to the user
pixel = frame[200,200]

height, width, channels = frame.shape
inv_frame = cv2.bitwise_not(frame)

first_rail_1 = width/3
first_rail_2 = width/3 + 0.025*width

second_rail_1 = 2*width/3
second_rail_2 = 2*width/3 + 0.025*width


for i in list(range(height)):
    for j in list(range(width)):
        if (j >= first_rail_1 and j <= second_rail_2):
            if(i % 100 >= 50):
                frame[i,j] = inv_frame[i,j]


cv2.imshow("DragonBoard 410c Workshop", frame)
# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
