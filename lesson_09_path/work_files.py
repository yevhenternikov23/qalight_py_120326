from pathlib import Path

def read_file(filepath: Path) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        return content

def write_file(filepath: Path, content):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

def append_file(filepath: Path, content):
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(content)

# def processing_file(filepath, content, mode):
# def processing_file(filepath, content="", mode="r"):

def convert_to_path(path:str):
    """Convert string to Path object"""
    file_path = Path(path)
    return file_path

def processing_file(
        filepath: Path | str,
        content: str = "",
        mode: str = "r"
) -> str:
    """
    This processing files

    Args:
        filepath: Path | str
        content: str
        mode: str
    
    Returns:
        str: for read
    """
    # 1 якщо стрінг - перетворити в Path
    if isinstance(filepath, str):
        filepath = convert_to_path(filepath)
    elif not isinstance(filepath, Path):
        raise TypeError("Unsupported filepath type - str or Path is expected")

    if mode not in "raw+":  # ["r", "a", "w", "+"]:
        raise AttributeError("This function support only read, write and append mode")

    with open(filepath, mode, encoding="utf-8") as file:
        if mode == "r":
            file_content = file.read()
            return file_content
        file.write(content)
