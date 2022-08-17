
from telethon.sync import TelegramClient

from telethon.sync import TelegramClient
from telethon import functions, types
import time

chay_lai_sau_x_giay = int(input("so giay ban muon spam lai tin nhan : "))

fileid=open("id_can_spam.txt","r")

duc=[]
for id in fileid:
    traveidlocxuonghang=id.strip('\n')
    duc.append(traveidlocxuonghang)


from telethon.tl.types import InputUser
tin_nhan=open("tin_nhan.txt","r",encoding="utf8")
chuoi = ""

for a in tin_nhan:
    chuoi += a


api_id = 19061182
api_hash = 'eff34fcae5b9fed06ee48ab87c75dcae'

while True:

        print("bat dau chay ")
        with TelegramClient("name", api_id, api_hash) as client:
            for nguoinhan in duc:
                print(nguoinhan)
                nguoinhan = int(nguoinhan)
                if nguoinhan < -1000000000:
                    nguoinhan -= 1000000000000
                try:
                    result = client(functions.messages.SendMediaRequest(
                        peer=nguoinhan,
                        media=types.InputMediaUploadedPhoto(file=client.upload_file("anh.jpg")),
                        message= chuoi,

                    ))
                except:
                    pass

        print("da chay xong")
        time.sleep(chay_lai_sau_x_giay)















