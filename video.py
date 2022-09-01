from pkgutil import ImpImporter
from moviepy.editor import *
import random,os
from utils import OUTPUT_FOLDER, RENDERED_VIDEO

from urllib.parse import urlparse

resolution = (1920, 1080)

def render(data):
    # Create clip 'flow'
    flow = []

    # Load all the clips
    image_clips = []
    duration = 0
    for slide in data:
        parsedUrl = urlparse(slide["link"])
        filename = os.path.basename(parsedUrl.path)
        f = os.path.join(OUTPUT_FOLDER, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(filename)
            image_clips.append(ImageClip(OUTPUT_FOLDER+"/"+filename,duration=slide["duration"]).fx(vfx.resize,width=resolution[0]*1).set_position(("center","center")))
            duration += slide["duration"]


    print(image_clips)
    # Combine all the clips into one
    image_clips = concatenate_videoclips(image_clips, method="compose").set_position(("center","center"))
    image_clips.close()
    print(image_clips)


    #Loading background
    # backgrounds = os.listdir("backgrounds")
    # backgrounds.remove('.DS_Store')
    # background_clip = "backgrounds/" + random.choice(backgrounds)
    # background = VideoFileClip(background_clip).fx(vfx.resize, height=resolution[1]).fx(vfx.loop, duration=image_clips.duration).set_position(("center","center"))
    
    # Composite all the components
    composite = CompositeVideoClip([image_clips],resolution)
    composite.duration = duration

    # Render
    composite.write_videofile(RENDERED_VIDEO,threads=6,fps=24)

    #Removing background clip to avoid repeated background
    #os.remove(background_clip)
    return True
