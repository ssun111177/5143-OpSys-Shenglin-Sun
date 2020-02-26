import Input, os
import cat

def history(**kwargs):
    kwargs['params'] = ['historylist']
    cat.cat(**kwargs)
