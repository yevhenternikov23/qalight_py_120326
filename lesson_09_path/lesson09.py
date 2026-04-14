from pathlib import Path

path_v1 = Path(r"D:\elearning\qalight_py_120326\lesson_09_path\my.txt")
path_v2 = Path("D:\\elearning\\qalight_py_120326\\lesson_09_path\\my.txt")
path_v3 = Path("D:/elearning/qalight_py_120326/lesson_09_path/my.txt")
print(path_v1.is_file())
print(path_v2.is_file())
print(path_v3.is_file())

current_file = Path(__file__)
print(current_file.is_file())
print(current_file)

current_folder = current_file.parent
print(current_folder)

my_txt_path = current_folder / "my.txt"
print(my_txt_path)

project_folder = current_folder.parent  ## current_file.parent.parent
print(project_folder)

try_except_folder = project_folder / "lesson_08_try_exept"
print(try_except_folder)

# for i in try_except_folder.iterdir():
#     print("t>", i)

# for i in current_folder.iterdir():
#     print("c>", i)

def folder_contains(folder: Path, ch=">"):
    for i in folder.iterdir():
        # if i.is_dir():
        #     ch += ch
        #     folder_contains(i, ch)
        print(ch, i)

folder_contains(try_except_folder)
folder_contains(current_folder)

all_folder = [d for d in project_folder.iterdir() if d.is_dir()]
print(all_folder)

all_f = []
for d in project_folder.iterdir():
    if d.is_dir():
        all_f.append(d)
print(all_f)
print(all_f == all_folder)


all_contain = [*project_folder.iterdir()]
print(all_contain)

files = [f for f in project_folder.iterdir() if f.is_file()]
print(files)

print(files[1].suffix)

files_txt = [f for f in project_folder.iterdir() if f.suffix == ".md"]
print(files_txt)

print(my_txt_path.exists())
print("my_txt_path.is_dir",my_txt_path.is_dir())
print("my_txt_path.is_file",my_txt_path.is_file())
print(my_txt_path.suffix)
print(my_txt_path.name)

print(my_txt_path.parent)
print([*my_txt_path.parents])
print(list(my_txt_path.parents))

new_file = current_folder / "new.txt"
print(new_file.exists())

current_directory = Path.cwd()
print("Поточна робоча директорія:", current_directory)

home_directory = Path.home()
print("Домашня директорія користувача:", home_directory)

print("==="*8)

new_folder = current_folder / "home" / "new"
new_folder.mkdir(parents=True, exist_ok=True)

with my_txt_path.open(encoding="utf8") as f:
    content = f.read()
    print(content)

with my_txt_path.open("w", encoding="utf8") as f:
    #f.write(content)
    f.write("якійсь там текст") 

with my_txt_path.open("a", encoding="utf8") as f:
    f.write("\nHello sudent!")


