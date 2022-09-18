import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import subprocess
import os
import cv2
import random
from requests import get
import smtplib
import psutil
import instaloader
import pyautogui
import PyPDF2
from PIL import ImageGrab
import streamlit as st
import wave
import numpy as np 
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from state import state
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import code

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 


    
def run():
    Intro()
def take_Command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            listener.pause_threshold = 1
            voice = listener.listen(source,timeout=4,phrase_time_limit=7)
            print("Recognizing...")
            command = listener.recognize_google(voice,language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis','')
        return command
    except:
        return 'None'

def run_jarvis():
    wish()
    talk('Welcome to the assistant! How may I help you?')
    while True:
        command = take_Command()
        print(command)
        if ('play a song' in command) or ('youtube' in command) or ("download a song" in command) or ("download song" in command) :
            yt(command)
        elif 'time' in command :
            Clock_time(command)
        elif ("today" in command):
            day = Cal_day()
            talk("Today is "+day)
        elif ("meeting" in command):
            talk("Ok sir opening meeet")
            webbrowser.open("https://google.meet/")
        elif ('facebook' in command) or ('whatsapp' in command) or ('instagram' in command) or ('twitter' in command) or ('discord' in command) or ('social media' in command):
            social(command)
        elif ('hotstar' in command) or ('prime' in command) or ('netflix' in command):
            OTT(command)
        elif ('online classes'in command):
            OnlineClasses(command)
        elif ('open teams'in command) or ('open stream'in command) or ('open sharepoint'in command) or('open outlook'in command)or('open amrita portal'in command)or('open octave'in command):
            college(command)
        elif ('wikipedia' in command) or ('what is meant by' in command) or ('tell me about' in command) or ('who the heck is' in command):
            B_S(command)
        elif ('open google'in command) or ('open edge'in command) :
            brows(command)
        elif ('open gmail'in command) or('open maps'in command) or('open calender'in command) or('open documents'in command )or('open spredsheet'in command) or('open images'in command) or('open drive'in command) or('open news' in command):
            Google_Apps(command)
        elif ('open github'in command) or ('open gitlab'in command) :
            open_source(command)
        elif ('slides'in command) or ('canva'in command) or ('figma'in command) or ('photoshop'in command) or ('illustrator'in command) or ('adobe'in command):
            edit(command)
        elif ('open calculator'in command) or ('open notepad'in command) or ('open paint'in command) or ('open online classes'in command) or ('open discord'in command) or ('open ltspice'in command) or ('open editor'in command) or ('open spotify'in command) or ('open steam'in command) or ('open media player'in command):
            OpenApp(command)
        elif ('close calculator'in command) or ('close notepad'in command) or ('close paint'in command) or ('close discord'in command) or ('close ltspice'in command) or ('close editor'in command) or ('close spotify'in command) or ('close steam'in command) or ('close media player'in command):
            CloseApp(command)
        elif ('flipkart'in command) or ('amazon'in command) :
            shopping(command)
        elif ('where i am' in command) or ('where we are' in command):
            locaiton()
        elif ('command prompt'in command) :
            talk('Opening command prompt')
            os.system('start cmd')
        elif ('instagram profile' in command) or("profile on instagram" in command):
            Instagram_Pro()
        elif ('take screenshot' in command)or ('screenshot' in command) or("take a screenshot" in command):
            scshot()
        elif ("read pdf" in command) or ("pdf" in command):
            pdf_reader()
        elif ("volume up" in command) or ("increase volume" in command):
            pyautogui.press("volumeup")
            talk('volume increased')
        elif ("volume down" in command) or ("decrease volume" in command):
            pyautogui.press("volumedown")
            talk('volume decreased')

        elif ("volume mute" in command) or ("mute the sound" in command) :
            pyautogui.press("volumemute")
            talk('volume muted')
        elif("search on"in command):
            searchon(command)

        elif ('web cam'in command) or ('webcam'in command) or ('camera'in command):
            webCam()
        elif 'music' in command:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        elif 'ip address' in command:
            ip = get('https://api.ipify.org').text
            print(f"your IP address is {ip}")
            talk(f"your IP address is {ip}")

        elif 'send email' in command:
            verifyMail()

        elif "internet speed" in command:
            InternetSpeed()
        elif ("goodbye" in command) or ("get lost" in command) or ('quit' in command) or ('exit' in command):
            talk("Thanks for using me, have a good day")
            running = False
            sys.exit()

        elif ('system condition' in command) or ('condition of the system' in command):
            talk("checking the system condition")
            condition()

        elif ('tell me news' in command) or ("the news" in command) or ("todays news" in command):
            talk("Please wait boss, featching the latest news")
            news()


def Intro():
    while True:
        permission = take_Command()
        print(permission)
        if ("wake up" in permission) or ("get up" in permission) or("hello there"in permission):
            run_jarvis()
        elif ("goodbye" in permission) or ("get lost" in permission):
            talk("Thanks for using me boss, have a good day")
            running = False
            sys.exit()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = Cal_day()
    print(t)
    if (hour>=0) and (hour <=12) and ('AM' in t):
        talk(f'Good morning boss, its {day} and the time is {t}')
    elif (hour >= 12) and (hour <= 16) and ('PM' in t):
        talk(f"good afternoon boss, its {day} and the time is {t}")
    else:
        talk(f"good evening boss, its {day} and the time is {t}")

def temperature():
    IP_Address = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data['city']
    search = f"temperature in {city}"
    url_1 = f"https://www.google.com/search?q={search}"
    r = get(url_1)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    talk(f"current {search} is {temp}")

def webCam():
    talk('Opening camera')
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('web camera',img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



def InternetSpeed():
    talk("Wait a few seconds boss, checking your internet speed")
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl/(1000000)
    up = st.upload()
    up = up/(1000000)
    print(dl,up)
    talk(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

def comum(command):
    print(command)
    if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
        talk("Hello boss what can I help for u")
    else :
        No_result_found()

def social(command):
    print(command)
    if 'facebook' in command:
        talk('opening your facebook')
        webbrowser.open('https://www.facebook.com/')
    elif 'whatsapp' in command:
        talk('opening your whatsapp')
        webbrowser.open('https://web.whatsapp.com/')
    elif 'instagram' in command:
        talk('opening your instagram')
        webbrowser.open('https://www.instagram.com/')
    elif 'twitter' in command:
        talk('opening your twitter')
        webbrowser.open('https://twitter.com/')
    elif 'discord' in command:
        talk('opening your discord')
        webbrowser.open('https://discord.com/channels/@me')
    elif 'youtube' in command:
        talk('opening your youtube')
        webbrowser.open('https://www.youtube.com/')
    elif 'github' in command:
        talk('opening your github')
        webbrowser.open('https://www.github.com')
    elif 'linkedin' in command:
        talk('opening your linkedin')
        webbrowser.open('https://www.linkedin.com')
    elif 'gmail' in command:
        talk('opening your gmail')
        webbrowser.open('https://mail.google.com/mail/u/0/inbox')
    elif 'outlook' in command:
        talk('opening your outlook')
        webbrowser.open('https://outlook.live.com/mail/inbox')
    elif 'reddit' in command:
        talk('opening your reddit')
        webbrowser.open('https://www.reddit.com/')
    elif 'tiktok' in command:
        talk('opening your tiktok')
        webbrowser.open('https://www.tiktok.com/')
    elif 'snapchat' in command:
        talk('opening your snapchat')
        webbrowser.open('https://www.snapchat.com/')
    elif 'pinterest' in command:
        talk('opening your pinterest')
        webbrowser.open('https://www.pinterest.com/')
    elif 'quora' in command:
        talk('opening your quora')
        webbrowser.open('https://www.quora.com/')
    elif 'stackoverflow' in command:
        talk('opening your stackoverflow')
        webbrowser.open('https://stackoverflow.com/')
    elif 'medium' in command:
        talk('opening your medium')
        webbrowser.open('https://medium.com/')
    elif 'codechef' in command:
        talk('opening your codechef')
        webbrowser.open('https://www.codechef.com/')
    elif 'codeforces' in command:
        talk('opening your codeforces')
        webbrowser.open('https://codeforces.com/')
    elif 'hackerrank' in command:
        talk('opening your hackerrank')
        webbrowser.open('https://www.hackerrank.com/')
    elif 'hackerearth' in command:
        talk('opening your hackerearth')
        webbrowser.open('https://www.hackerearth.com/')
    elif 'leetcode' in command:
        talk('opening your leetcode')
        webbrowser.open('https://leetcode.com/')
    elif 'geeksforgeeks' in command:
        talk('opening your geeksforgeeks')
        webbrowser.open('https://www.geeksforgeeks.org/')
    elif 'spotify' in command:
        talk('opening your spotify')
        webbrowser.open('https://open.spotify.com/')
    elif 'netflix' in command:
        talk('opening your netflix')
        webbrowser.open('https://www.netflix.com/')
    elif 'primevideo' in command:
        talk('opening your primevideo')
        webbrowser.open('https://www.primevideo.com/')
    elif 'hotstar' in command:
        talk('opening your hotstar')
        webbrowser.open('https://www.hotstar.com/')
    elif 'disneyplus' in command:
        talk('opening your disneyplus')
        webbrowser.open('https://www.disneyplus.com/')
    elif 'hulu' in command:
        talk('opening your hulu')
        webbrowser.open('https://www.hulu.com/')
    elif 'amazon' in command:
        talk('opening your amazon')
        webbrowser.open('https://www.amazon.com/')
    elif 'flipkart' in command:
        talk('opening your flipkart')
        webbrowser.open('https://www.flipkart.com/')
    elif 'myntra' in command:
        talk('opening your myntra')
        webbrowser.open('https://www.myntra.com/')
    elif 'snapdeal' in command:
        talk('opening your snapdeal')
        webbrowser.open('https://www.snapdeal.com/')
    elif 'shopclues' in command:
        talk('opening your shopclues')
        webbrowser.open('https://www.shopclues.com/')
    elif 'ebay' in command:
        talk('opening your ebay')
        webbrowser.open('https://www.ebay.com/')
    elif 'paytm' in command:
        talk('opening your paytm')
        webbrowser.open('https://paytm.com/')
    elif 'phonepe' in command:
        talk('opening your phonepe')
        webbrowser.open('https://www.phonepe.com/')
    elif 'googlepay' in command:
        talk('opening your googlepay')
        webbrowser.open('https://pay.google.com/intl/en_in/about/')
    elif 'amazonpay' in command:
        talk('opening your amazonpay')
        webbrowser.open('https://www.amazon.in/gp/help/customer/display.html?nodeId=202127010')
    else :
        No_result_found()

def Clock_time(command):
    print(command)
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk("Current time is "+time)

def Cal_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)

    return day_of_the_week

def shedule():
    day = Cal_day().lower()
    talk("Boss today's shedule is")
    Week = {"monday" : "Boss from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
    "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
    "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
    "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
    "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
    "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
    "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
    if day in Week.keys():
        talk(Week[day])

def college(command):
    print(command)
    if 'teams' in command:
        talk('opening your microsoft teams')
        webbrowser.open('https://teams.microsoft.com/')
    elif 'stream' in command:
        talk('opening your microsoft stream')
        webbrowser.open('https://web.microsoftstream.com/')
    elif 'outlook' in command:
        talk('opening your microsoft school outlook')
        webbrowser.open('https://outlook.office.com/mail/')
    elif 'octave' in command:
        talk('opening Octave online')
        webbrowser.open('https://octave-online.net/')
    else :
        No_result_found()

def OnlineClasses(command):
    print(command)
    if("java" in command):
        talk('opening meet')
        webbrowser.open("https://google.meet/java")
    elif("mechanics" in command):
        talk('opening mechanics class in meet')
        webbrowser.open("https://google.meet/mechanics")
    elif 'online classes' in command:
        talk('opening your google meet')
        webbrowser.open('https://google.meet/')

def B_S(command):
    print(command)
    try:
        if ('wikipedia' in command):
            target1 = command.replace('for','')
            target1 = command.replace('search','')
            target1 = target1.replace('wikipedia','')
            target1 = target1.replace('on','')
        elif('what is meant by' in command):
            target1 = command.replace("what is meant by"," ")
        elif('tell me about' in command):
            target1 = command.replace("tell me about"," ")
        elif('who the heck is' in command):
            target1 = command.replace("who the heck is"," ")
        print("searching....")
        info = wikipedia.summary(target1,5)
        print(info)
        talk("according to wikipedia "+info)
    except :
        No_result_found()

def brows(command):
    print(command)
    if 'google' in command:
        talk("Boss, what should I search on google..")
        S = take_Command()
        webbrowser.open(f"{S}")
    elif 'edge' in command:
        talk('opening your Miscrosoft edge')
        os.startfile('..\\..\\MicrosoftEdge.exe')
    else :
        No_result_found()

def Google_Apps(command):
    print(command)
    if 'gmail' in command:
        talk('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')
    elif 'maps' in command:
        talk('opening google maps')
        webbrowser.open('https://www.google.co.in/maps/')
    elif 'news' in command:
        talk('opening google news')
        webbrowser.open('https://news.google.com/')
    elif 'calender' in command:
        talk('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')
    elif 'photos' in command:
        talk('opening your google photos')
        webbrowser.open('https://photos.google.com/')
    elif 'documents' in command:
        talk('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')
    elif 'spreadsheet' in command:
        talk('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')
    else :
        No_result_found()

def yt(command):
    print(command)
    if 'play' in command:
        talk("Boss can you please say the name of the song")
        song = take_Command()
        if "play" in song:
            song = song.replace("play","")
        talk('playing '+song)
        print(f'playing {song}')
        pywhatkit.playonyt(song)
        print('playing')
    elif "download" in command:
        talk("Boss please enter the youtube video link which you want to download")
        link = input("Enter the youtube video link: ")
        yt=YouTube(link)
        yt.streams.get_highest_resolution().download()
        talk(f"Boss downloaded {yt.title} from the link you given into the main folder")
    elif 'youtube' in command:
        talk('opening your youtube')
        webbrowser.open('https://www.youtube.com/')
    else :
        No_result_found()

def open_source(command):
    print(command)
    if 'github' in command:
        talk('opening your github')
        webbrowser.open('https://github.com/BolisettySujith')
    elif 'gitlab' in command:
        talk('opening your gitlab')
        webbrowser.open('https://gitlab.com/-/profile')
    else :
        No_result_found()

def edit(command):
    print(command)
    if 'slides' in command:
        talk('opening your google slides')
        webbrowser.open('https://docs.google.com/presentation/')
    elif 'canva' in command:
        talk('opening your canva')
        webbrowser.open('https://www.canva.com/')
    else :
        No_result_found()

def OTT(command):
    print(command)
    if 'hotstar' in command:
        talk('opening your disney plus hotstar')
        webbrowser.open('https://www.hotstar.com/in')
    elif 'prime' in command:
        talk('opening your amazon prime videos')
        webbrowser.open('https://www.primevideo.com/')
    elif 'netflix' in command:
        talk('opening Netflix videos')
        webbrowser.open('https://www.netflix.com/')
    elif 'zee5' in command:
        talk('opening your zee5')
        webbrowser.open('https://www.zee5.com/')
    elif 'sonyliv' in command:
        talk('opening your sonyliv')
        webbrowser.open('https://www.sonyliv.com/')
    elif 'voot' in command:
        talk('opening your voot')
        webbrowser.open('https://www.voot.com/')
    elif 'altbalaji' in command:
        talk('opening your altbalaji')
        webbrowser.open('https://www.altbalaji.com/')
    elif 'mxplayer' in command:
        talk('opening your mxplayer')
        webbrowser.open('https://www.mxplayer.in/')
    else :
        No_result_found()

def OpenApp(command):
    print(command)
    if ('calculator'in command) :
        talk('Opening calculator')
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif ('paint'in command) :
        talk('Opening msPaint')
        os.startfile('c:\\Windows\\System32\\mspaint.exe')
    elif ('notepad'in command) :
        talk('Opening notepad')
        os.startfile('c:\\Windows\\System32\\notepad.exe')
    elif ('discord'in command) :
        talk('Opening discord')
        os.startfile('..\\..\\Discord.exe')
    elif ('editor'in command) :
        talk('Opening your Visual studio code')
        os.startfile('..\\..\\Code.exe')
    elif ('online classes'in command) :
        talk('Opening your Microsoft teams')
        webbrowser.open('https://teams.microsoft.com/')
    elif ('spotify'in command) :
        talk('Opening spotify')
        os.startfile('..\\..\\Spotify.exe')
    elif ('lt spice'in command) :
        talk('Opening lt spice')
        os.startfile("..\\..\\XVIIx64.exe")
    elif ('steam'in command) :
        talk('Opening steam')
        os.startfile("..\\..\\steam.exe")
    elif ('media player'in command) :
        talk('Opening VLC media player')
        os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
    else :
        No_result_found()

def CloseApp(command):
    print(command)
    if ('calculator'in command) :
        talk("okay boss, closing caliculator")
        os.system("taskkill /f /im calc.exe")
    elif ('paint'in command) :
        talk("okay boss, closing mspaint")
        os.system("taskkill /f /im mspaint.exe")
    elif ('notepad'in command) :
        talk("okay boss, closing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif ('discord'in command) :
        talk("okay boss, closing discord")
        os.system("taskkill /f /im Discord.exe")
    elif ('editor'in command) :
        talk("okay boss, closing vs code")
        os.system("taskkill /f /im Code.exe")
    elif ('spotify'in command) :
        talk("okay boss, closing spotify")
        os.system("taskkill /f /im Spotify.exe")
    elif ('lt spice'in command) :
        talk("okay boss, closing lt spice")
        os.system("taskkill /f /im XVIIx64.exe")
    elif ('steam'in command) :
        talk("okay boss, closing steam")
        os.system("taskkill /f /im steam.exe")
    elif ('media player'in command) :
        talk("okay boss, closing media player")
        os.system("taskkill /f /im vlc.exe")
    else :
        No_result_found()

def shopping(command):
    print(command)
    if 'flipkart' in command:
        talk('Opening flipkart online shopping website')
        webbrowser.open("https://www.flipkart.com/")
    elif 'amazon' in command:
        talk('Opening amazon online shopping website')
        webbrowser.open("https://www.amazon.in/")
    elif 'myntra' in command:
        talk('Opening myntra online shopping website')
        webbrowser.open("https://www.myntra.com/")
    elif 'snapdeal' in command:
        talk('Opening snapdeal online shopping website')
        webbrowser.open("https://www.snapdeal.com/")
    elif 'paytm' in command:
        talk('Opening paytm online shopping website')
        webbrowser.open("https://paytm.com/")
    elif 'shopclues' in command:
        talk('Opening shopclues online shopping website')
        webbrowser.open("https://www.shopclues.com/")
    elif 'ebay' in command:
        talk('Opening ebay online shopping website')
        webbrowser.open("https://www.ebay.com/")
    elif 'aliexpress' in command:
        talk('Opening aliexpress online shopping website')
        webbrowser.open("https://www.aliexpress.com/")
    elif 'croma' in command:
        talk('Opening croma online shopping website')
        webbrowser.open("https://www.croma.com/")
    elif 'ajio' in command:
        talk('Opening ajio online shopping website')
        webbrowser.open("https://www.ajio.com/")
    elif 'tatacliq' in command:
        talk('Opening tatacliq online shopping website')
        webbrowser.open("https://www.tatacliq.com/")
    elif 'firstcry' in command:
        talk('Opening firstcry online shopping website')
        webbrowser.open("https://www.firstcry.com/")
    elif 'mamaearth' in command:
        talk('Opening mamaearth online shopping website')
        webbrowser.open("https://www.mamaearth.in/")
    elif 'bigbasket' in command:
        talk('Opening bigbasket online shopping website')
        webbrowser.open("https://www.bigbasket.com/")
    elif 'grofers' in command:
        talk('Opening grofers online shopping website')
        webbrowser.open("https://grofers.com/")
    elif 'zomato' in command:
        talk('Opening zomato online shopping website')
        webbrowser.open("https://www.zomato.com/")
    elif 'swiggy' in command:
        talk('Opening swiggy online shopping website')
        webbrowser.open("https://www.swiggy.com/")
    else :
        No_result_found()

def pdf_reader():
    talk("Boss enter the name of the book which you want to read")
    n = input("Enter the book name: ")
    n = n.strip()+".pdf"
    book_n = open(n,'rb')
    pdfReader = PyPDF2.PdfFileReader(book_n)
    pages = pdfReader.numPages
    talk(f"Boss there are total of {pages} in this book")
    talk("please enter the page number Which I nedd to read")
    num = int(input("Enter the page number: "))
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    talk(text)

def silenceTime(command):
    print(command)
    x=0
    if ('10' in command) or ('ten' in command):x=600
    elif '1' in command or ('one' in command):x=60
    elif '2' in command or ('two' in command):x=120
    elif '3' in command or ('three' in command):x=180
    elif '4' in command or ('four' in command):x=240
    elif '5' in command or ('five' in command):x=300
    elif '6' in command or ('six' in command):x=360
    elif '7' in command or ('seven' in command):x=420
    elif '8' in command or ('eight' in command):x=480
    elif '9' in command or ('nine' in command):x=540
    silence(x)

def searchon(command):
    command.replace("search","")
    command.replace("on","")
    if ('google' in command):
        command.replace("google","")
        webbrowser.open("https://www.google.com/search?q="+command)
    elif('spotify' in command):
        command.replace("spotify","")
        webbrowser.open("https://open.spotify.com/search/"+command)
    elif('youtube' in command):
        command.replace("youtube","")
        webbrowser.open("https://www.youtube.com/results?search_query="+command)
    elif('github' in command):
        command.replace("github","")
        webbrowser.open("https://github.com/search?q="+command)
    elif('stackoverflow' in command):
        command.replace("stackoverflow","")
        webbrowser.open("https://stackoverflow.com/search?q="+command)

def silence(k):
    t = k
    s = "Ok boss I will be silent for "+str(t/60)+" minutes"
    talk(s)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    talk("Boss "+str(k/60)+" minutes over")

def verifyMail():
    try:
        talk("what should I say?")
        content = take_Command()
        talk("To whom do u want to send the email?")
        to = take_Command()
        SendEmail(to,content)
        talk("Email has been sent to "+str(to))
    except Exception as e:
        print(e)
        talk("Sorry sir I am not not able to send this email")

def SendEmail(to,content):
    print(content)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("YOUR_MAIL_ID","PASWORD")
    server.sendmail("YOUR_MAIL_ID",to,content)
    server.close()

def locaiton():
    talk("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
        talk(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        talk(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        talk("Sorry boss, due to network issue i am not able to find where we are.")
        pass

def Instagram_Pro():
    talk("Boss please enter the user name of Instagram: ")
    name = input("Enter username here: ")
    webbrowser.open(f"www.instagram.com/{name}")
    time.sleep(5)

def scshot():
    talk("Boss, please tell me the name for this screenshot file")
    name = take_Command()
    talk("Please boss hold the screen for few seconds, I am taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    talk("I am done boss, the screenshot is saved in main folder.")

def news():
    MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=YOUR_NEWS_API_KEY"
    MAIN_PAGE_ = get(MAIN_URL_).json()
    articles = MAIN_PAGE_["articles"]
    headings=[]
    seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
    for ar in articles:
        headings.append(ar['title'])
    for i in range(len(seq)):
        print(f"todays {seq[i]} news is: {headings[i]}")
        talk(f"todays {seq[i]} news is: {headings[i]}")
    talk("Boss I am done, I have read most of the latest news")

def condition():
    usage = str(psutil.cpu_percent())
    talk("CPU is at"+usage+" percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    talk(f"Boss our system have {percentage} percentage Battery")
    if percentage >=75:
        talk(f"Boss we could have enough charging to continue our work")
    elif percentage >=40 and percentage <=75:
        talk(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >=15 and percentage <=30:
        talk(f"Boss we don't have enough power to work, please connect to charging")
    else:
        talk(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

def No_result_found():
    talk('Boss I couldn\'t understand, could you please say it again.')

if st.button('Start the assistant'):
    running = True
    run()
else:
    running = False
