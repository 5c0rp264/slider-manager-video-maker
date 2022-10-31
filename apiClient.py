import requests
import wget
from utils import OUTPUT_FOLDER



url_api = "https://slider-manager.s-corp.it/api"


def get_version():
    try:
        reader = open('version.txt', "r")
        version = reader.readline()
        reader.close()
        if len(version) > 0 :
            return int(version)
        else:
            print("version is empty in file")
            raise RuntimeError('version is empty')
    except:
        try :
            return update_version()
        except Exception as e:
            print(e)
            return False

def update_version():
    uid = get_uid()
    if not uid:
        print("❌ Failed to get uid !")
        raise RuntimeError('NO UID')
    print(url_api+"/version/"+uid)
    response = requests.get(url_api+"/version/"+uid)
    print(str(response.status_code) + " : " + str(response.json()))
    version = response.json()["version"]
    f = open("version.txt", "w")
    f.write(str(version))
    f.close()
    return int(version)

def get_uid_from_api():
    print(url_api+"/devices/getNewUID")
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
        print("uid : "+uid)
        print("Add this uid to a new device in the online interface")
        return False
    elif "Error" in response.json():
        return False
    else:
        update_version()
        return response.json()

def parse_filename_to_data(slide_data):
    for slide in slide_data :
        slide["filename"] = slide["link"].rsplit('/', 1)[-1]

def download_content(slide_data, order):
    print(slide_data["link"])
    wget.download(slide_data["link"], out=OUTPUT_FOLDER)





def is_internet():
    try:
        requests.get("http://www.google.com", timeout=10)
        return True
    except:
        print(Error)
        return False
    