import requests


class Json:
    def serialize(self):
        pass


class Author(Json):
    def __init__(self, name: str, url: str, icon_url: str):
        self.name = name
        self.url = url
        self.icon_url = icon_url

    def serialize(self):
        json = {}
        if self.name:
            json["name"] = self.name
        if self.url:
            json["url"] = self.url
        if self.icon_url:
            json["icon_url"] = self.icon_url

        return json

    class Builder:
        _name = ""
        _url = ""
        _icon_url = ""

        def set_name(self, name: str):
            self._name = name
            return self

        def set_url(self, url: str):
            self._url = url
            return self

        def set_icon_url(self, icon_url: str):
            self._icon_url = icon_url
            return self

        def build(self):
            return Author(self._name, self._url, self._icon_url)


class Field(Json):
    def __init__(self, name: str, value: str, inline: bool):
        self.name = name
        self.value = value
        self.inline = inline

    def serialize(self):
        json = {}
        if self.name:
            json["name"] = self.name
        if self.value:
            json["value"] = self.value
        if self.inline:
            json["inline"] = self.inline

        return json

    class Builder:
        _name = ""
        _value = ""

        _inline = False

        def set_name(self, name: str):
            self._name = name
            return self

        def set_value(self, value: str):
            self._value = value
            return self

        def set_inline(self, inline: bool):
            self._inline = inline
            return self

        def build(self):
            return Field(self._name, self._value, self._inline)


class Footer(Json):
    def __init__(self, text: str, icon_url: str):
        self.text = text
        self.icon_url = icon_url

    def serialize(self):
        json = {}
        if self.text:
            json["text"] = self.text
        if self.icon_url:
            json["icon_url"] = self.icon_url

        return json

    class Builder:
        _text = ""
        _icon_url = ""

        def set_text(self, text: str):
            self._text = text
            return self

        def set_icon_url(self, icon_url: str):
            self._icon_url = icon_url
            return self

        def build(self):
            return Footer(self._text, self._icon_url)


class Embed(Json):
    def __init__(self, author: Author, footer: Footer, fields: list[Field], title: str, description: str, url: str,
                 timestamp: str, color: int):
        self.author = author

        self.footer = footer

        self.fields = fields

        self.title = title
        self.description = description
        self.url = url
        self.timestamp = timestamp

        self.color = color

    def serialize(self):
        json = {}
        if self.author is not None:
            json["author"] = self.author.serialize()
        if self.footer is not None:
            json["footer"] = self.footer.serialize()
        if self.fields:
            fields = []
            for field in self.fields:
                fields.append(field.serialize())

            json["fields"] = fields
        if self.title:
            json["title"] = self.title
        if self.description:
            json["description"] = self.description
        if self.url:
            json["url"] = self.url
        if self.timestamp:
            json["timestamp"] = self.timestamp
        if self.color:
            json["color"] = self.color

        return json

    class Builder:
        _author = None

        _footer = None

        _fields = []

        _title = ""
        _description = ""
        _url = ""
        _timestamp = ""

        _color = 0

        def set_author(self, author: Author):
            self._author = author
            return self

        def set_footer(self, footer: Footer):
            self._footer = footer
            return self

        def add_field(self, field: Field):
            self._fields.append(field)
            return self

        def set_title(self, title: str):
            self._title = title
            return self

        def set_description(self, description: str):
            self._description = description
            return self

        def set_url(self, url: str):
            self._url = url
            return self

        def set_timestamp(self, timestamp: str):
            self._timestamp = timestamp
            return self

        def set_color(self, color: int):
            self._color = color
            return self

        def build(self):
            return Embed(self._author, self._footer, self._fields, self._title, self._description, self._url,
                         self._timestamp, self._color)


class DiscordWebhook:
    def __init__(self, embeds: list[Embed], url: str, username: str, content: str, tts: bool):
        self.embeds = embeds

        self.url = url
        self.username = username
        self.content = content

        self.tts = tts

    def send(self):
        json = {}
        if self.embeds:
            embeds = []
            for embed in self.embeds:
                embeds.append(embed.serialize())

            json["embeds"] = embeds
        if self.username:
            json["username"] = self.username
        if self.content:
            json["content"] = self.content
        if self.tts:
            json["tts"] = self.tts

        requests.post(self.url, json=json)

    class Builder:
        _embeds = []

        _url = ""
        _username = ""
        _content = ""

        _tts = False

        def __init__(self, url: str):
            self._url = url

        def add_embed(self, embed: Embed):
            self._embeds.append(embed)
            return self

        def set_username(self, username: str):
            self._username = username
            return self

        def set_content(self, content: str):
            self._content = content
            return self

        def set_tts(self, tts: bool):
            self._tts = tts
            return self

        def build(self):
            return DiscordWebhook(self._embeds, self._url, self._username, self._content, self._tts)
