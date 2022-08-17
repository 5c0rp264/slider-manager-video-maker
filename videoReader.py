import vlc
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