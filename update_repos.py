import os
import sys

os.chdir('/Users/eirik/Downloads/VCV-Rack/Rack/community')

reset-repo = 'git reset HEAD ---hard'
update-repo = 'git pull'

os.system(reset-repo)
os.system(update-repo)
