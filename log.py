log_file = "image.log"

def log(msg):
    with open(log_file, "a") as f:
        f.write(msg +"\n")

def dump_log():
    with open(log_file, "r") as f:
        print(f.read())