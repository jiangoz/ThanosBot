# ThanosBot
![](https://i.imgur.com/HmZ1tqB.png)

### Discord bot built specifically for my large Discord servers (100k+ members).
WIP, always adding new features to assist me in server moderation & management. 

1) Create virtual environment in bot directory: `py -m venv bot_env`
2) Activate virtual environment on Linux: `source bot_env/bin/activate` or Windows: `bot_env\Scripts\activate`
3) Windows - change execution policy for PowerShell (if running above script is disabled): `Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "RemoteSigned"`
4) Install requirements/dependencies: `pip install -r requirements.txt`
5) Run bot with PM2: `pm2 start bot.py --interpreter=bot_env/bin/python`

### Python Packages Used:
- **jishaku:** https://github.com/Gorialis/jishaku 
- **langdetect:** https://github.com/Mimino666/langdetect 
- **emoji:** https://github.com/carpedm20/emoji
- **apscheduler:** https://github.com/agronholm/apscheduler

### Useful References/Links:
- **discord.py Documentation:** https://discordpy.readthedocs.io/en/latest/index.html  
- **Official Discord API:** https://discordapp.com/developers/docs/intro  
- **Python3 Documentation:** https://docs.python.org/3/

