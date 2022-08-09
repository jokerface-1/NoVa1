import subprocess
import opencage.geocoder
import phonenumbers
import time
from phonenumbers import geocoder, carrier, timezone
import pyautogui
import folium
import qrcode
import requests
import colorama
import sys

subprocess.call("clear", shell=True)

print(colorama.Fore.GREEN + """

         ,;;;,               |-------------------|   
        ;;;;;;;              |       NOVA        |
     .- `\, '/_              |  (Road to Hack)   |
   .'   \  (`(_)     	     |	 By-JF-Malwares  |
  / `-,. \ \_/        	     |___________________|	
  \  \/ \ `--`           
   \  \  \                 	        
    / /| |                	        
   /_/ |_|			                
  ( _\ ( _\ 	     		        	
  ---------------------------------------------------------		
                                    """)


def indent():
    print(colorama.Fore.RED+"""
			                    NOTE :
    		You want to gather information about phone number random location means,
    		you must have account opencage website link: https://opencagedata.com/
    		and you need internet connection to access all features of tool
                			Bye [Do it legally]
    """)

    cc = input(colorama.Fore.CYAN + "Enter country code > ")

    phonenumber = input(colorama.Fore.CYAN + "Enter number > ")

    x = phonenumbers.parse(cc + phonenumber)

    print(colorama.Fore.GREEN + "Number = ", phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.RFC3966))

    print(colorama.Fore.GREEN + "ISP = ", phonenumbers.carrier.name_for_valid_number(x, "en"))

    print(colorama.Fore.GREEN + "Time zone of Number= ", phonenumbers.timezone.time_zones_for_number(x))

    print(colorama.Fore.GREEN + "Geo_code = " + phonenumbers.geocoder.description_for_number(x, "en"))

    ask = int(input(colorama.Fore.CYAN + "you need random location of pone number means press 1 no need means press 2 >"))

    if ask == 1:
        api = input(colorama.Fore.CYAN + "Enter api of opencage >")

        geoCoode = phonenumbers.geocoder.description_for_number(x, "en")
        print(colorama.Fore.GREEN + "Geo_Code = ", geoCoode)
        query = str(geoCoode)

        geo = opencage.geocoder.OpenCageGeocode(api)
        print(geo.geocode(query))
        lot = input(colorama.Fore.CYAN + "How many Lan and long(If many type y or n) > ")

        if lot == "y":
            times = int(input(colorama.Fore.CYAN + "Enter time(less than approximate) > "))

            app = int(input(colorama.Fore.CYAN + "Enter approximate number >"))

            while times <= app:
                lan = float(input(colorama.Fore.CYAN + "Enter latitude >"))

                long = float(input(colorama.Fore.CYAN + "Enter longitude >"))

                fname = input(colorama.Fore.CYAN + "Enter filename(Don't enter same name & only in html file >)")

                cmap = folium.Map(location=[lan, long])
                cmap.save(fname)
                times += 1
        else:
            lan = float(input(colorama.Fore.CYAN + "Enter latitude >"))

            long = float(input(colorama.Fore.CYAN + "Enter longitude >"))

            fname = input(colorama.Fore.CYAN + "Enter filename(Don't enter same name & only in html file >)")

            cmap = folium.Map(location=[lan, long])
            cmap.save(fname)

    else:

        try:
            print(colorama.Fore.GREEN + "OK ^_^ are want to reuse the tool ^_^")
            ak = int(input(colorama.Fore.CYAN + "Want to reuse means press 1 no need means press 2 > "))

            if ak == 1:
                reuse = int(input(colorama.Fore.CYAN + """
        	            	1. Phone No Information Gathering
	
                	    	2. Msg Bombing 

                    		3. Qrcode making(with malicious link)

                       		 4.exit 

                        	ENTER >

                """))

                if reuse == 1:
                    indent()

                elif reuse == 2:
                    bomb()

                elif reuse == 3:
                    qr()

                elif reuse == 4:
                    print(colorama.Fore.BLUE + 		"< EXITING >")
                    sys.exit()

        except Exception as e:
            print(colorama.Fore.RED, e)


