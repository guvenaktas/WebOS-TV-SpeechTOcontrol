from multiprocessing.connection import Client
import os
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *



store = {} ## When script works first time then you can see tv asks for approval to connection.
           ## If you are click yes,then you can see client key output in the script
           ### example; store = {'client_key': '560c1d677984b58e0070668b5xxxxxa'}

client = WebOSClient("192.168.1.20") ## ip adress of LG TV

client.connect()
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("TV de çıkan bağlantıyı onaylayınız!")
    elif status == WebOSClient.REGISTERED:
        print("TV baglantısı yapıldı!",store)

def sesac():
    media = MediaControl(client)
    media.volume_up() 
def seskis():
    media = MediaControl(client)
    media.volume_down() 
def sesmute(status):
    media = MediaControl(client)
    media.mute(status)
    if status == False:
        print("ses açıldı")
    else:
        print("ses kapatıldı")
def ses(num):
    media = MediaControl(client)
    media.set_volume(num) 
def app(uygulama):
    app = ApplicationControl(client)
    app.list_apps(uygulama)
    app.launch(uygulama)
def geri():
    inp = InputControl(client)
    inp.connect_input()
    inp.back()
    print("Menü geri gelindi.")
def sec():
    inp = InputControl(client)
    inp.connect_input()
    inp.ok()
def sag():
    inp = InputControl(client)
    inp.connect_input()
    inp.right()
def sol():
    inp = InputControl(client)
    inp.connect_input()
    inp.left()
def alt():
    inp = InputControl(client)
    inp.connect_input()
    inp.down()
def ust():
    inp = InputControl(client)
    inp.connect_input()
    inp.up()
def anamenu():
    inp = InputControl(client)
    inp.connect_input()
    inp.home()
def knlup():
    inp = InputControl(client)
    inp.connect_input()
    inp.channel_up()
def knldwn():
    inp = InputControl(client)
    inp.connect_input()
    inp.channel_down()
def dur():
    inp = InputControl(client)
    inp.connect_input()
    inp.pause()
def baslat():
    inp = InputControl(client)
    inp.connect_input()
    inp.play()
def ilerisar():
    inp = InputControl(client)
    inp.connect_input()
    inp.fastforward()
def gerisar():
    inp = InputControl(client)
    inp.connect_input()
    inp.rewind()







    
    