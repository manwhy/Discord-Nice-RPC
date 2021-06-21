"""Nice-DRPC By RexHm
Discord ID: 612122239428722720
Github project repository: https://github.com/Rex-Hm/Discord-Nice-RPC
If you have any questions, suggestions or problems, you can enter this server and comment on your case. https://discord.gg/Ccbau6uPmC"""

print("""Made by RexHm
Discord ID: 612122239428722720
Github project repository: https://github.com/Rex-Hm/Discord-Nice-RPC
If you have any questions, suggestions or problems, you can enter this server and comment on your case. https://discord.gg/Ccbau6uPmC
thanks for using the app!\n""")

print("Starting")
from pypresence import Presence
from webbrowser import open as webopen
from time import time
import json

config = None

try:
    print("Looking for configuration")
    with open("config.json","r",encoding="utf-8") as config:
        print("Configuration located")
        config = json.load(config)
        client_id = config["client_id"]
        state = config["state"]
        details = config["details"]
        large_image = config["large_image"]
        large_text = config["large_text"]
        small_image = config["small_image"]
        small_text = config["small_text"]
        show_time = config["show_time"]
        buttons = config["buttons"]
        if state == None and details != None:
            state = details
            details = None
        if show_time == True:show_time = time()
        else:show_time = None
        
        print("Loading RPC")
        rpc = Presence(client_id)
        
        print("Conecting RPC to Discord...")
        rpc.connect()
        
        print("Applying settings")
        rpc.update(
            state=state,
            details=details,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text,
            start=show_time,
            buttons=buttons
        )
        print("RPC Connected successfully")
        while True:
            rpc.update(
                state=state,
                details=details,
                large_image=large_image,
                large_text=large_text,
                small_image=small_image,
                small_text=small_text,
                start=show_time,
                buttons=buttons
            )
except Exception as e:
    print("\nAn error has occurred, more information will be displayed below.")
    if config == None:
        with open("config.json","w+",encoding="utf-8") as makeconfig:
            preConfig = {
                "client_id" : "INPUT YOUR APP ID",
                "state" : "INPUT YOUR STATE",
                "details" : "INPUT YOUR DETAILS",
                "large_image" : "INPUT THE NAME OF YOUR IMAGE ASSET",
                "large_text" : "INPUT YOUR TEXT FOR THE large_image",
                "small_image" : "INPUT THE NAME OF YOUR IMAGE ASSET",
                "small_text" : "INPUT YOUR TEXT FOR THE small_image",
                "show_time" : "INPUT True/False IF YOU WANT TO SHOW OR NOT YOUR PRESENCE TIME",
                "buttons" : 
                [
                    {
                    "label" : "INPUT THE TEXT OF THE BUTTON",
                    "url" : "INPUT THE URL OF THE BUTTON"
                    }
                ]
            }
            json.dump(preConfig,makeconfig,indent=2,sort_keys=True,ensure_ascii=False,)
        
        print("A config file is missing, it has been added automatically, to configure it read the instructions in the github repository, be sure to do it, once configured reopen the application.")
        
        open_github_repository = input("\nDo you want to open the github repository? (y/n)")
        if "y" in open_github_repository:webopen("https://github.com/Rex-Hm/Discord-Nice-RPC")
        else:pass
        
    else:
        try:
            if e.errno == 104:
                print("Invalid credentials, make sure you have set the client_id correctly")
        except:
            print(e)
            input("\nPress enter to exit.")