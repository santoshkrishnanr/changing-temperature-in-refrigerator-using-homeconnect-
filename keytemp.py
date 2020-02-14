from homeconnect import HomeConnect
import webbrowser
import time

client_id = "2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
redirect_uri = "https://localhost/santa"

def print_status(app):
    print(app.name)
    print(app.status)

hc = HomeConnect(client_id, client_secret, redirect_uri)

# open this URL in your web browser
print(hc.get_authurl())
webbrowser.open(hc.get_authurl())

# do magic to enter the id and password and copy the code!!! 

auth_result = input("Please enter the URL redirected to: ")

print(hc.get_token(auth_result))
# list the existing appliances
appliances = hc.get_appliances()
print(appliances)


import keyboard

tem = 4
frez = -24
was_pressed = False
for app in appliances:
    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator",tem)#2-8
    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer",frez)#-24to-16
    while True:
        if keyboard.is_pressed('r'):
            if not was_pressed:
                tem += 1
                print("-Refrigerator temperature",tem)
                if tem in range(2, 9):
                    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator",tem)#2-8
                was_pressed = True

        elif keyboard.is_pressed('t'):
            if not was_pressed:
                tem -= 1
                print("-Refrigerator temperature",tem)
                if tem in range(2, 9):
                    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator",tem)#2-8
                was_pressed = True	
        elif keyboard.is_pressed('f'):
            if not was_pressed:
                frez += 1
                print("-Freezer temperature",frez)
                if frez in range(-24, -15):
                    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer",frez)#-24-16
                was_pressed = True

        elif keyboard.is_pressed('g'):
            if not was_pressed:
                frez -= 1
                print("-freezer temperature",frez)
                if frez in range(-24,-15):
                    app.set_setting("Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer",frez)#-24-16
                was_pressed = True 

        else:
            was_pressed = False
    
