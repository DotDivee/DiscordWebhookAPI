# DiscordWebhookAPI
A Simple And Easy To Use Webhook API For The Discord Service, Written In Python.

## Requirements
- The [Python](https://www.python.org) Programming Language.
- The [Requests](https://github.com/psf/requests) Library For Handling HTTP Requests.
- A Brain.

## Tutorial

### Importing
You Should Start Off By Importing The Discord Webhook Module Along With Any Elements You Will Need.

It's Best If You Just Import Everything Right Off The Bat Which Will Save You Time.

```python
from discord_webhook_api import *
```

### Initializing The Webhook
Initialize Your Webhook By Creating An Instance Of The **DiscordWebhook** Object.

Paste Your Webhook URL In The Constructor.

*This URL Is Just For Demonstration Purposes.*

```python
from discord_webhook_api import *

# Initialize Webhook
webhook = DiscordWebhook("https://your-webhook.url")
```

### Customizing Fields
Start By Settings Some Fields To Make It Fit Your Needs.

```python
from discord_webhook_api import *

# Initialize Webhook
webhook = DiscordWebhook("https://your-webhook.url")

# Set Fields
webhook.set_avatar_url("https://your-avatar.url")
webhook.set_username("Username")
webhook.set_content("Content")
webhook.set_tts(True)
```

### Adding An Embed
Embeds Are Useful For Displaying Large Amounts Of Information Or To Make Your Webhook Look Nice.

You Can Initialize One By Creating And Instance Of The **Embed** Object.

Unlike The **DiscordWebhook** Object, The **Embed** Object Doesn't Take Any Arguments. In Fact, The **DiscordWebhook** Object Is The Only Object That Takes Any Arguments.

```python
from discord_webhook_api import *

# Initialize Embed
embed = Embed()

# Set Embed Fields
embed.set_title("Title")
embed.set_description("Description")
``` 

Then Call The Add Embed Function On The Webhook Builder Class.

```python
from discord_webhook_api import *

# Initialize Embed
embed = Embed()

# Set Embed Fields
embed.set_title("Title")
embed.set_description("Description")

# Initialize Webhook
webhook = DiscordWebhook("https://your-webhook.url")

# Set Fields
webhook.set_username("Username")
webhook.set_content("Content")

# Add Embed
webhook.add_embed(embed)
``` 

### Sending
Finally, To Send Your Webhook Message, Call The Send Function On The Webhook.

If It Doesn't Work Check If You Have Inputted Your URLs Correctly Or If You Haven't Missed Any Required Fields.
