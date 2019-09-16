import subprocess
import os
import requests

pageSaved = open('page.html', 'w+')

requestedURL = input('URL: ')

page = requests.get(requestedURL)

pageSaved.write(page.text)

subprocess.Popen('page.html', shell=True)

subprocess.run(['git', 'push'])