def bomb():
    choice2 = int(input(colorama.Fore.CYAN + "Enter 1 for endlessBomb 2 for userDefined Bomb > "))

    if choice2 == 1:
        print(colorama.Fore.RED + " 		>>Note point mouse in msg box where you want to send 3 sec<< ")
        msg = input(colorama.Fore.CYAN + "Enter msg > ")

        while True:
            time.sleep(2)
            pyautogui.typewrite(msg)
            pyautogui.sleep(1)
            pyautogui.press("enter")

    else:
        print(colorama.Fore.RED + " 		>>Note point mouse in msg box where you want to send 3 sec<< ")

        loop = int(input(colorama.Fore.CYAN + "Enter time for loop(less than endloop) > "))

        endloop = int(input(colorama.Fore.CYAN + "Enter end of loop > "))

        msg = input(colorama.Fore.CYAN + "Enter msg > ")

        while loop <= endloop:
            time.sleep(2)
            pyautogui.typewrite(msg)
            pyautogui.sleep(1)
            pyautogui.press("enter")
            print(colorama.Fore.GREEN + " 		< Msg send > ")
            loop += 1

        print(colorama.Fore.GREEN + "		< Success >")

    try:
        print(colorama.Fore.GREEN + "OK ^_^ are want to reuse the tool ^_^")

        ak = int(input(colorama.Fore.CYAN + "Want to reuse means press 1 no need means press 2 > "))

        if ak == 1:

            reuse = int(input(colorama.Fore.CYAN + """
		                1. Phone No Information Gathering

                		2. Msg Bombing 

		                3. Qrcode making(with malicious link)

		                4.exit 

                		Enter >

            """))
            if reuse == 1:
                indent()

            elif reuse == 2:
                bomb()

            elif reuse == 3:
                qr()

            elif reuse == 4:
                print(colorama.Fore.BLUE + "		< EXITING >")
                sys.exit()

    except Exception as e:
        print(colorama.Fore.RED, e)


def qr():
    want = int(input(colorama.Fore.CYAN + "you need many qr means press 1 or don't need means press 2 >"))

    if want == 1:
        ask = int(input(colorama.Fore.CYAN + "same url or different 1 for same 2 for different >"))
        if ask == 1:
            time0 = int(input(colorama.Fore.CYAN + "How many times 1(less number than times 2) >"))

            time1 = int(input(colorama.Fore.CYAN + "How many times 2(greater than time 1) >"))

            url_inp = input(colorama.Fore.CYAN + "Enter your url >")

            while time0 <= time1:
                data = requests.get(url_inp)
                url = data.url
                make = qrcode.make(url)
                name = input(colorama.Fore.CYAN + "Enter file name(with png) >")
                make.save(name)
                time0 += 1

        else:
            time2 = int(input(colorama.Fore.CYAN + "How many times 1(less number than times 2) >"))

            time1 = int(input(colorama.Fore.CYAN + "How many times 2(greater than time 1) >"))

            while time2 <= time1:
                url_inp = input(colorama.Fore.CYAN + "Enter your url >")
                data = requests.get(url_inp)
                url = data.url
                make = qrcode.make(url)
                name = input(colorama.Fore.CYAN + "Enter file name(with png) >")
                make.save(name)
                time2 += 1
    else:
        url_inp = input(colorama.Fore.CYAN + "Enter your url >")
        data = requests.get(url_inp)
        url = data.url
        make = qrcode.make(url)
        name = input(colorama.Fore.CYAN + "Enter file name(with png) >")
        make.save(name)

    try:
        print(colorama.Fore.GREEN + "OK ^_^ are want to reuse the tool ^_^")

        ak = int(input(colorama.Fore.CYAN + "Want to reuse means press 1 no need means press 2 > "))

        if ak == 1:
            reuse = int(input(colorama.Fore.CYAN + """
                		1. Phone No Information Gathering

                		2. Msg Bombing 

		                3. Qrcode making(with malicious link)

		                4.exit 

                		ENTER >

            """))

            if reuse == 1:
                indent()

            elif reuse == 2:
                bomb()

            elif reuse == 3:
                qr()

            elif reuse == 4:
                print(colorama.Fore.BLUE + "		< EXITING >")
                sys.exit()

    except Exception as e:
        print(colorama.Fore.RED, e)


print(colorama.Fore.BLUE + """
		1. Phone No Information Gathering

		2. Msg Bombing 

		3. Qrcode making(with malicious link)

		4. Exit

""")

choice = int(input(colorama.Fore.CYAN + "Enter choice: "))

if choice == 1:
    indent()

elif choice == 2:
    bomb()

elif choice == 3:
    qr()

elif choice == 4:
    print(colorama.Fore.GREEN + "		BYE ^_^")
    sys.exit()
