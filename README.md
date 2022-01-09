# IOT_SoapDispenser

## Auto Soap Dispenser

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
![](https://i.imgur.com/Hgu1tza.png)

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
1. Download Telegram on your computer or on your mobile phone, then sign up for Telegram
https://telegram.org/apps
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20200926/20130283oUk4njEXco.png)
2. Use [@BotFather](https://t.me/BotFather) to create new bot accounts and manage your existing bots
![](https://miro.medium.com/max/698/1*oelrrJ132Ta6sp91Xo-xEQ.png)
3. Click these links to learn how to set your telegram bot
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

## References
a.	MediaPipe

https://core-electronics.com.au/tutorials/hand-identification-raspberry-pi.html#Down

https://www.youtube.com/watch?v=a7B5EZVHHkw&ab_channel=CoreElectronics

https://www.youtube.com/watch?v=EgjwKM3KzGU&ab_channel=NicholasRenotte

b.	telegram bot

https://github.com/chung-coder/Iot-bartender

https://www.youtube.com/watch?v=rRJ6H5gxaNA&ab_channel=MSDGurukul

https://ithelp.ithome.com.tw/articles/10245264

https://hackmd.io/@truckski/HkgaMUc24?type=view#Python-Telegram-Bot-%E6%95%99%E5%AD%B8-by-%E9%99%B3%E9%81%94%E4%BB%81

c.	Automatic Soap Dispenser 

https://www.hackster.io/FANUEL_CONRAD/automatic-soap-dispenser-75abd6

https://www.hackster.io/aakash11/automatic-hand-sanitizer-using-arduino-2924ad

https://www.hackster.io/iasonas-christoulakis/hand-sanitizer-bfbb5a

d.	Servo Motors

https://www.youtube.com/watch?v=_fdwE4EznYo&t=682s&ab_channel=GaryExplains

https://www.youtube.com/watch?v=xHDT4CwjUQE&ab_channel=ExplainingComputers



