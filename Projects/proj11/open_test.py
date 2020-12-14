# FT choose pokemon
##############################################################################
from pokemon import Pokemon
from proj11 import choose_pokemon
p_list=[Pokemon('bulbasaur','grass','poison',None,45,49,49,65,65), Pokemon('ivysaur','grass','poison',None,60,62,63,80,80), Pokemon('venusaur','grass','poison',None,80,82,83,100,100), Pokemon('charmander','fire','',None,39,52,43,60,50), Pokemon('charmeleon','fire','',None,58,64,58,80,65), Pokemon('charizard','fire','flying',None,78,84,78,109,85), Pokemon('squirtle','water','',None,44,48,65,50,64)]
p1 = choose_pokemon('3',p_list)
print("Instructor:",Pokemon('venusaur','grass','poison',None,80,82,83,100,100))
print("Student:",p1)
assert p1 ==  Pokemon('venusaur','grass','poison',None,80,82,83,100,100)
p2 = choose_pokemon('charmeleon',p_list)
print("Instructor:",Pokemon('charmeleon','fire','',None,58,64,58,80,65))
print("Student:",p2)
assert p2 == Pokemon('charmeleon','fire','',None,58,64,58,80,65)