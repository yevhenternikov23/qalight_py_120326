import xml.etree.ElementTree as ET
from pathlib import Path


def get_hmdtoken_expires(filepath: Path) -> str | None:
    
    tree = ET.parse(filepath)
    root = tree.getroot()

    namespaces = {
        "n": "http://example.org/alertcontrol"
    }

    # Шукаємо тег n:expires
    expires = root.find(".//n:expires", namespaces)
    if expires is not None:
        return expires.text
    return None

def get_group_incoming(filepath: Path, group_number: str) -> str | None:

    tree = ET.parse(filepath)
    root = tree.getroot()
   
    for group in root.findall("group"):
        number = group.find("number")

        # Перевіряємо номер групи
        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")
            if incoming is not None:
                return incoming.text

    return None

if __name__ == "__main__":
    base_path = Path(__file__).parent

    # 1. Обробка файлу `login.xml`

    login_xml = base_path / "login.xml"
    expires_value = get_hmdtoken_expires(login_xml)
    print("Значення n:expires:")
    print(expires_value)

    # 2. Обробка файлу `groups.xml`

    groups_xml = base_path / "groups.xml"
    incoming_value = get_group_incoming(groups_xml, "5")
    print("Значення timingExbytes/incoming для group number=5:")
    print(incoming_value)