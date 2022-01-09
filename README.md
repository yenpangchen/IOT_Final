# IOT_SoapDispenser

## Introduction
This is an **Automatic Soap Dispenser**. The automatic soap dispenser is aimed to spread soap automatically without pressing the bottle. This is archived by preventing the user from gettig contact with the handwash bottle while washing hands. As it has been proven through research, the Corona virus spreads through coming into contact with infected surfaces. Meanwhile, we should encourage people to wash hands frequently.

It's easy to use and need a few steps. The steps are as follows:

1.  You need to send text to the bot and the bot will ask you to put your hand under the camera.

2.  Show your hand. If the device recognize that your five fingers are up, it will pour the soap on your hand.

## Things Used In This Project
### Hardware
- Raspberry Pi 4 *1
- PiCamera *1
- Jumper wires
- Servo motor *1
- Breadboard
- 5V Battery case

### Software
- Python 3.7.3
- Open-Vino
- OpenCV
- Python Telegram Bot
- Pigpiod
- MediaPipe
- gtts
- mpg321


## Circuit Diagram
![](https://i.imgur.com/QBvCgU7.png)

Remember!! Please plug the PiCamera `BEFORE` you turn on your Raspberry Pi!!

Do not put PiCamera on the circuit diagram!

Just plug them in your raspberry pi. 

### Check Your Camera First
Make sure you enable your camera first.

Press the raspberry icon on the top left of the screen -> Preferences -> Raspberry Pi Configuration

![](https://i.imgur.com/iCaCkKr.png)

This link provides information about how to use camera on Raspberry Pi:

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3

Type in the following command to take a still picture and save it to the Desktop:
```
raspistill -o Desktop/image.jpg
```
If you see the picture appear on your screen, it means that your camera is fine.
## How to Control Servo Motor

This link provides information about GPIO pins:

https://pinout.xyz/pinout/pin11_gpio17

These two videos provide information about how to control servo motors:

https://www.youtube.com/watch?v=_fdwE4EznYo&t=682s&ab_channel=GaryExplains  

https://www.youtube.com/watch?v=xHDT4CwjUQE&ab_channel=ExplainingComputers

Note that GPIO ZERO has already installed by default in the Raspberry Pi OS.

Circuit Diagram:
![](https://i.imgur.com/oyFwUKy.png)

Install `pigpio`
If you're working with the rpi3's gpio, the `pigpio` library can be very handy.
```
sudo apt-get install pigpio 
```
Start the `pigpio`
```
sudo pigpiod 
```
Then run your code to control servo motor.

## MediaPipe
### Introduction
In this project, I use mediapipe to achieve hand recognition and finger identification. Let us install mediapipe for the gesture control.

### Install MediaPipe
This has specific packages that work with Raspberry Pi 4 and Raspberry Pi 3, you can install both to your system.
These commands are going to provide us with our MediaPipe Package. Go to Terminal and enter:

```
sudo pip3 install mediapipe-rpi3
sudo pip3 install mediapipe-rpi4
sudo pip3 install gtts
sudo apt install mpg321
```

MediaPipe is able to identify, locate and provide a unique number for each joint on both your hands.
![](https://i.imgur.com/Yy2hJDa.png)

To get more infomation about mediapipe, you can go to

https://mediapipe.dev/

### Hand Recognition and Gesture Control
press the link and download the code.

https://core-electronics.com.au/media/kbase/527/Code-For-Hand-Identification-Media-Pipe-new.zip

After download and unzip the file, please make sure when running the main script that | module.py | is in the same directory.

This is the result of running the script. After you put your hand in front of the picamera, mediapipe will detect how many fingers are up and how many fingers are down.

![](https://i.imgur.com/zMwPQku.png)

## Build Telegram Bot
This video teaches you how to control Raspberry Pi using telegram bot:

https://www.youtube.com/watch?v=rRJ6H5gxaNA&ab_channel=MSDGurukul

In order to create your telegram bot, go to Terminal and enter:
```
pip3 install python-telegram-bot --upgrade
```
1. Download Telegram on your computer,then sign up for Telegram
https://telegram.org/apps
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20200926/20130283oUk4njEXco.png)
2. Use [@BotFather](https://t.me/BotFather) to create new bot accounts and manage your existing bots
![](https://miro.medium.com/max/698/1*oelrrJ132Ta6sp91Xo-xEQ.png)
4. Click these links to learn how to set your telegram bot
- https://ithelp.ithome.com.tw/articles/10245264
- https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81

4. Input your token on the script "**YOUR TOKEN HERE**".

	Notice: You need to keep your token and store it safely.
```
updater = Updater("YOUR TOKEN HERE", use_context=True)
```

5. Run the script
```
python3 telegram_bot.py
```
## Build up your Iot Bartender
1. Make sure that all electronic component can work normally
![](https://i.imgur.com/zCsALGT.png)


3. Set up your circuit diagram first, and make sure that all electronic component has been installed.
![](https://i.imgur.com/rHljPYQ.jpg)


3. Using `camera.py` to scan and decode QR codes with OpenCV
![](https://i.imgur.com/yG46nxj.png)

    To get more infomation, you can go to [An OpenCV barcode and QR code scanner with ZBar](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)

4. Run the script
```
python iotbartender.py
```

## References
a.	iot Bartender
- Smart Bartender
https://www.hackster.io/hackershack/smart-bartender-5c430e
- Pitender
https://hackmd.io/@nI3k8IIMTUuNhfYnYiVKlQ/rklX1RllU
- 原住民調酒
http://winelist.niusnews.com/post/3k2kt84

b.	telegram bot

- telegram bot api
https://core.telegram.org/bots/api
- python-telegram-bot
    
    https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/README.md
- python QR Code generator
https://pypi.org/project/qrcode/
- upload image via PyImgur
    - https://pyimgur.readthedocs.io/en/latest/
    - https://ithelp.ithome.com.tw/articles/10241006

c.	Age Classification
- microsoft azure face api

    https://azure.microsoft.com/zh-tw/services/cognitive-services/face/#features
