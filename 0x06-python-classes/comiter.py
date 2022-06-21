import os
import subprocess

files = os.listdir()
for file in files:
	if file != "comiter.py":
		subprocess.run(['git', 'add', file])
		subprocess.run(['git', 'commit', '-m', file])

