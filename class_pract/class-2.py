#!/usr/bin/python3
# inheritance, polymorphism and Magic methods

class Animal:
    def __init__(self, birthType="unknown", appearance="unknown",
                 blooded="unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__,
                                                     self.birthType,
                                                     self.appearance,
                                                     self.blooded)


class Mammal(Animal):
    def __init__(self, birthType="born Alive", appearance="hair or fur",
                 blooded="warmblooded", nurseYoung="True"):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__()+"and it is {} they" \
            " nurse their young".format(self.nurseYoung)


def main():
    animal1 = Animal("born Alive")
    print(animal1.birthType)
    animal2 = Mammal()
    print(animal2)


if __name__ == "__main__":
    main()
