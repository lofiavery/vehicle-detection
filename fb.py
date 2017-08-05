import urllib.request
from urllib.error import HTTPError, URLError

def downloadFile(file_name, file_mode, base_url):
    url = base_url + file_name + "/picture"

    try:
            f = urllib.request.urlopen(url)
            print("downloading ", url)

            # Open our local file for writing
            local_file = open(file_name+".jpg", "w" + file_mode)
            local_file.write(f.read())
            local_file.close()

    except HTTPError as e:
            print("HTTP Error:", e.code, url)
    except URLError as e:
            print("URL Error:", e.reason, url)

profile = 100002599463613  
while(1 == 1):
    base_url = 'https://graph.facebook.com/'
    s_index = str(profile)
    file_name = s_index
    downloadFile(file_name, "b", base_url)
    profile = profile + 1
