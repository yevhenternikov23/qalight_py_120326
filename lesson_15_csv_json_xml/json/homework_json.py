import json
from pathlib import Path


def read_json(filepath: Path) -> dict:
    """
    Читає JSON файл та повертає його вміст як Python об'єкт.
    """

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filepath} не знайдено.")
    except json.JSONDecodeError as e:
        print(f"Помилка у файлі {filepath}: {e}")
    return None
    
def write_json(filepath: Path, content: dict):
    """
    Записує Python об'єкт у JSON файл.
    """

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Не вдалося записати файл {filepath}: {e}")
        return False
    
if __name__ == "__main__":
    files = [
        Path(__file__).parent / "file_01.json",
        Path(__file__).parent / "file_02.json",
        Path(__file__).parent / "file_03.json",
    ]
    for file_path in files:
        print(f"Назва файлу: {file_path.name}")
        content = read_json(file_path)
        if content is not None:
            print("JSON коректний")
        else:
            print("JSON некоректний")