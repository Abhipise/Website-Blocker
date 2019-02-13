import time
from datetime import datetime as dt

hosts_path="C:\Windows\System32\drivers\etc\hosts"

# hosts_path="F:\Application\App3\hosts"
redirect="127.0.0.1"
websites_list =["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in websites_list:
                 if website in content:
                     pass
                 else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun Hours....")
    time.sleep(5)
