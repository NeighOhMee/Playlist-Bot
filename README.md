# Playlist-Bot

## Build Instructions
Follow step 1 to generate a YOUR_CLIENT_SECRET_FILE.json
https://developers.google.com/youtube/v3/quickstart/python

Create the discord bot by going to https://discordapp.com/ Developers - Developer Portal.
click on new aplication and name the bot.
Go to the bot tab and click on add bot.
click on copy under Token in the bot tab and paste it on the last line in main.py where it says 'INSERT CLIENT ID HERE'.
Invite the bot to your server by going to the OAuth2 tab and clicking on the bot checkmark.
In the Bot Permisions section check Send Messages, Send TTS Messages, Manage Messages, and Read Message History.
Copy the link right above and past it into a browser.
Select which server you want the bot in.
Go back to main.py and where it says INSERT PLAYLIST ID HERE(on lines 2313 and 231) put the playlist id associated with the youtube account that you want to change.
Run the main.py file to activate the bot. The youtube api will give a link to authorize the bot. Select the youtube account that you want to change the playlist for.

use !updatePlaylist to add all the songs in the channel to your playlist
use !playlist to get a link to your playlist


## References
https://discordpy.readthedocs.io/en/latest/api.html#
https://developers.google.com/youtube/v3/docs/playlistItems/insert?apix=true
