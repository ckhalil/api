import subprocess

def githubcommande():
    my_file = open("com.txt", "r")
    print(my_file.read())
    subprocess.call("git add .")
    subprocess.call("git commit -m 'jalil'")
    subprocess.call("git push")


githubcommande()