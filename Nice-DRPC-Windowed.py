import os
import json
import tkinter
from tkinter import ttk
from tkinter.constants import E, END, LEFT, RIGHT, W
from time import time
from pypresence import Presence
from webbrowser import open as webopen

class Colors:
    """Color variables"""
    def __init__(self):
        self.dark_gray = "#28282c"

class App:
    """App Manager"""
    def OnError(self,error):
        self.ErrorWindow = tkinter.Toplevel()
        self.ErrorWindow.title("Nice DRPC - Error")
        self.ErrorWindow.config(bg=Color.dark_gray)
        self.ErrorLabel = tkinter.Label(self.ErrorWindow,text="An error has occurred, more information will be displayed below:\n\n -{0}".format(error),font="google 10 bold",bg=Color.dark_gray).pack(padx=10,pady=10)
        self.ErrorLabel = tkinter.Label(self.ErrorWindow,text="Press X to close the window",font="google 10 bold",bg=Color.dark_gray).pack(padx=10,pady=10)

    def __init__(self):
        self.AppWindow = tkinter.Tk()
        #self.Img_Background = tkinter.PhotoImage(file="Discord-Background.png")
        #label = tkinter.Label(self.window,image=self.Img_Background).place(x=0,y=0,relwidth=1,relheight=1)
        #Miscellaneous
        self.AppWindow.title("Nice DRPC - Select Your Presence")
        self.AppWindow.geometry("400x450")
        self.AppWindow.config(bg=Color.dark_gray)
        self.emptySpace = tkinter.Label(self.AppWindow,bg=Color.dark_gray)
        self.emptySpace.pack(pady=1)
        self.title = tkinter.Label(self.AppWindow,text="Welcome to Nice DRPC",font="google 22 bold",bg=Color.dark_gray)
        self.title.pack()
        self.subtitle = tkinter.Label(self.AppWindow,text="An easy way to set up your Discord Rich Presence",font="google 11",bg=Color.dark_gray)
        self.subtitle.pack()
        self.emptySpace2 = tkinter.Label(self.AppWindow,bg=Color.dark_gray)
        self.emptySpace2.pack(pady=1)
        self.title2 = tkinter.Label(self.AppWindow,text="Select your presence",font="google 20 bold",bg=Color.dark_gray)
        self.title2.pack()
        self.RunningPresenceMessage = tkinter.Label(self.AppWindow,text="",font="google 10 bold",bg=Color.dark_gray)
        self.RunningPresenceMessage.place(x=15,y=400)
        #Presence List
        self.presenceList = ttk.Treeview(self.AppWindow,height=10,)
        self.presenceList.heading("#0",text="Presences")
        self.presenceList.place(x=30,y=170)
        self.RechargeSelectPresenceList()
        #Create Presence Button
        self.CreatePresenceButton = ttk.Button(self.AppWindow, text="New Presence",command=self.CreatePresence,width=15)
        self.CreatePresenceButton.place(x=250,y=170)
        self.EditPresenceButton = ttk.Button(self.AppWindow, text="Edit Presence",command=self.EditPresence,width=15) #Coming soon
        self.EditPresenceButton.place(x=250,y=215)
        self.DeletePresenceButton = ttk.Button(self.AppWindow, text="Delete Presence",command=self.DeletePresenceConfirmWindow,width=15)
        self.DeletePresenceButton.place(x=250,y=260)
        self.StartPresenceButton = ttk.Button(self.AppWindow, text="Start Presence",command=self.StartPresence,width=15)
        self.StartPresenceButton.place(x=250,y=305)
        self.HelpButton = ttk.Button(self.AppWindow,text="Help",command=self.Help,width=15)
        self.HelpButton.place(x=250,y=350)

    def RechargeSelectPresenceList(self):
        i = 0
        #Clean all presences
        presenceListChildrens = self.presenceList.get_children()
        for presenceListed in presenceListChildrens:
            self.presenceList.delete(presenceListed)
        #Load all presences
        for file in os.listdir("./config/presences"):
            if file.endswith(".json"):
                self.presenceList.insert("",END,text=file[:-5])
                i+=1
        self.presenceList.heading("#0",text="Presences ({0})".format(i))

    def CreatePresence(self):
        #Variables
        self.ButtonsList = [None,None]
        #Create Window
        self.CreatePresenceWindow = tkinter.Toplevel()
        self.CreatePresenceWindow.title("Nice DRPC - Create Rich Presence")
        self.CreatePresenceWindow.geometry("500x330")
        self.CreatePresenceWindow.config(bg=Color.dark_gray)
        #Entrys
        self.clientId_Label = tkinter.Label(self.CreatePresenceWindow,text="*Client ID",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=0,column=0)
        self.clientId_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.clientId_Entry.grid(row=1,column=0)
        self.ShowTime_Label = tkinter.Label(self.CreatePresenceWindow,text="Show Time Playing (True/False)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=0,column=1)
        self.ShowTime_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.ShowTime_Entry.grid(row=1,column=1)
        self.state_Label = tkinter.Label(self.CreatePresenceWindow,text="State",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=2,column=0)
        self.state_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.state_Entry.grid(row=3,column=0)
        self.details_Label = tkinter.Label(self.CreatePresenceWindow,text="Details",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=2,column=1)
        self.details_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.details_Entry.grid(row=3,column=1)
        self.largeImage_Label = tkinter.Label(self.CreatePresenceWindow,text="Large Image",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=4,column=0)
        self.largeImage_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.largeImage_Entry.grid(row=5,column=0)
        self.smallImage_Label = tkinter.Label(self.CreatePresenceWindow,text="Small Image (Large Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=4,column=1)
        self.smallImage_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.smallImage_Entry.grid(row=5,column=1)
        self.largeText_Label = tkinter.Label(self.CreatePresenceWindow,text="Large Text (Large Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=6,column=0)
        self.largeText_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.largeText_Entry.grid(row=7,column=0)
        self.smallText_Label = tkinter.Label(self.CreatePresenceWindow,text="Small Text (Small Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=6,column=1)
        self.smallText_Entry = tkinter.Entry(self.CreatePresenceWindow,width=30)
        self.smallText_Entry.grid(row=7,column=1)
        #Buttons
        self.Buttons_Label = tkinter.Button(self.CreatePresenceWindow,text="New Button",command=lambda:self.CreatePresenceButtons(0,self.CreatePresenceWindow),width=20)
        self.Buttons_Label.grid(row=8,column=0,columnspan=1,rowspan=1,padx=10,pady=15)
        self.Buttons2_Label = tkinter.Button(self.CreatePresenceWindow,text="New Button",command=lambda:self.CreatePresenceButtons(1,self.CreatePresenceWindow),width=20)
        self.Buttons2_Label.grid(row=8,column=1,columnspan=1,rowspan=1,padx=10,pady=15)
        #Save presence
        self.nameLabel = tkinter.Label(self.CreatePresenceWindow,text="Save presence as",font="google 10 bold",justify=LEFT,bg=Color.dark_gray).grid(row=11,column=0)
        self.nameEntry = tkinter.Entry(self.CreatePresenceWindow,width=25)
        self.nameEntry.grid(row=12,column=0,columnspan=1,padx=5)
        self.NewPresenceButton = tkinter.Button(self.CreatePresenceWindow,text="Save Presence", command=lambda:self.SavePresence(self.CreatePresenceWindow),width=20).grid(row=12,column=1)

    def CreatePresenceButtons(self,b,window):
        self.CreatePresenceButtonsWindow = tkinter.Toplevel()
        self.CreatePresenceButtonsWindow.config(bg=Color.dark_gray)
        self.CreatePresenceButtonsWindow.title("Nice DRPC - Create Button")
        self.ButtonLabel_Label = tkinter.Label(self.CreatePresenceButtonsWindow,text="Button Text: ",font="google 10",justify=RIGHT,bg=Color.dark_gray)
        self.ButtonLabel_Label.grid(row=0,column=0,pady=5)
        self.ButtonLabel_Entry = tkinter.Entry(self.CreatePresenceButtonsWindow,width=20)
        self.ButtonLabel_Entry.grid(row=0,column=1)
        self.ButtonUrl_Label = tkinter.Label(self.CreatePresenceButtonsWindow,text="Url:",font="google 10",justify=RIGHT,bg=Color.dark_gray)
        self.ButtonUrl_Label.grid(row=1,column=0,pady=5)
        self.ButtonUrl_Entry = tkinter.Entry(self.CreatePresenceButtonsWindow,width=20)
        self.ButtonUrl_Entry.grid(row=1,column=1)
        self.SavePresenceButton_Button = tkinter.Button(self.CreatePresenceButtonsWindow,text="Save Button",command=lambda:self.SavePresenceButtons(b,window))
        self.SavePresenceButton_Button.grid(row=2,column=0,columnspan=2,sticky=W+E)
        
    def SavePresenceButtons(self,b,window):
        Label = self.ButtonLabel_Entry.get()
        Url = self.ButtonUrl_Entry.get()
        UrlHasHttps = "https://" in Url
        if Label == "" or Label == " " or Label == "  ":
            self.OnError("You cannot leave the name of the button empty")
            return
        if Url == "" or Url == " " or Url == "  ":
            self.OnError("You cannot leave the url of the button empty")
            return
        if UrlHasHttps == False:
            self.OnError("The page is not provided with secure transfer protocols, so we cannot allow you to add this url.")
            return

        ButtonData = {"label": Label, "url": Url}
        self.ButtonsList[b]=ButtonData
        self.DeleteCreateButton_AppearDestroyButton(b,window)
        self.CreatePresenceButtonsWindow.destroy()
        print(self.ButtonsList[b])
    
    def DeleteDestroyPresenceButtons(self,b,window):
        self.ButtonsList[b] = None
        print(self.ButtonsList[b])
        self.DeleteDestroyButton_AppearCreateButton(b,window)

    def SavePresence(self,window):
        fileName = self.nameEntry.get()
        ClientID = self.clientId_Entry.get()
        state = self.state_Entry.get()
        details = self.details_Entry.get()
        largeimage = self.largeImage_Entry.get()
        largetext = self.largeText_Entry.get()
        smallimage = self.smallImage_Entry.get()
        smalltext = self.smallText_Entry.get()
        showtime = self.ShowTime_Entry.get().lower()
        buttons = self.ButtonsList
        
        #Error Handler
        if fileName == "":
            self.OnError("It is not defined how to save the presence")
            return
        if " " in fileName:
            self.OnError('There cannot be spaces in the presence name, but you can use "-" or "_"')
            return
        if ClientID == "":
            self.OnError("The Client ID its not defined")
            return
        if " " in ClientID:
            self.OnError("There cannot be spaces in the Client ID, can only have numbers")
            return
        try: 
            ClientID = int(ClientID)
            ClientID = str(ClientID)
        except:
            self.OnError("You can only enter numbers in the Client ID")
            return
        if len(state) == 1:state+=" "
        if len(details) == 1:details+=" "
        if state == "":state = None
        if details == "":details = None
        if state == None and details != None:
            state = details
            details = None
        if "true" in showtime:showtime = True
        else: showtime = False
        if largeimage == "":largeimage = None
        if largetext == "":largetext = None
        if smallimage == "":smallimage = None
        if smalltext == "":smalltext = None

        presenceData = {
            "client_id" : ClientID,
            "state" : state,
            "details" : details,
            "large_image" : largeimage,
            "large_text" : largetext,
            "small_image" : smallimage,
            "small_text" : smalltext,
            "show_time" : showtime,
            "buttons" : buttons,
        }

        with open("./config/presences/{0}.json".format(fileName),"w+",encoding="utf-8") as presenceFile:
            json.dump(presenceData,presenceFile,indent=2,sort_keys=True,ensure_ascii=False)
        self.RechargeSelectPresenceList()
        window.destroy()

    def EditPresence(self):
        selectedPresence = self.presenceList.item(self.presenceList.selection())["text"]
        if selectedPresence == "":
            return
        try:
            with open("./config/presences/{0}.json".format(selectedPresence),"r+",encoding="utf-8") as presenceFile:presenceFile = json.load(presenceFile)
        except Exception as e:
            self.DeleteStopButton_AppearStartButton()
            try:
                if e.errno == 2:
                    self.OnError("Please Select a Rich Presence")
                    return
            except:
                self.OnError(e)
                return
        #Variables
        if presenceFile["show_time"] == True:presenceFile["show_time"] = "true"
        else: presenceFile["show_time"] = "false"
        self.ButtonsList = presenceFile["buttons"]
        #Create Window
        self.EditPresenceWindow = tkinter.Toplevel()
        self.EditPresenceWindow.title("Nice DRPC - Create Rich Presence")
        self.EditPresenceWindow.geometry("500x330")
        self.EditPresenceWindow.config(bg=Color.dark_gray)
        #Entrys
        self.clientId_Label = tkinter.Label(self.EditPresenceWindow,text="*Client ID",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=0,column=0)
        self.clientId_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["client_id"]))
        self.clientId_Entry.grid(row=1,column=0)
        self.ShowTime_Label = tkinter.Label(self.EditPresenceWindow,text="Show Time Playing (True/False)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=0,column=1)
        self.ShowTime_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["show_time"]))
        self.ShowTime_Entry.grid(row=1,column=1)
        self.state_Label = tkinter.Label(self.EditPresenceWindow,text="State",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=2,column=0)
        self.state_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["state"]))
        self.state_Entry.grid(row=3,column=0)
        self.details_Label = tkinter.Label(self.EditPresenceWindow,text="Details",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=2,column=1)
        self.details_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["details"]))
        self.details_Entry.grid(row=3,column=1)
        self.largeImage_Label = tkinter.Label(self.EditPresenceWindow,text="Large Image",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=4,column=0)
        self.largeImage_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["large_image"]))
        self.largeImage_Entry.grid(row=5,column=0)
        self.smallImage_Label = tkinter.Label(self.EditPresenceWindow,text="Small Image (Large Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=4,column=1)
        self.smallImage_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["small_image"]))
        self.smallImage_Entry.grid(row=5,column=1)
        self.largeText_Label = tkinter.Label(self.EditPresenceWindow,text="Large Text (Large Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=6,column=0)
        self.largeText_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["large_text"]))
        self.largeText_Entry.grid(row=7,column=0)
        self.smallText_Label = tkinter.Label(self.EditPresenceWindow,text="Small Text (Small Image is obligatory)",font="google 10",justify=LEFT,bg=Color.dark_gray).grid(row=6,column=1)
        self.smallText_Entry = tkinter.Entry(self.EditPresenceWindow,width=30,textvariable=tkinter.StringVar(self.EditPresenceWindow,presenceFile["small_text"]))
        self.smallText_Entry.grid(row=7,column=1)
        #Buttons
        if presenceFile["buttons"][0] == None:self.Buttons_Label = tkinter.Button(self.EditPresenceWindow,text="New Button",command=lambda:self.CreatePresenceButtons(0,self.EditPresenceWindow),width=20)
        else:self.Buttons_Label = tkinter.Button(self.EditPresenceWindow,text="Destroy Button",command=lambda:self.DeleteDestroyPresenceButtons(0,self.EditPresenceWindow),width=20)
        self.Buttons_Label.grid(row=8,column=0,columnspan=1,rowspan=1,padx=10,pady=15)
        if presenceFile["buttons"][1]== None:self.Buttons2_Label = tkinter.Button(self.EditPresenceWindow,text="New Button",command=lambda:self.CreatePresenceButtons(1,self.EditPresenceWindow),width=20)
        else:self.Buttons2_Label = tkinter.Button(self.EditPresenceWindow,text="Destroy Button",command=lambda:self.DeleteDestroyPresenceButtons(1,self.EditPresenceWindow),width=20)
        self.Buttons2_Label.grid(row=8,column=1,columnspan=1,rowspan=1,padx=10,pady=15)
        #Save presence
        self.nameLabel = tkinter.Label(self.EditPresenceWindow,text="Save presence as",font="google 10 bold",justify=LEFT,bg=Color.dark_gray).grid(row=11,column=0)
        self.nameEntry = tkinter.Entry(self.EditPresenceWindow,width=25,textvariable=tkinter.StringVar(self.EditPresenceWindow,selectedPresence),state="readonly")
        self.nameEntry.grid(row=12,column=0,columnspan=1,padx=5)
        self.NewPresenceButton = tkinter.Button(self.EditPresenceWindow,text="Save Presence", command=lambda:self.SavePresence(self.EditPresenceWindow),width=20).grid(row=12,column=1)
    
    def DeletePresenceConfirmWindow(self):
        #Get the selected element
        selectedPresence = self.presenceList.item(self.presenceList.selection())["text"]
        if selectedPresence == "":
            return
        self.ConfirmWindow = tkinter.Toplevel()
        self.ConfirmWindow.title("Nice DRPC - Waiting for response")
        self.ConfirmWindow.config(bg=Color.dark_gray)
        self.ConfirmLabel = tkinter.Label(self.ConfirmWindow,text='Are you sure you want to delete the presence "{0}"?'.format(selectedPresence),font="google 10 bold",bg=Color.dark_gray).grid(row=0,column=0,columnspan=2)
        self.ConfirmButtonYes = tkinter.Button(self.ConfirmWindow,text="Yes",font="google 10 bold",bg=Color.dark_gray,command=lambda: self.DeletePresence(selectedPresence)).grid(row=1,column=0,sticky=W+E)
        self.ConfirmButtonNo = tkinter.Button(self.ConfirmWindow,text="No",font="google 10 bold",bg=Color.dark_gray,command=lambda: self.ConfirmWindow.destroy()).grid(row=1,column=1,sticky=W+E)
    def DeletePresence(self,selectedPresence):
        try:
            os.remove("./config/presences/{0}.json".format(selectedPresence))
            self.ConfirmWindow.destroy()
        except Exception as e:
            try:
                if e.errno == 2:
                    self.OnError("No Presence Selected to delete or the selected presence was not found")
                    return
            except:
                self.OnError(e)
        self.RechargeSelectPresenceList()
    
    def StartPresence(self):
        self.DeleteStartButton_AppearStopButton()
        #Loading Config
        selectedPresence = self.presenceList.item(self.presenceList.selection())["text"]
        try:
            with open("./config/presences/{0}.json".format(selectedPresence),"r",encoding="utf-8") as presenceFile:presenceFile = json.load(presenceFile)
        except Exception as e:
            self.DeleteStopButton_AppearStartButton()
            try:
                if e.errno == 2:
                    self.OnError("Please Select a Rich Presence")
                    return
            except:
                self.OnError(e)
                return

        try:
            #Getting data
            self.RunningPresenceError = "Error: The file is missing information, create the file again or select another.\nYou can close the app."
            ClientID = presenceFile["client_id"]
            state = presenceFile["state"]
            details = presenceFile["details"]
            largeimage = presenceFile["large_image"]
            largetext = presenceFile["large_text"]
            smallimage = presenceFile["small_image"]
            smalltext = presenceFile["small_text"]
            showtime = presenceFile["show_time"]
            buttons = presenceFile["buttons"]
            #Init Presence
            self.RPC = Presence(ClientID)
            #Connect Presence
            self.RunningPresenceError ="If the connection process is taking time, it is probably because of 1 of these 2 things:\n1. You don't have Discord open\n2. You have run the application repeatedly\n in a short amount of time, this causes Discord\n to not accept RPC requests for a short time."
            self.RPC.connect()
            #Updating Presence
            self.RunningPresenceError = "Parameters error,\n you can get help by clicking the corresponding button on the main menu,\n You can cooperate in troubleshooting by taking a screenshot of this error\n and sending it to the developer of this application.\n Error: {0}"
            if showtime:showtime = time()
            else: showtime = None
            self.RPC.update(
                state=state,
                details=details,
                large_image=largeimage,
                large_text=largetext,
                small_image=smallimage,
                small_text=smalltext,
                start=showtime,
                buttons=buttons
            )
            self.RunningPresenceMessage.config(text="Successfully connected to Discord!\nShowing Rich Presence")

        except Exception as e:
            self.DeleteStopButton_AppearStartButton()
            try:
                if e.errno == 104:
                    self.OnError("Error: Wrong access credentials.\n Try to enter a valid ClientID.\nYou can close the app.")
            except:self.OnError(self.RunningPresenceError.format(e))
    
    def StopPresence(self):
        self.DeleteStopButton_AppearStartButton()
        self.RPC.clear()
        self.RunningPresenceMessage.config(text="")

    def DeleteStartButton_AppearStopButton(self):
        self.StartPresenceButton.destroy()
        self.StopPresenceButton = ttk.Button(self.AppWindow, text="Stop Presence",command=self.StopPresence,width=15)
        self.StopPresenceButton.place(x=250,y=305)
        self.AppWindow.title("Nice DRPC - Running Presence")   
    def DeleteStopButton_AppearStartButton(self):
            self.StopPresenceButton.destroy()
            self.StartPresenceButton = ttk.Button(self.AppWindow, text="Start Presence",command=self.StartPresence,width=15)
            self.StartPresenceButton.place(x=250,y=305)
            self.AppWindow.title("Nice DRPC - Select Your Presence")

    def DeleteCreateButton_AppearDestroyButton(self,b,window):
        if b == 0:
            self.Buttons_Label.destroy()
            self.Buttons_Label = tkinter.Button(window,text="Destroy Button",command=lambda:self.DeleteDestroyPresenceButtons(0,window),width=20)
            self.Buttons_Label.grid(row=8,column=0,columnspan=1,rowspan=1,padx=10,pady=15)
        if b == 1:
            self.Buttons2_Label.destroy()
            self.Buttons2_Label = tkinter.Button(window,text="Destroy Button",command=lambda:self.DeleteDestroyPresenceButtons(1,window),width=20)
            self.Buttons2_Label.grid(row=8,column=1,columnspan=1,rowspan=1,padx=10,pady=15)
    def DeleteDestroyButton_AppearCreateButton(self,b,window):
        if b == 0:
            self.Buttons_Label.destroy()
            self.Buttons_Label = tkinter.Button(window,text="New Button",command=lambda:self.CreatePresenceButtons(0,window),width=20)
            self.Buttons_Label.grid(row=8,column=0,columnspan=1,rowspan=1,padx=10,pady=15)
        if b == 1:
            self.Buttons2_Label.destroy()
            self.Buttons2_Label = tkinter.Button(window,text="New Button",command=lambda:self.CreatePresenceButtons(1,window),width=20)
            self.Buttons2_Label.grid(row=8,column=1,columnspan=1,rowspan=1,padx=10,pady=15)


    def Help(self):
        self.HelpWindow = tkinter.Toplevel()
        self.HelpWindow.title("Nice DRPC - Help")
        self.HelpWindow.config(bg=Color.dark_gray)
        self.Info_label = tkinter.Label(self.HelpWindow,text="Thanks for using the app.\nIf you need guidance on how to use the app you can visit the github repository and read the guide I wrote\nIf you have any problems / questions / suggestions you can visit my Discord server and talk to me there!\nRemember that the application is under development, so it is possible to find errors, try to avoid causing them and notify me\nNice-DRPC v2 Windows 10 Build",font="google 10 italic",bg=Color.dark_gray).grid(row=0,column=0,columnspan=2)
        self.Button1 = tkinter.Button(self.HelpWindow,text="Open Github",font="google 10 bold",bg=Color.dark_gray,command=lambda:webopen("https://github.com/Rex-Hm/Discord-Nice-RPC")).grid(row=1,column=0,sticky=W+E)
        self.Button1 = tkinter.Button(self.HelpWindow,text="Discord Server",font="google 10 bold",bg=Color.dark_gray,command=lambda:webopen("https://discord.gg/Ccbau6uPmC")).grid(row=1,column=1,sticky=W+E)

if __name__ == "__main__":
    #Create necessary folders
    if os.path.exists("./config") == False:
        os.system("mkdir ./config")
    if os.path.exists("./config/presences") == False:
        os.system("mkdir ./config/presences")
    #Init Colors
    Color = Colors()
    #Init GUI
    GUI_App = App()
    GUI_App.AppWindow.mainloop()