This is a bot that reminds users to use vxTwitter to embed Twitter links in
Discord. It replies with a list of every Twitter link in the original messages
changed to vxTwitter links.

# Usage

Installing the package with `pip` creates a `vxbot` command to start the bot.
The bot requires a [token](#create-a-discord-bot).

```
python3 -m pip install https://github.com/pgsocks/vxbot/archive/1.0.0.tar.gz

vxbot --token <YOUR BOT TOKEN>
```

# Docker

Docker can make it easier to deploy Discord bots. First, build the image, then
run the container.

```
docker build -t vxbot \
    -f docker/Dockerfile \
    https://github.com/pgsocks/vxbot.git#1.0.0

docker run -e DISCORD_TOKEN=<YOUR BOT TOKEN> vxbot
```

# Create a Discord Bot

* Create an application in the [Discord developer portal][1]
* Create a bot
* Copy the bot token
* Enable message content **Intents** for your application
* Create an OAuth2 invite link for your bot with the following permissions
    * Read messages
    * Send messages
    * Embed links
* Paste the invite link in your browser address bar to invite the bot

[1]: https://discord.com/developers/applications/
