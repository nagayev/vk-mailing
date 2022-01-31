from random import randint
import time
import json
import vk_api

f=open('config.json')
content = f.read()
f.close()
data=json.loads(content)
app_id,client_secret = data.get('app_id'),data.get('client_secret')

if (not app_id) or (not client_secret):
    print('Using default client_secret and app_id')
    app_id = 2685278
    client_secret = "hHbJug59sKJie78wjrH8" # Kate Mobile App

def send(uids,message):
    for uid in uids:
       r=randint(10**6,10**7)
       opts={"user_id": uid, "message":message,"random_id":r}
       try:
          vk.method("messages.send",opts)
          time.sleep(0.34)
       except Exception as e:
           print(e)

login=data['login']
password=data['password']
vk=vk_api.VkApi(login=login,
password=password,app_id=app_id,
client_secret=client_secret,
api_version="5.131")
vk.auth()
api=vk.get_api()
ids = data['ids']
start=time.time()
send(ids,data['message'])
delta=time.time()-start
print("Отправлено за {} секунд".
	format(delta))
