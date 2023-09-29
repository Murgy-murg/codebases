from lib.diary_peer_classes import Diary
from lib.secret_diary_peer_classes import SecretDiary
import pytest

def test_read_when_lock_is_true_by_defult_returns_error():
    diary = Diary('This is some contents')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'

def test_read_when_lock_is_false_returns_error():
    diary = Diary('This is some contents')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'This is some contents'

def test_read_when_lock_is_true_returns_error():
    diary = Diary('This is some contents')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'
