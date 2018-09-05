import open from os


fh = open("messages.log", "w")
fh.write(message + "\n")
