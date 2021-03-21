from discord_webhook import DiscordWebhook, Embed, Author, Footer

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
    .setColor(0xffffff)
    .setTimestamp("2021-3-21")
    .setFooter(
        # Initializes A New Footer Using The Footer Builder Object
        Footer.Builder()
        .setText("TEXT")
        .setIconURL("http://YOUR.ICONURL")
    )
    .build()
)

# Converts Builder Object To A DiscordWebhook Object And Runs
builder.build().send()
