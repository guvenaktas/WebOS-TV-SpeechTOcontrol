from ast import Continue, Return
from asyncio import wait_for
from gettext import find
import os
import re
from xmlrpc.client import boolean
import speech_recognition as sr
import googletrans
from googletrans import Translator
import pyttsx3
import webostv


while True:
    wait_for
    language = 'tr'
    r = sr.Recognizer()
    translator = Translator()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Dinliyorum..')
        audio_text = r.listen(source)
        print('İstek İşleniyor','\r\n')
    try:
            text = r.recognize_google(audio_text,language="tr_TR")
            print('İstek Tanıma BASLATILDI ...','\r\n')
            print('İstenen:','\r\n',text,'\r\n')
        #example1 = translator.translate(text)
            textlist= text.split()
            text = text.lower()
            sesup = (bool(re.findall(r'arttır',text)))
            sesdown = (bool(re.findall(r'düşür',text)))
            sesmute = (bool(re.findall(r'kapat',text)))
            sesnmute = (bool(re.findall(r'aç',text)))
            ses = (bool(re.findall(r'seviye',text)))
            gerib = (bool(re.findall(r'geri gel',text)))
            sec = (bool(re.findall(r'seç',text)))
            dty = (bool(re.findall(r'gir',text)))
            sag = (bool(re.findall(r'sağa',text)))
            sol = (bool(re.findall(r'sola',text)))
            alt = (bool(re.findall(r'in',text)))
            ust = (bool(re.findall(r'çık',text)))
            aname = (bool(re.findall(r'ana menü',text)))
            knlup = (bool(re.findall(r'geç',text)))
            knldwn = (bool(re.findall(r'dön',text)))
            dur = (bool(re.findall(r'dur dur',text)))
            baslat = (bool(re.findall(r'devam et',text)))
            ilerisar = (bool(re.findall(r'ileriye',text)))
            gerisar= (bool(re.findall(r'geriye',text)))
            seslevel = (textlist[1])
            print(text)
            if sesup == True:
                webostv.sesac()
                print("Ses bir kademe açıldı.")
            if sesdown == True:
                webostv.seskis()
                print("Ses bir kademe kısıldı.")
            if sesnmute == True or sesmute == True:
                webostv.sesmute(sesmute)
            if ses == True:
                webostv.ses(int(seslevel))
                print("ses seviyesi" , seslevel , "yapıldı")
            if gerib == True:
                webostv.geri()
            if sec == True:
                webostv.sec()
            if dty == True:
                webostv.sec()
            if sag == True:
                webostv.sag()
            if sol == True:
                webostv.sol()
            if alt == True:
                webostv.alt()
            if ust == True:
                webostv.ust()
            if aname == True:
                webostv.anamenu()
            if knlup == True:
                webostv.knlup()
            if knldwn == True:
                webostv.knldwn()
            if dur == True:
                webostv.dur()
            if baslat == True:
                webostv.baslat()
            if ilerisar == True:
                webostv.ilerisar()
            if gerisar == True:
                webostv.gerisar()
            else:
                Continue
    except:
        print('İstek algilanmadi....')
