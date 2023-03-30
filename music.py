from kivy.utils import platform


class _AndroidMusic:
    def __init__(self):
        from jnius import autoclass
        MediaPlayer = autoclass('android.media.MediaPlayer')


        self.player = MediaPlayer()
        self.filename = None
    def load(self,filename):
        self.filename=filename
        self.player.setDataSource(self.filename)

    def play(self):
        self.player.prepare()
        self.player.start()

    def reset(self):
        self.player.reset()
        self.filename=None

class _WindowsMusic:
    def __init__(self):
        self.filename = None
    def load(self, filename):
        self.filename = filename

    def play(self):
        if self.filename is not None:
            from playsound import playsound
            playsound(self.filename)
        else:
            raise Exception("you need to call load() before calling play()")

    def reset(self):
        self.filename=None

def get_music_player():
    if platform=="android":
        return _AndroidMusic()
    return _WindowsMusic()
