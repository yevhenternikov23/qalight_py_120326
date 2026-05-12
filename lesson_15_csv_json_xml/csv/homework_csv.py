import csv
from pathlib import Path


def read_file(filepath: Path) -> list[dict]:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def remove_duplicates(rows: list[dict]) -> list[dict]:
    exist = set()
    unique_rows = []
        
    for row in rows:
        row_tuple = tuple(row.items())

        if row_tuple not in exist:
            exist.add(row_tuple)
            unique_rows.append(row)

    return unique_rows

def write_csv(filepath: Path, content: list[dict]):
    if not content:
        return
    
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        headers = content[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
        writer.writerows(content)

if __name__ == "__main__":
    base_path = Path(__file__).parent

    file1 = base_path / "users_1.csv"
    file2 = base_path / "users_2.csv"
    output = base_path / "clean_users_3.csv"

    rows1 = read_file(file1)
    rows2 = read_file(file2)

    all_rows = rows1 + rows2

    unique_rows = remove_duplicates(all_rows)

    write_csv(output, unique_rows)

    print(f"Збережено {len(unique_rows)} унікальних рядків у {output} файл")