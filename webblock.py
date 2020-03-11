import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
weblist = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com', 'https://twitter.com/home']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for webs in weblist:
                if webs in content:
                    pass
                else:
                    file.write(redirect+ " "+ webs+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any (webs in line for webs in weblist):
                    file.write(line)
            file.truncate()
        print('Fun time')
    time.sleep(5)
