import requests


class DiscordWebhook:
    def __init__(self, url, username, content, embeds, tts):
        self.url = url
        self.username = username
        self.content = content
        self.embeds = embeds
        self.tts = tts

    def send(self):
        json = {}
        if self.username is not None:
            json["username"] = self.username
        if self.content is not None:
            json["content"] = self.content
        if self.embeds:
            json["embeds"] = self.embeds
        if self.tts is not None:
            json["tts"] = self.tts

        request = requests.post(self.url, json=json)

        try:
            request.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            print(exception)

    class Builder:
        _url = None
        _username = None
        _content = None
        _embeds = []
        _tts = None

        def __init__(self, url, content):
            self._url = url
            self._content = content

        def set_url(self, url):
            self._url = url
            return self

        def set_username(self, username):
            self._username = username
            return self

        def set_content(self, content):
            self._content = content
            return self

        def add_embed(self, embed):
            json = {}
            if embed.author is not None:
                json["author"] = embed.author
            if embed.title is not None:
                json["title"] = embed.title
            if embed.url is not None:
                json["url"] = embed.url
            if embed.description is not None:
                json["description"] = embed.description
            if embed.fields is not None:
                json["fields"] = embed.fields
            if embed.color is not None:
                json["color"] = embed.color
            if embed.timestamp is not None:
                json["timestamp"] = embed.timestamp
            if embed.footer is not None:
                json["footer"] = embed.footer

            self._embeds.append(json)
            return self

        def set_tts(self, tts):
            self._tts = tts
            return self

        def build(self):
            return DiscordWebhook(self._url, self._username, self._content, self._embeds, self._tts)


class Embed:
    def __init__(self, author, title, url, description, fields, color, timestamp, footer):
        self.author = author
        self.title = title
        self.url = url
        self.description = description
        self.fields = fields
        self.color = color
        self.timestamp = timestamp
        self.footer = footer

    class Builder:
        _author = None
        _title = None
        _url = None
        _description = None
        _fields = []
        _color = None
        _timestamp = None
        _footer = None

        def set_author(self, author):
            json = {}
            if author.name is not None:
                json["name"] = author.name
            if author.url is not None:
                json["url"] = author.url
            if author.icon_url is not None:
                json["icon_url"] = author.icon_url

            self._author = json
            return self

        def set_title(self, title):
            self._title = title
            return self

        def set_url(self, url):
            self._url = url
            return self

        def set_description(self, description):
            self._description = description
            return self

        def add_field(self, field):
            json = {}
            if field.name is not None:
                json["name"] = field.name
            if field.value is not None:
                json["value"] = field.value
            if field.inline is not None:
                json["inline"] = field.inline

            self._fields.append(json)
            return self

        def set_color(self, color):
            self._color = color
            return self

        def set_timestamp(self, timestamp):
            self._timestamp = timestamp
            return self

        def set_footer(self, footer):
            json = {}
            if footer.text is not None:
                json["text"] = footer.text
            if footer.icon_url is not None:
                json["icon_url"] = footer.icon_url

            self._footer = json
            return self

        def build(self):
            return Embed(self._author, self._title, self._url, self._description, self._fields, self._color,
                         self._timestamp, self._footer)


class Author:
    def __init__(self, name, url, iconURL):
        self.name = name
        self.url = url
        self.icon_url = iconURL

    class Builder:
        _name = None
        _url = None
        _icon_url = None

        def set_name(self, name):
            self._name = name
            return self

        def set_url(self, url):
            self._url = url
            return self

        def set_icon_url(self, iconURL):
            self._icon_url = iconURL
            return self

        def build(self):
            return Author(self._name, self._url, self._icon_url)


class Field:
    def __init__(self, name, value, inline):
        self.name = name
        self.value = value
        self.inline = inline

    class Builder:
        _name = None
        _value = None
        _inline = None

        def __init__(self, name, value):
            self._name = name
            self._value = value

        def set_name(self, name):
            self._name = name
            return self

        def set_value(self, value):
            self._value = value
            return self

        def set_inline(self, inline):
            self._inline = inline
            return self

        def build(self):
            return Field(self._name, self._value, self._inline)


class Footer:
    def __init__(self, text, icon_url):
        self.text = text
        self.icon_url = icon_url

    class Builder:
        _text = None
        _icon_url = None

        def set_text(self, text):
            self._text = text
            return self

        def set_icon_url(self, icon_url):
            self._icon_url = icon_url
            return self

        def build(self):
            return Footer(self._text, self._icon_url)
