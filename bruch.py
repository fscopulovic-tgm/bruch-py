import math
class Bruch:
    """
    class Bruch initialisiert bis zu zwei Nummern als Bruch
    """

    def __init__(self, *args):
        """
        Konstruktor erstellt einen Bruch
        Zudem prüft er noch ob der Nenner 0 ist und
        ob Nenner und Zaehler beide ganzzahlig sind

        :param *args: Liste, die Zahler und Nenner uebergibt. Kann auch nur eine Zahl oder eine Klasse Bruch uebergeben
        """
        if len(args) == 1:
            if isinstance(args[0], Bruch):
                self.zaehler = args[0].zaehler
                self.nenner = args[0].nenner
            elif isinstance(args[0], int):
                self.zaehler = args[0]
                self.nenner = 1
            else:
                raise TypeError
        elif len(args) == 2:
            self.zaehler = args[0]
            self.nenner = args[1]
        else:
            raise ValueError("Mehr als 2 Parameter sind nicht erlaubt")

        if self.nenner == 0:
            raise ZeroDivisionError("Division durch 0 nicht möglich")
        elif isinstance(self.nenner, float) or isinstance(self.zaehler, float):
            raise TypeError("Zaehler und Nenner müssen ganzzahlig sein")

    def __float__(self):
        """
        Der Bruch wird als float-Wert zurueckgeliefert

        :return: float
        """
        return float(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Der Bruch wird als komplexe Zahl zurueckgeliefert

        :return: complex
        """
        return complex(self.zaehler / self.nenner)

    def __int__(self):
        """
        Der Bruch wird als int-Wert zurueckgeliefert

        :return: int
        """
        return  int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Zaehler und Nenner werden vertauscht zurueckgeliefert

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        Der Bruch wird als String umgewandelt und zurueckgeliefert

        :return: string
        """
        if self.nenner == 1:
            return '(%s)' % (str(self.zaehler))
        else:
            return '(%s,%s)' % (str(self.zaehler),self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Potenziert den Bruch mit dem Parameter power

        :param power: int
        :return: int
        """
        return Bruch(self.zaehler ** power, self.nenner ** power)

    def __abs__(self):
        """
        Zaehler und Nenner werden als absolute Zahlen in einem Bruch zurueckgeliefert

        :return: Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    @staticmethod
    def __makeBruch(value):
        """
        Zaehler wird als value zuruckgeliefert

        :return: int
        """
        if isinstance(value, int):
            return Bruch(value, 1)
        else:
            raise TypeError("Value ist keine ganzzahlige Zahl")

    def __neg__(self):
        """
        Gibt negativiert den Zaehler und den Nenner eines Bruches

        :return: ìnt
        """
        return Bruch(-self.zaehler, -self.nenner)

    def __add__(self, other):
        """
        Addiert zwei Brueche, die mit + addiert werden

        :param other: int oder Bruch
        :return: Bruch
        """
        help_other = Bruch(other)
        kgv = help_other.nenner * self.nenner // math.gcd(help_other.nenner, self.nenner)
        help_zaehler = (self.zaehler * help_other.nenner) + (help_other.zaehler * self.nenner)
        return Bruch(help_zaehler, kgv)

    def __iadd__(self, other):
        """
        Addiert zwei Brüche, die mit += addiert werden

        :param other: int oder Bruch
        :return: Bruch
        """
        self.__add__(other)

    def __radd__(self, other):

        """
        Addiert einen int-Type mit einem Bruch-Type, die mit + addiert werden

        :param other: int or Bruch
        :return: Bruch
        """
        help_other = Bruch(other)
        kgv = help_other.nenner * self.nenner // math.gcd(help_other.nenner, self.nenner)
        help_zaehler = (self.zaehler * help_other.nenner) + (help_other.zaehler * self.nenner)
        return Bruch(help_zaehler, kgv)

    def __truediv__(self, other):
        """
        Dividiert einen Bruch-Wert durch einen int-Wert oder einen Bruch-Wert, der / geschrieben wurde

        :param other: int oder Bruch
        :return: Bruch
        """
        kehrwert = ~Bruch(other)
        if not kehrwert.nenner == 0:
            return self * kehrwert
        else:
            raise ZeroDivisionError

    def __itruediv__(self, other):
        """
        Dividiert einen Bruch-Wert durch einen int-Wert oder einem Bruch-Wert, der /= geschrieben wurde

        :param other: int`` oder Bruch
        :return: Bruch
        """
        self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        Dividiert einen Bruch-Wert

        :param other:
        :return: Bruch
        """
        self.__truediv__(other)

    def __mul__(self, other):
        """

        :param other: int or Bruch
        :return: Bruch
        """
        help_bruch = Bruch(other)
        return Bruch(self.zaehler * help_bruch.zaehler, self.nenner * help_bruch.nenner)

    def __imul__(self, other):
        """
        Ruft die __mul__-Methode auf

        :param other: int oder Bruch
        :return: Bruch
        """
        self.__mul__(other)

    def __rmul__(self, other):
        """
        Ruft die __mul__ Methode auf

        :param other: int oder Bruch
        :return: Bruch
        """
        self.__mul__(other)
