import os
import subprocess

files = os.listdir()
for file in files:
	if file != "commit.py" and file != "main.py":
		subprocess.run(['git', 'add', file])
		subprocess.run(['git', 'commit', '-m', file])