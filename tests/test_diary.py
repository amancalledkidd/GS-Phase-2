from lib.diary import Diary

def test_empty_diary():
    my_diary = Diary()
    assert my_diary.all() == [] 
