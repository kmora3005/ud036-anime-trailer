import webbrowser
from twilio import rest

class Anime(object):
    def __init__(self, title, storyline, image, trailer_video):
        self.title=title
        self.storyline=storyline
        self.image=image
        self.trailer_video=trailer_video

    def show_trailer():
        webbrowser.open(self.trailer_video)
