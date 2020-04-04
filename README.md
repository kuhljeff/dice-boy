# dice-boy
A simple bot for playing RPGs over discord

# Installation
1. [Follow these steps](https://discordpy.readthedocs.io/en/latest/discord.html) to setup a bot account. Be sure to hang on to your token from step 7.
2. Get [discord.py](https://github.com/Rapptz/discord.py) up and running (voice support not required. Python virtual environments recommended.)
3. Clone this repository.
4. Paste your token into environments_template.json in the "token" property. Rename this file to "environments.json".
5. Fill out the campaign and system info in environments.json as you see fit. It's all metadata. Be sure to set the "default" property to match the campaign name of the default environment.
6. Run dice_boy.py
7. You're done!

TODOs
1. automatic saving
1. finish rest of profile commands
1. refreshables (long / short rest)
1. roll from profile without switching profile
1. show multi dice rolls results separately
1. timekeeping
1. dm can award xp (dm tools in general)
1. Cleanup this readme lol
