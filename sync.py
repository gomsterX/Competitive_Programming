import os
from datetime import date

os.system("git init")
os.system("git add .")
os.system("git status")
os.system("git commit -m '{}' ".format(date.today()))
os.system('git push -u origin')
