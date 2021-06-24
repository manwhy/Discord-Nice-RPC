# A easy Discord Rich Presence
 A nice Rich Presence for Discord that you can customize as you like. 
 only available for Windows 10 onwards, I'm not sure if it will ever have support for Windows 7, at least not the version with Python. 
 
 Project discontinued, maybe rewrite in another language soon
 
 # Downloads
 __Windows 10__: Not avaible
 
 __Linux__: https://github.com/Rex-Hm/Discord-Nice-RPC/releases
 
 __Mac__: Not available

# First steps
(Setting up our RPC is now much easier thanks to the GUI integrated in v2!)
First of all, to have a custom RPC you need to have a "Discord application,"
Yes, it sounds complicated, but it is not, do not worry, creating your application will be very simple, then I will leave a series of steps that you must follow to successfully create a Discord application.

### 1. Enter the Discord developer page:

https://discord.com/developers/applications

When you enter the page you will find an interface like this, you must go to the upper right, next to your profile photo and click on "New application"
![ 23_06_21 22:55:31](https://user-images.githubusercontent.com/77251557/123190554-23654180-d476-11eb-83aa-cc520e027414.png)

### 2. Create the Discord aplicacition

Then a box like this will appear asking us to enter a name, which will be the title of our Rich Presence, (We can change the name at any time from the same page)
In this case I will enter "My Presence", you can enter the name you want.
![ 23_06_21 22:57:54](https://user-images.githubusercontent.com/77251557/123190713-73dc9f00-d476-11eb-8c13-8bd20effaff4.png)

### 3. Get ID

Well, once we have the application created we must save its ID, which will help us to connect the rich presence from the application.
To obtain the ID we must select our application and go to the general information section, where within the first labels we will see a call "Application ID", which contains a moderate amount of numbers, we will copy it and once done we can proceed to customize our Rich Presence
![imagen](https://user-images.githubusercontent.com/77251557/123191447-a3d87200-d477-11eb-90cb-c4ba5a80206a.png)

## Configuring RPC from Nice-DRPC

When you enter the application for the first time you will see that you have a list of presences, that's right! You can save your custom RPCs and use them whenever you want in the future! (You can keep an unlimited amount of RPC)
![ 23_06_21 23:12:30](https://user-images.githubusercontent.com/77251557/123192018-7dff9d00-d478-11eb-881b-aaf57fbb10e5.png)

To create our first presence we must give the button located in the upper right part of the screen that says "New presence", this will open a menu that will contain several boxes that we must fill in depending on how we want our Rich Presence to look. 
![ 23_06_21 23:15:47](https://user-images.githubusercontent.com/77251557/123192285-f5cdc780-d478-11eb-8a06-7df015011d53.png)

Do you remember the ID of the app we created earlier? You must put the ID of your application in the first box, this step is mandatory for Rich Presence to work correctly.
Next I will give a brief explanation and demonstration of each frame and its function.

### Client ID

The client ID of our application, allows connection with Discord, it is mandatory

### Show Time Playing

Decide whether to show the time you have been active with Rich Presence, by default it is False

### State

State is the description of our presence, by default it is null

### Details

details becomes the second description of our presence, (although it is located above state)

### Large Image

here will go the name of our asset that contains the large image that we want to show in our rich presence

### Small Image

here will go the name of our asset that contains the small image that we want to show in our rich presence

### Large Text

here will go the text that we want to show when we hover the mouse over the large image, it is mandatory to define the image before

### Small Text

here will go the text that we want to show when we hover the mouse over the small image, it is mandatory to define the image before

### Buttons

We have the possibility of creating 2 buttons for our presence, we must specify the text of the button and the url to which it will take us.

### Save presence as

Here will go the name with which we will save the presence, the text entered here will not influence our rich presence, it is a way of classifying it.

## Add images to Rich Presence

To add an asset we will have to go to the RichPresence> ArtAssets section within our Discord application, we will click on the "add image" button, we will select the assets to upload, and we will give it a name of our choice, since later it will not be possible change the name, (unless you delete the asset and upload it again)
![ 24_06_21 01:20:47](https://user-images.githubusercontent.com/77251557/123202138-6c26f580-d48a-11eb-8d5d-8387e2bf2b6c.png)
Once you have uploaded the asset, you will have to wait a few minutes for discord to finish processing it, and you will be able to use your image for your custom RPC! (To use the image, you must put the name of the asset you want to show in its respective box, Large Image or Small Image)

# Extra Notes

Don't try to open the same window 2 times, example:

> 2 "new presence" windows.

> 2 "new button" windows.

> 2 "edit presence" windows.

this will cause the application to understand that it should ignore the previous window, so it is preferable to avoid it.

Avoid bugs at all costs, and if you run into one it is appreciated if you can share it on my server so I try to find a solution.

Currently this is v2 of the project.

I plan to do another rewrite (v3) solving all the bugs that I have found so far and could not solve, and give better performance.
