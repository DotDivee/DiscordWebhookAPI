import requests


class Json:
    def serialize(self):
        pass


class Author(Json):
    url = ""
    icon_url = ""
    name = ""

    def set_url(self, url: str):
        self.url = url
        return self

    def set_icon_url(self, icon_url: str):
        self.icon_url = icon_url
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def serialize(self):
        json = {}
        if self.icon_url:
            json["icon_url"] = self.icon_url
        if self.name:
            json["name"] = self.name
        if self.url:
            json["url"] = self.url

        return json


class Field(Json):
    name = ""
    value = ""

    inline = False

    def set_name(self, name: str):
        self.name = name
        return self

    def set_value(self, value: str):
        self.value = value
        return self

    def set_inline(self, inline: bool):
        self.inline = inline
        return self

    def serialize(self):
        json = {}
        if self.name:
            json["name"] = self.name
        if self.value:
            json["value"] = self.value
        if self.inline:
            json["inline"] = self.inline

        return json


class Footer(Json):
    text = ""
    icon_url = ""

    def set_text(self, text: str):
        self.text = text
        return self

    def set_icon_url(self, icon_url: str):
        self.icon_url = icon_url
        return self

    def serialize(self):
        json = {}
        if self.text:
            json["text"] = self.text
        if self.icon_url:
            json["icon_url"] = self.icon_url

        return json


class Embed(Json):
    fields = []

    author = None

    footer = None

    url = ""
    title = ""
    description = ""
    timestamp = ""

    color = 0

    def add_field(self, field: Field):
        self.fields.append(field)
        return self

    def set_author(self, author: Author):
        self.author = author
        return self

    def set_footer(self, footer: Footer):
        self.footer = footer
        return self

    def set_url(self, url: str):
        self.url = url
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_description(self, description: str):
        self.description = description
        return self

    def set_timestamp(self, timestamp: str):
        self.timestamp = timestamp
        return self

    def set_color(self, color: int):
        self.color = color
        return self

    def serialize(self):
        json = {}
        if self.fields:
            fields = []
            for field in self.fields:
                fields.append(field.serialize())

            json["fields"] = fields
        if self.author is not None:
            json["author"] = self.author.serialize()
        if self.footer is not None:
            json["footer"] = self.footer.serialize()
        if self.url:
            json["url"] = self.url
        if self.title:
            json["title"] = self.title
        if self.description:
            json["description"] = self.description
        if self.timestamp:
            json["timestamp"] = self.timestamp
        if self.color:
            json["color"] = self.color

        return json


class DiscordWebhook:
    embeds = []

    avatar_url = ""
    username = ""
    content = ""

    tts = False

    def __init__(self, url: str):
        self.url = url

    def add_embed(self, embed: Embed):
        self.embeds.append(embed)
        return self

    def set_avatar_url(self, avatar_url: str):
        self.avatar_url = avatar_url
        return self

    def set_username(self, username: str):
        self.username = username
        return self

    def set_content(self, content: str):
        self.content = content
        return self

    def set_tts(self, tts: bool):
        self.tts = tts
        return self

    def send(self):
        json = {}
        if self.embeds:
            embeds = []
            for embed in self.embeds:
                embeds.append(embed.serialize())

            json["embeds"] = embeds
        if self.avatar_url:
            json["avatar_url"] = self.avatar_url
        if self.username:
            json["username"] = self.username
        if self.content:
            json["content"] = self.content
        if self.tts:
            json["tts"] = self.tts

        requests.post(self.url, json=json)
