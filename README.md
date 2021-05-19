# DogFeedTimer
i created a code to remind you and let you know what time of the day the dog has been fed. 
great for a house full of people that don't communicate when or if the dog has been fed


>git clone https://github.com/KmartJamJar/DogFeedTimer




1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install git -y
4. sudo apt-get install python3-pip -y
5. sudo pip3 install --upgrade setuptools
6. sudo apt-get install -y python-smbus
7. sudo apt-get install -y i2c-tools
8. sudo raspi-config # enable i2c in interface options
9. in terminal type i2cdetect -y 1 #write down and remember the number shown
10. sudo pip3 install rpi_lcd
11. sudo find /usr/local –name rpi_lcd 2> /dev/null
12. cd /usr/local/lib/python3.7/dist-packages/rpi-lcd
13. sudo nano __init__.py
14. update your lcd address



10. to have the script auto boot on startup type
11. sudo crontab -e
12. select nano
13. scroll down and type @reboot python3 /(location of .py script) then save and exit
