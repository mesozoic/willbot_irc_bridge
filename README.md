# Willbot IRC Bridge Plugin

This is a plugin for the awesome Will Bot (https://github.com/skoczen/will/ and http://skoczen.github.io/will).

This plugin will connect to your IRC server of choice, and dutifully relay messages in both directions between same-named Hipchat rooms and IRC channels. This can be useful for letting less technical people participate in IRC discussions, or even to bridge the gap in a move between IRC and Hipchat.

Very alpha currently, but is in working order.

## Usage

 1. Get a Will instance running using the instructions at http://skoczen.github.io/will
 2. Clone this repo into a directory in your plugins directory
 3. pip install -r requirements.txt to install the python dependencies
 4. Add the following to your config.py, modifying as required:

     > IRC_BRIDGE_IRC_SERVER="irc.server.name"
     > IRC_BRIDGE_IRC_PORT="6667"
     > IRC_BRIDGE_NICKNAME="will_bot"
     > IRC_BRIDGE_USE_SSL=False
     > ROOMS = [ "list", "of", "hipchat", "rooms" ]

 5. Make sure your Will Bot is configured to join the Hipchat rooms with the same name as the IRC channels (without the #). Note that this is currently case-sensitive when relaying messages from IRC to Hipchat, which can cause issues with Hipchat rooms with capitals in the name.
 6. In a Hipchat room where Will Bot has joined, issue the command "@willbotname connect to IRC". This will instruct the plugin to connect to the IRC server and join the list of channels, and start relaying messages. This should be all that you need to do to make it work.

## Rate Limiting

Due to rate-limiting of the Hipchat messaging API, messages are relayed to Hipchat in batches every 2 seconds, this means that theoretically the plugin should never go over the 30/minute per-room message limit.

## Configuration Options

These should all go into your Willbot's `config.py` or the runtime environment:

* `HIPCHAT_SERVER` - HipChat server name (optional; default is `api.hipchat.com`)
* `USERNAME` - HipChat username
* `PASSWORD` - HipChat password
* `ROOMS` - HipChat rooms that you'll relay to/from IRC
* `IRC_BRIDGE_IRC_SERVER` - server name
* `IRC_BRIDGE_IRC_PORT` - server port
* `IRC_BRIDGE_NICKNAME` - nick to use within IRC channels
* `IRC_BRIDGE_PASSWORD` - password for IRC server (optional; default is empty string)
* `IRC_BRIDGE_USE_SSL` - whether to encrypt IRC connection (optional; default is `False`)
* `HIPCHAT_ROOMS_TO_IRC_CHANNELS` - dict of HipChat rooms to IRC channels (optional; default is empty).
  - IRC channel names should include the pound sign prefix (`#`).
  - If a HipChat room does not exist in this dict, the bridged IRC channel will have the same name as the HipChat room.
