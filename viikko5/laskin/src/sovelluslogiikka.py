class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._arvot = [arvo]

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._arvot.append(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._arvot.append(self._arvo)
    def nollaa(self):
        self._arvo = 0
        self._arvot.append(0)
    def aseta_arvo(self, arvo):
        self._arvo = arvo
        self._arvot.append(arvo)
    def arvo(self):
        return self._arvo
    def kumoa(self):
        if len(self._arvot) <=1:
            self._arvo = 0
        else:
            self._arvot.pop()
            self._arvo = self._arvot[-1]

