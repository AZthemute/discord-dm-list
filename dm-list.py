# boring
import os
import json
from tkinter import filedialog
import time
recipients = []
channels = []
recipientsTags = []
dmlistPath = None
print("WARNING: YOU ARE WORKING WITH VERY SENSITIVE DATA. IF YOU HAVE NOT DOWNLOADED THIS FROM THE OFFICIAL GITHUB REPOSITORY, DELETE THIS PROGRAM RIGHT NOW OR RISK YOUR INORMATION BEING STOLEN.")
print("THE ONLY OFFICIAL DOWNLOAD IS AT https://github.com/AZthemute/discord-dm-list")
input("If you understand, press enter to continue.")

# ask for folder
os.system("cls")
print("Please select the directory of your Discord data package.")
#time.sleep(2.5)
filePath = filedialog.askdirectory()
# lazy check to see if it's valid
if not(os.path.isdir("messages")):
    print("This is an invalid Discord data package. Please download your data from Discord again or extract the package.zip if you still have it.")
    exit()
print("Working...")

# read index file
indexFile = open("./messages/index.json", "r")
indexFileLines = indexFile.read()
indexJSON = json.loads(indexFileLines)
indexFile.close()

# need ID of user, fuck discord
userFile = open("./account/user.json", "r")
userFileLines = userFile.read()
userFileJSON = json.loads(userFileLines)
userFile.close()
userID = userFileJSON["id"]

# get list of recipients and channels
for dir in os.listdir("messages"):
    channelFilePath = dir + "\channel.json"
    try: channelFile = open("messages\\" + channelFilePath, "r")
    except FileNotFoundError: continue
    channelFileLines = channelFile.read()
    channelJSON = json.loads(channelFileLines)
    # 1 is a dm
    if channelJSON["type"] != 1:
        continue
    # fuck discord
    if channelJSON["recipients"][1] == userID:
        recipients.append(channelJSON["recipients"][0])
    else:
        recipients.append(channelJSON["recipients"][1])
    channels.append(channelJSON["id"])

# correlate channel IDs with index.json to get usernames and tags of recipients
for channelID in channels:
    recipientTag = indexJSON[channelID]
    recipientsTags.append(recipientTag[20:])

# ask user where to save
if dmlistPath is None:
    print("Please select where to save the DM list file.")
    #time.sleep(2.5)
    dmlistPath = filedialog.asksaveasfilename(initialfile="dm-list.txt", defaultextension="txt")
    print(f"Saved to {dmlistPath}")

# output as file
with open(dmlistPath, "w", encoding="utf-8") as dmlistFile:
    dmlistFile.write("First is the username + tag, second is the user's ID, third is the channel ID.\nYou can look up the user ID using websites such as https://discord.id if the user's changed their username.\nList of all your Discord DMs:\n\n")
    for i in range(0, len(recipients)):
        dmlistFile.write(f"{recipientsTags[i]}   {recipients[i]}   {channels[i]}\n")

print(f"Opening {dmlistPath}")
os.startfile(dmlistPath)
input("Thanks for using this program! Press enter to exit...")
