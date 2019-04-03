class Youtuber:

    def __init__(self, name, channel_link):
        self.name = name
        self.channel_link = channel_link

    def get_name(self):
        return self.name

    def get_channel(self):
        return self.channel_link

    def update_name(self, new_name):
        self.name = new_name

    def update_channel(self, new_channel_link):
        self.channel_link = new_channel_link
