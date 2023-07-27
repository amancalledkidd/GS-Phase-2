from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_to_list():
    my_diary = Diary()
    first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
    second_entry = DiaryEntry('Day 2', 'so far so good, making good')
    my_diary.add(first_entry)
    my_diary.add(second_entry)
    assert my_diary.all() == [first_entry, second_entry]

def test_total_count_words():
    my_diary = Diary()
    first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
    second_entry = DiaryEntry('Day 2', 'so far so good, making good')
    my_diary.add(first_entry)
    my_diary.add(second_entry)
    assert my_diary.count_words() == 10

def test_diary_reading_time():
    my_diary = Diary()
    first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
    second_entry = DiaryEntry('Day 2', 'so far so good, making good')
    my_diary.add(first_entry)
    my_diary.add(second_entry)
    assert my_diary.reading_time(10) == 2

def test_best_entry_for_reading_time():
    my_diary = Diary()
    first_entry = DiaryEntry('Hello, world' , 'Welcome to my diary')
    second_entry = DiaryEntry('Day 2', 'so far so good, making good')
    third_entry = DiaryEntry('Day 3', 'more more more so far so good, making good')
    my_diary.add(first_entry)
    my_diary.add(second_entry)
    my_diary.add(third_entry)
    assert my_diary.find_best_entry_for_reading_time(7, 1) == second_entry