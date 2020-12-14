##############################################################################
#   Computer proj 11
#
#   Design a program that can read pokemon and move data, and allow two users
#   to simulate a pokemon battle similar to the real game version
#
#   Algorithm:
#       create and init data types for both a move and a pokemon
#       define methods for pokemon and moves that include all necessary
#       calls for proj11.py
#
##############################################################################
from random import randint
import math

# DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'},
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'},
                           'electric': {'water', 'flying'},
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock',
                                        'steel'},
                           'fire': {'bug', 'grass', 'ice', 'steel'},
                           'flying': {'bug', 'fighting', 'grass'},
                           'ghost': {'ghost', 'psychic'},
                           'grass': {'water', 'ground', 'rock'},
                           'ground': {'electric', 'fire', 'poison', 'rock',
                                      'steel'},
                           'ice': {'dragon', 'flying', 'grass', 'ground'},
                           'normal': set(),
                           'poison': {'fairy', 'grass'},
                           'psychic': {'fighting', 'poison'},
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {
    'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost', 'poison', 'steel'},
    'dragon': {'steel'},
    'dark': {'dark', 'fairy', 'fighting'},
    'electric': {'dragon', 'electric', 'grass'},
    'fairy': {'fire', 'poison', 'steel'},
    'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'},
    'fire': {'dragon', 'fire', 'rock', 'water'},
    'flying': {'electric', 'rock', 'steel'},
    'ghost': {'dark'},
    'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'},
    'ground': {'bug', 'grass'},
    'ice': {'fire', 'ice', 'steel', 'water'},
    'normal': {'rock', 'steel'},
    'poison': {'ghost', 'ground', 'poison', 'rock'},
    'psychic': {'psychic', 'steel'},
    'rock': {'fighting', 'ground', 'steel'},
    'steel': {'electric', 'fire', 'steel', 'water'},
    'water': {'dragon', 'grass', 'ice'}
    }

no_effect_dictionary = {'electric': {'ground'},
                        'dragon': {'fairy'},
                        'fighting': {'ghost'},
                        'ghost': {'normal', 'psychic'},
                        'ground': {'flying'},
                        'normal': {'ghost'},
                        'poison': {'steel'},
                        'psychic': {'dark'},

                        'bug': set(), 'dark': set(), 'fairy': set(),
                        'fire': set(),
                        'flying': set(), 'grass': set(), 'ice': set(),
                        'rock': set(), 'steel': set(), 'water': set()
                        }


# Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name="", element="normal", power=20, accuracy=80,
                 attack_type=2):
        """ Initialize attributes of the Move object """

        self.name = name
        self.element = element
        self.power = power

        self.accuracy = accuracy
        self.attack_type = attack_type  # attack_type is 1, 2 or 3
        # 1 - status moves, 2 - physical attacks, 3 - special attacks

    def __str__(self):
        """
            returns the name of the move
            :return str
        """
        return str(self.name)

    def __repr__(self):
        """
            returns the name of the move
            :return str
        """
        return self.__str__()

    def get_name(self):
        """
            returns the name of the move
            :return str
        """
        return self.name

    def get_element(self):
        """
            returns the element of the move
            :return str
        """
        return self.element

    def get_power(self):
        """
            returns the power of a move
            :return int
        """
        return self.power

    def get_accuracy(self):
        """
            returns accuracy of the move
            :return int
        """
        return self.accuracy

    def get_attack_type(self):
        """
            returns an integer representation of the attack type
            :return int
        """
        return self.attack_type

    def __eq__(self, m):
        """ return True if all attributes are equal; False otherwise """
        return self.name == m.get_name() and self.element == m.get_element() and \
               self.power == m.get_power() and self.accuracy == m.get_accuracy() and \
               self.attack_type == m.get_attack_type()


