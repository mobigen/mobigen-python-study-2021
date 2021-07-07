import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("./"), "my_history")
try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

print("ready to write history")
atexit.register(readline.write_history_file, histfile)

# exec(open("/root/python-study/readline/study_readline.py").read())
