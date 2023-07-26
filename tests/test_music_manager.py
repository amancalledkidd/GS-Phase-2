from lib.music_manager import *

def test_list_music():
    music = MusicManager()
    assert music.list_music() == []
    

def test_add_music():
    music = MusicManager()
    music.add('Jimmy Cliff - I can see clearly now')
    assert music.list_music() == ['Jimmy Cliff - I can see clearly now']