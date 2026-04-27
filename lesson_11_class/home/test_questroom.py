## **Завдання 3: Написати юніт-тести для класу QuestRoom**

import pytest
from quest_room import QuestRoom

## **1. Тести конструктора**

def test_constructor():
    room = QuestRoom("Піратський острів", 3, 4)

    assert room.name == "Піратський острів"
    assert room.level_dificulty == 3
    assert room.player_limit == 4
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []

## **2. Додавання гравців**

def test_add_player():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Євген")

    assert "Євген" in room.players

def test_add_multiple_players_order():
    room = QuestRoom("Піратський острів", 3, 5)
    room.add_player("Андрій")
    room.add_player("Іван")

    assert room.players == ["Андрій", "Іван"]

def test_add_player_when_limit_reached():
    room = QuestRoom("Піратський острів", 3, 2)
    room.add_player("Петро")
    room.add_player("Хома")

    result = room.add_player("Яків")

    assert result == "No free slots!"
    assert "Яків" not in room.players
    assert room.players == ["Петро", "Хома"]

def test_add_duplicate_player_name():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Натанаїл")
    room.add_player("Натанаїл")

    assert room.players == ["Натанаїл", "Натанаїл"]

def test_add_player_log():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Натанаїл")

    assert "Player Натанаїл joined" in room.events_log

## **3. Видалення гравців**

def test_remove_player():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Василь")

    result = room.remove_player("Василь")

    assert "Василь" not in room.players
    assert result == "Player Василь left"
    assert "Player Василь left" in room.events_log

def test_remove_not_existing_player():
    room = QuestRoom("Піратський острів", 3, 4)

    result = room.remove_player("Віктор")

    assert result == "Player not found"
    assert room.events_log == []

def test_remove_from_empty_room():
    room = QuestRoom("Піратський острів", 3, 4)

    result = room.remove_player("Віктор")

    assert result == "Player not found"

def test_remove_player_log():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Сергій")
    room.remove_player("Сергій")

    assert "Player Сергій left" in room.events_log

## **4. Перевірка заповненості**

def test_room_not_full():
    room = QuestRoom("Піратський острів", 3, 3)
    room.add_player == "Сергій"
    
    assert room.is_full() is False

def test_room_is_full():
    room = QuestRoom("Піратський острів", 3, 2)
    room.add_player("Антон")
    room.add_player("Ігор")

    assert room.is_full() is True

def test_free_slots():
    room = QuestRoom("Піратський острів", 3, 3)
    room.add_player("Степан")

    assert room.free_slots() == 2

def test_free_slots_when_full():
    room = QuestRoom("Піратський острів", 3, 3)
    room.add_player("Марина")
    room.add_player("Галина")
    room.add_player("Дарина")

    assert room.free_slots() == 0

## **5. Запуск квесту**

def test_start_empty_room():
    room = QuestRoom("Піратський острів", 3, 4)

    result = room.start()

    assert result == "Room is empty"
    assert room.status == "waiting"

def test_start_with_players():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Катерина")
    room.add_player("Устина")

    result = room.start()

    assert room.status == "active"
    assert result == "Quest 'Піратський острів' started with 2 players!"
    assert room.events_log[2] == "Quest 'Піратський острів' started with 2 players!"

## **6. Скидання кімнати**

def test_reset_clears_players():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Катерина")
    room.add_player("Устина")

    room.reset_room()

    assert room.players == []

def test_reset_room_status():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Ярина")
    room.start()
    room.reset_room()

    assert room.status == "waiting"

def test_reset_room_log():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Юстина")
    room.reset_room()

    assert "Room reset" in room.events_log

 ## **7. Список гравців**
 
def test_players_list():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Катерина")
    room.add_player("Устина")

    assert room.players_list() == ["Катерина", "Устина"]

def test_if_players_list_is_empty():
    room = QuestRoom("Піратський острів", 3, 4)

    assert room.players_list() == "No players in the room"

## **8. Лог подій**

def test_show_log_correct_order():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Андрій")
    room.add_player("Іван")
    room.remove_player("Василь")
    room.start()
    room.reset_room()
    result = room.show_log()

    assert result == [
        "Player Андрій joined",
        "Player Іван joined",
        "Quest 'Піратський острів' started with 2 players!",
        "Room reset"
    ]

## **9. Комбіновані сценарії**

def test_full_flow_add_start_reset():
    room = QuestRoom("Піратський острів", 3, 4)
    room.add_player("Андрій")
    room.add_player("Іван")
    room.start()
    room.reset_room()

    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == [
        "Player Андрій joined",
        "Player Іван joined",
        "Quest 'Піратський острів' started with 2 players!",
        "Room reset"
    ]

def test_capacity_and_replacement_flow():
    room = QuestRoom("Піратський острів", 3, 2)
    room.add_player("Андрій")
    room.add_player("Іван")

    assert room.is_full() is True

    result = room.add_player("Петро")

    assert result == "No free slots!"
    assert "Петро" not in room.players

    room.remove_player("Іван")
    room.add_player("Юда")

    assert room.players == ["Андрій", "Юда"]