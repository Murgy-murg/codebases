from lib.diary_peer_classes import Diary

#given  a string, read returns string

def test_read_returns_string_of_contents():
    diary = Diary('this is the contents')
    assert diary.read() == 'this is the contents'
