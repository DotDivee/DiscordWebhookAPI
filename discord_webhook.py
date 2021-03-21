import requests


class DiscordWebhook:
    def __init__(self, url, username, content, embeds):
        self.url = url
        self.username = username
        self.content = content
        self.embeds = embeds

    def send(self):
        json = {}
        if self.username is not None:
            json["username"] = self.username
        if self.content is not None:
            json["content"] = self.content
        if self.embeds:
            json["embeds"] = self.embeds

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

        def __init__(self, url, content):
            self._url = url
            self._content = content

        def setURL(self, url):
            self._url = url
            return self

        def setUsername(self, username):
            self._username = username
            return self

        def setContent(self, content):
            self._content = content
            return self

        def addEmbed(self, embed):
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

        def build(self):
            return DiscordWebhook(self._url, self._username, self._content, self._embeds)


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

        def setAuthor(self, author):
            json = {}
            if author.name is not None:
                json["name"] = author.name
            if author.url is not None:
                json["url"] = author.url
            if author.iconURL is not None:
                json["icon_url"] = author.iconURL

            self._author = json
            return self

        def setTitle(self, title):
            self._title = title
            return self

        def setURL(self, url):
            self._url = url
            return self

        def setDescription(self, description):
            self._description = description
            return self

        def addField(self, field):
            json = {}
            if field.name is not None:
                json["name"] = field.name
            if field.value is not None:
                json["value"] = field.value
            if field.inline is not None:
                json["inline"] = field.inline

            self._fields.append(json)
            return self

        def setColor(self, color):
            self._color = color
            return self

        def setTimestamp(self, timestamp):
            self._timestamp = timestamp
            return self

        def setFooter(self, footer):
            json = {}
            if footer.text is not None:
                json["text"] = footer.text
            if footer.iconURL is not None:
                json["icon_url"] = footer.iconURL

            self._footer = json
            return self

        def build(self):
            return Embed(self._author, self._title, self._url, self._description, self._fields, self._color,
                         self._timestamp, self._footer)


class Author:
    def __init__(self, name, url, iconURL):
        self.name = name
        self.url = url
        self.iconURL = iconURL

    class Builder:
        _name = None
        _url = None
        iconURL = None

        def setName(self, name):
            self._name = name
            return self

        def setURL(self, url):
            self._url = url
            return self

        def setIconURL(self, iconURL):
            self.iconURL = iconURL
            return self

        def build(self):
            return Author(self._name, self._url, self.iconURL)


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

        def setName(self, name):
            self._name = name
            return self

        def setValue(self, value):
            self._value = value
            return self

        def setInline(self, inline):
            self._inline = inline
            return self

        def build(self):
            return Field(self._name, self._value, self._inline)


class Footer:
    def __init__(self, text, iconURL):
        self.text = text
        self.iconURL = iconURL

    class Builder:
        _text = None
        _iconURL = None

        def setText(self, text):
            self._text = text
            return self

        def setIconURL(self, iconURL):
            self._iconURL = iconURL
            return self

        def build(self):
            return Footer(self._text, self._iconURL)
