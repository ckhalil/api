import subprocess

def githubcommande():

    subprocess.call("git add .")
    subprocess.call("git commit -m 'jalil'")
    subprocess.call("git push")


githubcommande()