RUSSET=set('абвгд.....я')
LATSET=set('abcde.....z')

def isLat(word):
    latin = 0 < len(set(word.lower())&LATSET)
    russian = 0 == len(set(word.lower())&RUSSET)
    return latin and russian


RUSSET=set('абвгд.....я')
LATSET=set('abcde.....z')

def getLanguage(word):
    '''
    0 - mixed
    1 - russian
    2 - latin
    '''
    latin = 0 < len(set(word.lower())&LATSET)
    russian = 0 < len(set(word.lower())&RUSSET)

    if latin and not russian:
        return 2
    elif russian and not latin:
        return 1
    else:
        return 0