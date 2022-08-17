import requests
import wget
from utils import OUTPUT_FOLDER



url_api = "https://slider-manager.s-corp.it/api"

def get_uid_from_api():
    print("https://slider-manager.s-corp.it/api/devices/getNewUID")
    response = requests.get(url_api+"/devices/getNewUID")
    print(str(response.status_code) + " : " + str(response.json()))
    uid = response.json()["uid"]
    f = open("uid.txt", "w")
    f.write(uid)
    f.close()
    return uid

def get_uid():
    try:
        reader = open('uid.txt', "r")
        uid = reader.readline()
        reader.close()
        if len(uid) > 0 :
            return uid
        else:
            print("uid is empty in file")
            raise RuntimeError('uid is empty')
    except:
        try :
            return get_uid_from_api()
        except Exception as e:
            print(e)
            return False

def get_data():
    uid = get_uid()
    if not uid:
        print("❌ Failed to get uid !")
        raise RuntimeError('NO UID')
    print("Requesting data at :"+url_api+"/slides/"+uid)
    response = requests.get(url_api+"/slides/"+uid)
    print(str(response.status_code) + " : " + str(response.json()))
    if "Error" in response.json() and response.status_code == 406 :
        #TODO : show uid and ask for association of the device
        print("uid : "+uid)
        print("Add this uid to a new device in the online interface")
        return False
    elif "Error" in response.json():
        return False
    else:
        return response.json()

def download_content(slide_data, order):
    print(slide_data["link"])
    wget.download(slide_data["link"], out=OUTPUT_FOLDER)
    