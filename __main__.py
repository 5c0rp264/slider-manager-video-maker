import asyncio,os,video
from apiClient import get_data, download_content
from videoReader import launch_video


 
async def main():
    try:

        # Clean 'temporary' files from last video
        for file in os.listdir('output'):
            os.remove(f'output/{file}')

        # Getting all datas from the api
        print("\n⚙️ Getting data")
        slide_data = get_data()
        #print(slide_data)


        print("\n📩 Downloading slide contents")
        for index, slide in enumerate(slide_data):
            download_content(slide, index)

        # Render & Upload
        print("\n🎥 Rendering video...")
        if video.render(slide_data):
            # Upload video if rendered
            print("🌟 Video generated")
            launch_video()
    except Exception as e:
        #just play old video
        raise e






if __name__ == '__main__':
    [os.mkdir(dir) for dir in ['output','render','backgrounds'] if not os.path.exists(dir)]
    asyncio.run(main())
