from App import App
from MusicManager import MusicManager
from SyncManager import SyncManager

app = App()
session = app.auth_user() # authorise in account

manager = MusicManager(session)
songs = manager.get_audio_list()

sync = SyncManager()
sync.download_audio(songs)
