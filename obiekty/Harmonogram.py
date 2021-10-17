

dniTygodnia= ["Po","Wt", "Sr","Cz","Pt","So","Ni"]

class Harmonogram:
    dnitygodnia = dict()

    def __init__(self):
        for dzien in dniTygodnia:
            dniTygodnia[dzien]={}

    