def get_id():
    file = open("id_pw.txt", 'r')
    lines = [line.rstrip() for line in file]
    get_id = lines[0]
    
    return get_id

def get_pw():
    file = open("id_pw.txt", 'r')
    lines = [line.rstrip() for line in file]
    get_pw = lines[1]
    
    return get_pw

def check():
    id = input("id: ")
    pw = input("pw: ")
    
    g_id = get_id()
    g_pw = get_pw()
    
    if id == g_id and pw == g_pw:
        passed = True
    else: passed = False
    return passed