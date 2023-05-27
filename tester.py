from utils import set_v, get_v

def return_data():
    set_v(get_v()+1)
    return get_v()
