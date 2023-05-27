sid_save = ""
current_state = 1
break_state = 0
v = 0
def get_sid_save():
    return sid_save

def get_current_state():
    return current_state

def set_current_state(state):
    global current_state
    current_state = state

def get_break_state():
    return break_state

def set_break_state(state):
    global break_state
    break_state = state

def get_v():
    return v

def set_v(vnew):
    global v
    v = vnew