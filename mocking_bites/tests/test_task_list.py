from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

#Given task, add task to list and all return list of tasks

def test_add_and_returns_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1 = 'Clean the car'
    fake_task_2 = Mock()
    fake_task_2 = 'Buy some milk'
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all() == [fake_task_1, fake_task_2]

def test_all_complete_returns_true_when_all_complete():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2 = Mock()
    fake_task_2.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all_complete() == True

def test_all_complete_returns_false_when_one_false():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2 = Mock()
    fake_task_2.is_complete.return_value = False
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all_complete() == False

def test_all_complete_returns_false_when_both_false():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = False
    fake_task_2 = Mock()
    fake_task_2.is_complete.return_value = False
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all_complete() == False



















































# def test_fake_task_returns_list_of_tasks():
#     task_list = TaskList()
#     fake_task_1 = Mock()
#     fake_task_1.return_value = 'hello'
#     fake_task_2 = Mock()
#     fake_task_2.return_value = 'goodbye'
#     task_list.add(fake_task_1)
#     task_list.add(fake_task_2)
#     assert task_list.all() == [fake_task_1, fake_task_2]

# def test_mock_all_complete_if_true():
#     task_list = TaskList()
#     fake_task_1 = Mock()
#     fake_task_1.is_complete.return_value = True
#     fake_task_2 = Mock()
#     fake_task_2.is_complete.return_value = True
#     task_list.add(fake_task_1)
#     task_list.add(fake_task_2)
#     assert task_list.all_complete() == True

# def test_mock_all_complete_if_only_one_value_true():
#     task_list = TaskList()
#     fake_task_1 = Mock()
#     fake_task_1.is_complete.return_value = True
#     fake_task_2 = Mock()
#     fake_task_2.is_complete.return_value = False
#     task_list.add(fake_task_1)
#     task_list.add(fake_task_2)
#     assert task_list.all_complete() == False

