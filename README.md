# DiscordWebhookAPI
A Simple And Easy To Use Webhook API For The Discord Service, Written In Python.

## Requirements
- The [Python](https://www.python.org) Programming Language.
- The [Requests](https://github.com/psf/requests) Library For Handling HTTP Requests.
- A Brain.

## Examples

### Importing
You Should Start Off By Importing The Discord Webhook Module Along With Any Elements You Will Need.

```python
from discord_webhook import *
```

### Initializing The Webhook
Initialize Your Discord Webhook Via The Discord Webhook Builder Object And Assign It To A Variable.

Paste In Your Webhook URL In The Constructor.

*This URL Is Just For Demonstration Purposes.*

```python
from discord_webhook import *

# Initialize Webhook
webhook = DiscordWebhook.Builder("https://your-webhook.url")
```

### Customizing Fields
Start By Perhaps Setting The Username Or Content Of Your Webhook.

```python
from discord_webhook import *

# Initialize Webhook
webhook = DiscordWebhook.Builder("https://your-webhook.url")

# Set Fields
webhook.set_username("Username")
webhook.set_content("Content")
```

### Adding An Embed
Embeds Are Useful For Displaying Large Amounts Of Information.

You Can Initialize One Using The Embed Builder Object.

Here I Change The Author Of The Embed Using The Author Builder Object.

**Make Sure To Call The Build Function Otherwise It Will Not Work.**

```python
from discord_webhook import *

# Initialize Embed
embed = Embed.Builder()

# Make Sure To Call Build On Any Builder Classes
embed.set_author(
    Author.Builder()
        .set_name("Name")
        .build()
)
``` 

Then Call The Add Embed Function On The Webhook Builder Class.

```python
from discord_webhook import *

# Initialize Webhook
webhook = DiscordWebhook.Builder("https://your-webhook.url")

# Set Fields
webhook.set_username("Username")
webhook.set_content("Content")

# Initialize Embed
embed = Embed.Builder()

# Make Sure To Call Build On Any Builder Classes
embed.set_author(
    Author.Builder()
        .set_name("Name")
        .build()
)

# Add Embed
webhook.add_embed(
    embed.build()
)
``` 

### Sending
Finally, To Send Your Webhook Message, Call The Build Function On Your Webhook Builder And Then The Send Function On The Webhook.

If It Doesn't Work Check If You Have Inputted Your URLs Correctly And Check For Required Fields (For Example The Content Field In The Webhook Is Required).
