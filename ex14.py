import os
import pathlib

print(os.path.exists("C:\Windows"))

print(os.path.exists('C:\Windows'))

print(os.path.exists('C:\\Windows'))

print(os.path.exists(r'C:\Windows'))

path = pathlib.Path(r'C:\Intel')

print(path.exists())

print(path.is_dir())

print(path.is_file())

for i in path.iterdir():
    print(i)

for i in path.iterdir():
    print(i.name)

for i in path.glob("**/*"):
    print(i)

path.joinpath("Video")

print(path.joinpath("Video"))