class Pokemon(object):
    def __init__(self, name="", element1="normal", element2="", moves=None,
                 hp=100, patt=10, pdef=10, satt=10, sdef=10):
        """ initializes attributes of the Pokemon object """

        self.name = name
        self.element1 = element1
        self.element2 = element2

        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef

        self.moves = moves

        try:
            if len(moves) > 4:
                self.moves = moves[:4]

        except TypeError:  # For Nonetype
            self.moves = list()

    def __eq__(self, p):
        """return True if all attributes are equal; False otherwise"""
        return self.name == p.name and \
               self.element1 == p.element1 and \
               self.element2 == p.element2 and \
               self.hp == p.hp and \
               self.patt == p.patt and \
               self.pdef == p.pdef and \
               self.satt == p.satt and \
               self.sdef == p.sdef and \
               self.moves == p.moves

    def __str__(self):
        """
            returns a string representation of the pokemon in 3 lines
            line 1: name, hp, patt, sdef, satt, sdef
            line 2: element 1, element 2
            line 3: moves
            :return str
        """
        pull =  '{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n' \
               '{:<15}{:<15}\n'.format(
                self.name,
                self.hp,
                self.patt,
                self.pdef,
                self.satt,
                self.sdef,
                self.element1,
                self.element2,
                )
        for move in self.get_moves():
            if move:
                pull += '{:15}'.format(move.get_name())
        return pull

    def __repr__(self):
        """
            returns the same as __str__ for display in the shell
            :return str
        """
        return self.__str__()

    def get_name(self):
        """
            returns name attribute
            :return str
        """
        return self.name

    def get_element1(self):
        """
            returns element 1 attribute
            :return str
        """
        return self.element1

    def get_element2(self):
        """
            returns element 2 attribute
            :return str
        """
        return self.element2

    def get_hp(self):
        """
            returns hp of pokemon
            :return int
        """
        return self.hp

    def get_patt(self):
        """
            returns patt attribute
            :return int
        """
        return self.patt

    def get_pdef(self):
        """
            returns pdef attribute
            :return int
        """
        return self.pdef

    def get_satt(self):
        """
            returns satt attribute
            :return int
        """
        return self.satt

    def get_sdef(self):
        """
            returs sdef attribute
            :return int
        """
        return self.sdef

    def get_moves(self):
        """
            returns moves
            :return list or None
        """
        return self.moves

    def get_number_moves(self):
        """
            returns the number of moves
            :return int
        """
        if self.moves:
            return len(self.moves)
        else:
            return 0

    def choose(self, index):
        """
            accepts an index and returns the corresponding move
            :return move object or None
        """
        if self.moves:
            return self.moves[index]
        else:
            return self.moves

    def show_move_elements(self):
        """
            Displays the elements of the pokemon’s moves
            (each in a 15-space field, left justified)
            :return
        """
        if self.moves:
            print('{:<15}\n{:<15}\n{:<15}\n{:<15}'.format(
                *self.moves
            ))
        return

    def show_move_power(self):
        """
            Displays the power of the pokemon’s moves
            (each in a 15-space field, left justified)
            :return
        """
        if self.moves:
            print('{:<15}\n{:<15}\n{:<15}\n{:<15}'.format(
                *[move.get_power() for move in self.moves]
            ))
        return

    def show_move_accuracy(self):
        """
            Displays the accuracy of the pokemon’s moves
            (each in a 15-space field, left justified)
            :return
        """
        if self.moves:
            print('{:<15}\n{:<15}\n{:<15}\n{:<15}'.format(
                *[move.get_accuracy() for move in self.moves]
            ))
        return

    def add_move(self, move):
        """
           Adds the move parameter to the list of moves for this pokemon
           if this pokemon has three or less moves
           :return
        """

        if len(self.moves) < 4:
            self.moves.append(move)
        return

    def attack(self, move, opponent):
        """
          This method takes the move used by the attacker (self) and deals
          damage to the opponent (who should also be an instance of class
          Pokemon).
          :return
        """
        # extract power of move
        mp = move.get_power()
        modifier = 1.0

        # determine attacks and defense
        if isinstance(opponent, Pokemon):
            attack_type = move.get_attack_type()    # check this
            if attack_type == 2:
                attk = self.get_patt()
                dfnce = opponent.get_pdef()
            elif attack_type == 3:
                attk = self.get_satt()
                dfnce = opponent.get_sdef()
            else:
                print('Invalid attack_type, turn skipped.')
                return
        else:
            raise TypeError('Pokemon can only attack another Pokemon!')

        if move.get_accuracy() <= randint(0, 100):
            print('Move missed!')
            return

        else:
            usr_elements = [elem for elem in [self.get_element1(),
                            self.get_element2()] if elem]

            opponent_elements = [elem for elem in [opponent.get_element1(),
                                 opponent.get_element2()] if elem]

            for elem in opponent_elements:
                if any(elem in is_effective_dictionary[usr] for usr in usr_elements):
                    modifier *= 2

                if any(elem in not_effective_dictionary[usr] for usr in usr_elements):
                    modifier *= .5

                if any(elem in no_effect_dictionary[usr] for usr in usr_elements):
                    modifier = 0

            if modifier > 1:
                print('It\'s super effective!!!!')
            elif 0 < modifier < 1:
                print('Not very effective...')
            elif modifier == 0:
                print('No effect!')
                return

            if move.get_element() in usr_elements:
                modifier *= 1.5

            damage = (((mp * (attk / dfnce) * 20) / 50) + 2) * modifier

            if damage > 0:
                opponent.subtract_hp(damage)

            return

    def subtract_hp(self, damage):
        """
             takes the damage variable and subtracts it from the hp of the
             Pokemon object.
             :param damage int
             :return
        """
        self.hp = math.ceil(self.hp-damage) if self.hp-damage > 0 else 0
