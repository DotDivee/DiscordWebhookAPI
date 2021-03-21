# DiscordWebhookAPI
A Simple And Easy To Use Webhook API For The Discord Service, Written In Python.

## Requirements
- The [Python](https://www.python.org) Programming Language
- The [Requests](https://github.com/psf/requests) Library For Handling HTTP Requests.
- A Brain.

## Example
From [Example](example.py) File.

```python
from discord_webhook import DiscordWebhook, Embed, Author, Field, Footer

# Initializing The Webhook Builder Object
builder = DiscordWebhook.Builder("WEBHOOK URL", "CONTENT")
builder.setUsername("USERNAME")
builder.setURL("http://YOUR.URL")

# Adds A New Embed Using The Embed Builder Object
builder.addEmbed(
    Embed.Builder()
    .setAuthor(
        # Initializes A New Author Using The Author Builder Object
        Author.Builder()
        .setName("NAME")
        .setURL("http://YOUR.URL")
        .setIconURL("http://YOUR.ICONURL")
    )
    .setTitle("TITLE")
    .setURL("http://YOUR.URL")
    .setDescription("DESCRIPTION")
    .addField(
        Field.Builder()
        .setName("NAME")
        .setValue("VALUE")
        .setInline(True)
        .build()
    )
    .setColor(0xffffff)
    .setTimestamp("2021-3-21")
    .setFooter(
        # Initializes A New Footer Using The Footer Builder Object
        Footer.Builder()
        .setText("TEXT")
        .setIconURL("http://YOUR.ICONURL")
        .build()
    )
    .build()
)

# Converts Builder Object To A DiscordWebhook Object And Runs
builder.build().send()
```
