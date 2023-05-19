sid_save = ""
current_state = 1

def get_sid_save():
    return sid_save

def get_current_state():
    return current_state

def set_current_state(state):
    global current_state
    current_state = state
