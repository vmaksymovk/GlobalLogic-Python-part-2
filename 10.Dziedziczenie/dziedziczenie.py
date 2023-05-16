from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self):
        self._pole = None
        self._obwod = None

    @abstractmethod
    def oblicz_pole(self):
        pass

    @abstractmethod
    def oblicz_obwod(self):
        pass

    def get_pole(self):
        return self._pole

    def get_obwod(self):
        return self._obwod


class Kwadrat(Figura):
    def __init__(self, bok):
        super().__init__()
        self._bok = bok

    def oblicz_pole(self):
        self._pole = self._bok ** 2

    def oblicz_obwod(self):
        self._obwod = 4 * self._bok


class Kolo(Figura):
    def __init__(self, promien):
        super().__init__()
        self._promien = promien

    def oblicz_pole(self):
        self._pole = 3.14 * self._promien ** 2

    def oblicz_obwod(self):
        self._obwod = 2 * 3.14 * self._promien


kwadrat = Kwadrat(7)
kwadrat.oblicz_pole()
kwadrat.oblicz_obwod()
print(f"Kwadrat - pole: {kwadrat.get_pole()}, obwód: {kwadrat.get_obwod()}")

kolo = Kolo(7)
kolo.oblicz_pole()
kolo.oblicz_obwod()
print(f"Koło - pole: {kolo.get_pole()}, obwód: {kolo.get_obwod()}")
