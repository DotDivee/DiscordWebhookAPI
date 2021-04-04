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
builder.set_username("USERNAME")
builder.set_url("http://YOUR.URL")
builder.set_tts(True)

# Adds A New Embed Using The Embed Builder Object
builder.add_embed(
    Embed.Builder()
    .set_author(
        # Initializes A New Author Using The Author Builder Object
        Author.Builder()
        .set_name("NAME")
        .set_url("http://YOUR.URL")
        .set_icon_url("http://YOUR.ICONURL")
    )
    .set_title("TITLE")
    .set_url("http://YOUR.URL")
    .set_description("DESCRIPTION")
    .add_field(
        # Initializes A New Field Using The Field Builder Object
        Field.Builder()
        .set_name("NAME")
        .set_value("VALUE")
        .set_inline(True)
        .build()
    )
    .set_color(0xffffff)
    .set_timestamp("2021-3-21")
    .set_footer(
        # Initializes A New Footer Using The Footer Builder Object
        Footer.Builder()
        .set_text("TEXT")
        .set_icon_url("http://YOUR.ICONURL")
        .build()
    )
    .build()
)

# Converts Builder Object To A DiscordWebhook Object And Runs
builder.build().send()

```

Note That Fields Such As The URL For The Webhook Builder Are Necessary To Pass Through The Init Constructor As The Request Would Work Without Them Being Filled.

Make Sure To **NOT** Leave These Fields Empty Either.
