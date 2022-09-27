# boring
import os
import json
cur_path = os.path.dirname(__file__)
recipients = []
channels = []
recipientsTags = []
indexFile = open("messages/index.json", "r")
indexFileLines = indexFile.read()
indexJSON = json.loads(indexFileLines)
indexFile.close()
print("WARNING: YOU ARE WORKING WITH VERY SENSITIVE DATA. IF YOU HAVE NOT DOWNLOADED THIS FROM THE OFFICIAL GITHUB REPOSITORY, DELETE THIS SOFTWARE RIGHT NOW OR RISK YOUR INORMATION BEING STOLEN.")
print("THE ONLY OFFICIAL DOWNLOAD IS AT https://github.com/AZthemute/discord-dm-list/")
input("If you understand, press enter to continue.")

# get list of recipients and channels
for dir in os.listdir("messages"):
    channelFilePath = dir + "\channel.json"
    try: channelFile = open("messages\\" + channelFilePath, "r")
    except FileNotFoundError: continue
    channelFileLines = channelFile.read()
    channelJSON = json.loads(channelFileLines)
    if channelJSON["type"] != 1:
        continue
    recipients.append(channelJSON["recipients"][0])
    channels.append(channelJSON["id"])

# correlate channel IDs with index.json to get usernames and tags of recipients
for channelID in channels:
    recipientTag = indexJSON[channelID]
    recipientsTags.append(recipientTag[20:])

# output as file
with open("dm-list.txt", "w", encoding="utf-8") as o:
    o.write("First is the username + tag, second is the user's ID, third is the channel ID.\nYou can look up the user ID using websites such as https://discord.id if the user's changed their username.\nList of all your Discord DMs:\n\n")
    for i in range(0, len(recipients)):
        o.write(f"{recipientsTags[i]}   {recipients[i]}   {channels[i]}\n")

print("The file has been output as dm-list.txt\n\nThanks for using this software!")
