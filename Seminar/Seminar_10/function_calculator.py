import emoji

def calc(example):
    try:
        return eval(example)
    except:
        return f'А чё, так можно было...' + emoji.emojize('🤓\n')