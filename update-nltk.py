import subprocess

subprocess.run('python -m nltk.downloader all', shell=True, stdout=subprocess.PIPE)
