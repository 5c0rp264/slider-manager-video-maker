import vlc
# import cv2
# import numpy as np
from utils import RENDERED_VIDEO

def launch_video():
    media_player = vlc.MediaPlayer()
 
    # toggling full screen
    media_player.toggle_fullscreen()
    
    
    # media object
    media = vlc.Media(RENDERED_VIDEO)
    
    # setting media to the media player
    media_player.set_media(media)
    
    # start playing video
    media_player.play()



# def launch_video():

    
#     # Create a VideoCapture object and read from input file
#     cap = cv2.VideoCapture(RENDERED_VIDEO)
#     FPS = 24
#     #cv2.namedWindow("slideshow", cv2.WND_PROP_FULLSCREEN)
#     #cv2.setWindowProperty("slideshow",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
#     while(cap.isOpened()):
        
#         ret, frame = cap.read() 
        
        
#         if ret:
#             cv2.imshow("slideshow", frame)
#         else:
#             print('no video')
#             cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#             continue
        
#         if cv2.waitKey(int(1000/FPS)) & 0xFF == ord('q'):
#             break
        
        
#     cap.release()
#     cv2.destroyAllWindows()