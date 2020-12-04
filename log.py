"""The module allowing to read and write in the log file"""

log_file = "image.log"

def log(msg):
    """
    Writes a message in the log file
    :param msg: The message to be written
    """
    with open(log_file, "a") as f:
        f.write(msg +"\n")

def dump_log():
    """
    Prints content pf the log file in the console
    """
    with open(log_file, "r") as f:
        print(f.read())