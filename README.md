# A easy Discord Rich Presence
 A nice Rich Presence for Discord that you can customize as you like. 
 only available for Windows 10, I'm not sure if it will ever have support for Windows 7, at least not the version with Python. 
 If you are a Linux user you can directly download the source code and run it
 

# Configuring application
To configure our RPC we must modify the config.json file located in the same folder as the application,
to open it we will right click and click on the "open with" option,
this will show us the list of our applications,
we will select an editor from text of our preference (Word, Excel, powerpoint and the like do not count, preferably use the default text editor of your system)
Once our file is open, you will see that there are different boxes where you will be asked to enter certain data,
now we will proceed to explain how to configure each one.


>__CLIENT_ID__

"client_id" is the box where we must enter the ID of our application.

client_id Example: "client_id": "0000000000000"

If you have no idea how to get that ID or how to have an "application" here we will leave you a little explanation.
You must first go to the Discord developer page and log in.

https://discord.com/developers/applications

After logging in, you will click on the "New application" button, and give it a name, (The name of our application will be the title of our RPC)
We already have our application!
Once you have the application ready, you can access the "application ID", copy that number and save it in client_id, as shown in the previous example, between quotes.

>__STATE AND DETAILS__

"state" is the box where the subtitle of our RPC will be saved, in case of also having the "details" box filled, state will be located below details, as if it were a description.

state Example: "state" : "Hi"

details Example: "details" : "Hello"

>__LARGE_IMAGE__

"large_image" will be our main RPC image, to add an image to our RPC we must first go to the configuration of our application, enter the "Rich Presence"> "Art Assets" section and add our image, after adding the image we will have to fill "large_image" with the name of the image that we want to appear.
Example: We have added an image called "MyPresenceImage" in the "Art Assets" in "large_image" we will proceed to put something like this:

"large_image" : "MyPresenceImage"

>__LARGE_TEXT__

"large_text" is a box where we must enter the text that we want to show when we hover the mouse over our "large_image".

large_text Example: "large_text" : "Nice"

>__SMALL_IMAGE__

"small_image" works in a similar way to "large_image", it is a small image displayed in the shape of a circle on the lower side of "large_image", here you must place the name of some previously added Art Assets as with "large_image", how it works is the same.

small_image Example: "small_image" : "MyPresenceImage"

>__SMALL_TEXT__

It works in the same way as "large_text" here you must enter the text that you want to show when hovering the mouse over the "small_image"

small_text Example: "small_text" : "Nice Small"

>__SHOW_TIME__

This box must be marked with true or false depending on whether or not we want to show how long we have been running the RPC.

show_time Example: "show_time" : true

show_time Example2: "show_time" : false

>__BUTTONS__

This configuration will allow us to add various buttons linked to pages in our rich presence, this is a little more complicated to configure.
first we will have to open and close some brackets like this \[]

then inside we will open and close some keys like this: \[{}]

Inside the keys we will add 2 parameters separated by commas, one will be "label" where we will save the text of the button and another "url" where we will save the link of the page of our button, we must configure it to be something like this:

\[{"label": "My Button", "url": "https://discord.com"}]

With this we will have a button, to add multiple buttons we will have to open other keys within the same brackets, separating the keys from the previous button in such a way that it looks something like this:

\[{"label": "My Button", "url": "https://discord.com"}, {"label": "My Button 2", "url": "https://discord.com"}]

# Extra Notes:

any text must have a minimum of 2 characters (2 spaces do not count)

If you want to not show any parameter such as "large_image", just replace the content with null, something like this:
"large_image": null

When you write a text you must put it in quotes, the terms true, false and null should not be enclosed in quotes.

Then I will leave an example of RPC configuration in case it is not clear yet how to configure the parameters.


	{
			"buttons": [
					{
							"label": "Discord Page",
							"url": "https://discord.com"
					}
			],
			"client_id": "000000000000000000",
			"details": None,
			"large_image": "MyPresenceImage",
			"large_text": "This is my RPC image",
			"show_time": false,
			"small_image": null,
			"small_text": null,
			"state": "Nice"
	}



> By RexHm
>
> Discord ID: 612122239428722720

> report bugs or leave your suggestions here: https://discord.gg/Ccbau6uPmC
