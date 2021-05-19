# DogFeedTimer
i created a code to remind you and let you know what time of the day the dog has been fed. 
great for a house full of people that don't communicate when or if the dog has been fed


>git clone https://github.com/KmartJamJar/DogFeedTimer




1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt install python3 idle3
4. sudo apt-get install i2c-tools
5. sudo raspi-config # enable i2c in interface options
6. in terminal type i2cdetect -y 1 #write down and remember the number shown
7. sudo pip3 install rpi_lcd
8. sudo find /usr/local-name rpi_lcd 2> /dev/null
9. sd /usr/local/lib/python3.7/dist-packages/rpi-lcd
10. update your lcd address



10. to have the script auto boot on startup type
11. sudo crontab -e
12. select nano
13. scroll down and type @reboot python3 /(location of .py script) then save and exit
