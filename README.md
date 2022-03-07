# Kizmeow-NFT-Mint-Progress-Discord-Bot(editing, I'll finish it tommorow, I'm too tired now UwU)


### [中文版](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/%E8%AE%80%E6%88%91.md) | [English Ver](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/README.md)
A Discord bot wrote with Python. Kizmeow let you track mint progress of your NFT project and display them by editing channel name.

If you like this project, please give me star on the upper right corner:)


What can this bot do?
-----------------
Get data from Etherscan and display mint progress by change channel name of voice channel.

![image](https://user-images.githubusercontent.com/80938768/156949496-d08b131e-8702-4045-801a-6a3aa6aab7a2.png)

-------------------------------------------------------------------------------------------------------------------------------------------------

note: collection_slug is the text at the end of OpenSea url

![image](https://user-images.githubusercontent.com/80938768/155941533-a9e86c86-54e5-4708-b1fe-0b05ca48033c.png)


`/project-realtime`

display real-time price of specific project. option:project_name

`/project-history`

display history price of specific project. option:project_name

`/project-nft`

search the NFT of a specific collection and token id. option:contract_address token_id

`/project-rarity`

calculate the rarity of a specific NFT. option:collection_slug token_id

`/txn`

enter the address and display the transaction record. option: eth_address

`/account_info`

enter the address to display ETH balance and Demi NFT balance. option: eth_address

Requirements
-----------------
**environment**

+ Python > 3.8

**packages**

+ discord
+ discord-py-slash-command
+ qrcode
+ urllib
+ json
+ asyncio
+ request
+ flask

Video Tutorial
-----------------
If you want to use different version bot, change the repl.it link I fork in the video.

https://www.youtube.com/watch?v=WFP9LdiB8yk

Usage
-----------------
There are 2 ways to run this bot.
Whether you choose first or second method, you'll need [Discord bot token](https://discord.com/developers/applications) and [Etherscan API](https://etherscan.io/myapikey). If you choose the second method, you'll also need [Uptimerbot](https://uptimerobot.com/) account. If you want to use "send message in specific channel when there's a list or sold event of your NFT collection on OpenSea" this function, you'll also need OpenSea API key, you can apply for the API key [here](https://docs.opensea.io/reference/request-an-api-key). Fill in the google form to apply for the API key. They will send API key to your gmail in about 2 days

### 1.run it on repl.it(cloud)
You can run it on repl.it, just fork [it](https://replit.com/@xeiftc/Kizmeow-NFT-Tracker-V2) and run. Remember to change discord bot token and Etherscan API key, then put them in environment variable. **DO NOT PUT TOKENS IN YOUR CODE DIRECTLY** cuz repls on replit is public if you use their free plan, and there are some ppl using scrypt to grab your token.
Next, copy the link here, ![image](https://user-images.githubusercontent.com/80938768/146533872-021b05b3-f18c-44db-a943-527903dc6616.png) create a [Uptimerbot](https://uptimerobot.com/) account and paste your link here. ![image](https://user-images.githubusercontent.com/80938768/146534310-74201ab2-700e-4271-94a2-f2ecf8d12acb.png)

### 2.run it on your computer(local)
Just download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and install all the packages in **Requirement**, make sure you have install python. Remember to change discord bot token and Etherscan API key. Then, run main.py

Official Website
-----------------
https://watercatuwu.github.io/kizmeow-nft-site/ 

by WaterCatMeow

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)
