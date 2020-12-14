##
## Class PetError -- complete
##

class PetError(ValueError):
    pass


##
## Class Pet -- not complete
##

class Pet(object):
    accept = ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']

    def __init__(self, species=None, name=""):

        if species:
            if species.lower() not in Pet.accept:
                raise PetError()
            else:
                self.species_str = species.title()
                self.name_str = name.title()

        else:
            raise PetError()

    def __str__(self):
        if self.name_str != '':
            result_str = "Species of {:s}, named {:s}".format(self.species_str,
                                                              self.name_str)
        else:
            result_str = "Species of {:s}, unnamed".format(self.species_str)

        return result_str


##
## Class Dog
##

class Dog(Pet):
    def __init__(self, name='', chases='Cats'):
        super().__init__(species='Dog', name=name)
        self.chases_str = chases.title()

    def __str__(self):

        result_str = '{}, chases {}'.format(
            super().__str__(),
            self.chases_str
        )

        return result_str

##
## Class Cat
##


class Cat(Pet):
    def __init__(self, name='', hates='Dog'):
        super().__init__(species='Cat', name=name)
        self.hates_str = hates

    def __str__(self):

        result_str = '{}, hates {}'.format(
            super().__str__(),
            self.hates_str
        )
        return result_str
