from unittest.mock import Mock
from lib.secret_diary_peer_classes import SecretDiary
import pytest
#given lock is true, read returns error when read function called

def test_read_when_lock_is_true_by_defult_returns_error():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    fake_diary.contents = 'This is a diary entry'
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'

#given lock is false, read returns diary entry 

def test_read_when_lock_is_false_returns_error():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    fake_diary.contents = 'This is a diary entry'
    secret_diary.unlock()
    assert secret_diary.read() == 'This is a diary entry'

def test_read_when_lock_is_true_returns_error():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    fake_diary.contents = 'This is a diary entry'
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'
