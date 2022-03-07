# Kizmeow-NFT-Mint-Progress-Discord-Bot(editing, I'll finish it tommorow, I'm too tired now UwU)


### [中文版](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/%E8%AE%80%E6%88%91.md) | [English Ver](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/README.md)
A Discord bot wrote with Python. Kizmeow let you track mint progress of your NFT project and display them by editing channel name.

If you like this project, please give me star on the upper right corner:)


What can this bot do?
-----------------
Get data from Etherscan and display mint progress by change channel name of voice channel.

![image](https://user-images.githubusercontent.com/80938768/156949496-d08b131e-8702-4045-801a-6a3aa6aab7a2.png)

Commands
-----------------
`/config`

enter some information to setup yuor bot. option: channel_id contract_address total_supply etherscan_api_key

`/config_check`

check the information you entered using `/config`

`/ping`

return bot latency

Requirements
-----------------
**environment**

+ Python > 3.8

**packages**

+ discord
+ discord-py-slash-command
+ urllib
+ json
+ asyncio
+ request
+ flask

Usage
-----------------
There are 2 ways to run this bot.
Whether you choose first or second method, you'll need [Discord bot token](https://discord.com/developers/applications) and [Etherscan API](https://etherscan.io/myapikey). If you choose the second method, you'll also need [Uptimerbot](https://uptimerobot.com/) account.

### 1.run it on repl.it(cloud)
You can run it on repl.it, just fork [it](https://replit.com/@xeiftc/Kizmeow-Mint-Progress) and run. Remember to change discord bot token and Etherscan API key, then put them in environment variable. **DO NOT PUT TOKENS IN YOUR CODE DIRECTLY** cuz repls on replit is public if you use their free plan, and there are some ppl using script to grab your token.
Next, copy the link here, ![image](https://user-images.githubusercontent.com/80938768/146533872-021b05b3-f18c-44db-a943-527903dc6616.png) create a [Uptimerbot](https://uptimerobot.com/) account and paste your link here. ![image](https://user-images.githubusercontent.com/80938768/146534310-74201ab2-700e-4271-94a2-f2ecf8d12acb.png)

### 2.run it on your computer(local)
Just download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and install all the packages in **Requirement**, make sure you have install python. Remember to change discord bot token and Etherscan API key. Then, run main.py

After you finish 1 or 2 above,

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)
