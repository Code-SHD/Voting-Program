import random

id_list = "1234567890"
pw_list = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*"

def create_id():
    id = []
    for i in range(10):
        id.append(random.choice(id_list))
    return id

def create_pw():
    pw = []
    for i in range(15):
        pw.append(random.choice(pw_list))
    return pw

def main():
    file = open("id_pw.txt", 'w')
    id = create_id()
    pw = create_pw()
    id = ("".join(id))
    pw = ("".join(pw))
    d_id = "%s\n" %id
    d_pw = "%s" %pw
    file.write(d_id)
    file.write(d_pw)
    return id, pw