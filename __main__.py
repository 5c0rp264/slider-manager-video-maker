import asyncio,os,video
from apiClient import *
from slideshow import *
from device_setup_screen import *
from wifi_setup_screen import *

#TODO change title "Fancy startup"


 
async def main():
    while True:
        try:
            if is_internet():
                # Clean 'temporary' files from last video
                for file in os.listdir('output'):
                    os.remove(os.path.join('output/', file))

                # Getting all datas from the api
                print("\n⚙️ Getting data")
                slide_data = get_data()
                if slide_data:
                    print("\n⚙️ Parsing data")
                    parse_filename_to_data(slide_data)
                    print(slide_data)


                    print("\n📩 Downloading slide contents")
                    for index, slide in enumerate(slide_data):
                        download_content(slide, index)
                    

                    try:
                        screen.destroy()
                    except Exception as e:
                        print("Error on screen destroy")
                    try:
                        slideshow.destroy()
                    except Exception as e:
                        print("Error on slideshow destroy")



                    print("\n🌟 Displaying slideshow")
                    slideshow = Slideshow(slide_data)
                    slideshow.show_slides()
                    slideshow.mainloop()
                else :
                    uid = get_uid()
                    if uid :
                        screen = Device_setup_screen(uid=uid)
                    else :
                        screen = Device_setup_screen(message="Une errreur est survenue \nMerci de nous contacter")
                    screen.checkloop()
                    screen.mainloop()
            else :
                screen = Wifi_setup_screen()
                screen.mainloop()

            
        except Exception as e:
            print("\n❌ ❌ ❌ : "+str(e))
            # try:
            #     launch_slideshow(slide_data)
            # except Exception as e:
            #     raise e






if __name__ == '__main__':
    [os.mkdir(dir) for dir in ['output','render'] if not os.path.exists(dir)]
    os.system('export DISPLAY=:0')
    futures = [main()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    # asyncio.run(main())
