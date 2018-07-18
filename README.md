# Belt-for-Parkinson-s-patients

Patients suffering from Parkinson's diesease experience a problem called as Freeze of Gait. This causes them to suddenly freeze when they are walking on the roads or other flat surfaces. However, research and experiments have shown that these patients can easily walk on staircases. They can also walk on zebra crossings as these create an illusion of a staircase on the road. 

So, our project is all about creating this illusion on the road/floor. As printing such patterns on every surface such people walk on(as proposed by the author of a paper that we referred for this project) might be infeasible, we thought of using technology to solve this problem. 

We offer a simple and elegant solution. We capture the image of the surface the person walks on via a camera, use our python script to print a staircase illusion on this image and then finally project this image back to the floor. When the person climbs on a staircase, he can manually disable this device with a simple button press. 

As this is just a proof of concept, we have currently projected the manipulated image onto the monitor connected to the dragonboard. 

Also, we could AR for better implementation. 

This project setup includes the following connections:
1. Interface a camera with the Dragonboard using the USB port.
2. Interface a display using the HDMI port.
3. We used the Debian linux OS on the board.
4. Copy the source code (staircase_add.py).
5. Run the python script.

