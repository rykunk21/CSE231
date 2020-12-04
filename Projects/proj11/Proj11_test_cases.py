
#    CT attack method
##############################################################################
from pokemon import Move,Pokemon
from random import seed
seed(2)
m_L = [Move('rock-throw','rock',50,90,2), Move('hyper-fang','normal',80,90,2), Move('comet-punch','normal',18,85,2), Move('pay-day','normal',40,100,2)]
p2 = Pokemon('pidgeot','normal','flying',m_L,83,80,75,70,70)
m_L2 =[Move('slam','normal',80,75,2), Move('thunder-punch','electric',75,100,2), Move('thunderbolt','electric',90,100,3), Move('thunder','electric',110,70,3)]
p1 = Pokemon('pikachu','electric','',m_L2,35,55,40,50,50)
print(p1)
print(p2)
print("Attack #1")
print("{} hp before:{}".format(p2.get_name(),p2.get_hp()))
p1.attack(Move('thunderbolt','electric',90,100,3),p2)
print("{} hp after:{}".format(p2.get_name(),p2.get_hp()))
assert p2.get_hp() == 0
print('-'*20)
m_L3=[Move('bubble','water',40,100,3), Move('rock-throw','rock',50,90,2), Move('bone-club','ground',65,85,2), Move('dig','ground',80,100,2)]
m_L4=[Move('wrap','normal',15,90,2), Move('horn-attack','normal',65,100,2), Move('self-destruct','normal',200,100,2), Move('egg-bomb','normal',100,75,2)]
p2 = Pokemon('pidgeot','normal','flying',m_L4,83,80,75,70,70)
p3 = Pokemon('rhydon','ground','rock',m_L3,105,130,120,45,45)
print(p2)
print(p3)
print("Attack #2")
print("{} hp before:{}".format(p2.get_name(),p2.get_hp()))
p3.attack(Move('bone-club','ground',65,85,2),p2)
print("{} hp after:{}".format(p2.get_name(),p2.get_hp()))
assert p2.get_hp() == 83
print('-'*20)
print("Attack #3")
print(p2)
print(p3)
print("{} hp before:{}".format(p3.get_name(),p3.get_hp()))
p2.attack(Move('egg-bomb','normal',100,75,2),p3)
print("{} hp after:{}".format(p3.get_name(),p3.get_hp()))
assert p3.get_hp() == 84
print('-'*20)

#    CT move
##############################################################################
from pokemon import Move
m = Move('rock-throw','rock',50,90,2)
s = m.__str__()
assert s == 'rock-throw'
s = m.__repr__()
assert s == 'rock-throw'
s = m.get_name()
assert s == 'rock-throw'
s = m.get_element()
assert s == 'rock'
i = m.get_power()
assert i == 50
i = m.get_accuracy()
assert i == 90
i = m.get_attack_type()
assert i == 2

#    CT Pokemon
##############################################################################
from pokemon import Move,Pokemon
m_L4=[Move('wrap','normal',15,90,2), Move('horn-attack','normal',65,100,2), Move('self-destruct','normal',200,100,2), Move('egg-bomb','normal',100,75,2)]
p2 = Pokemon('pidgeot','normal','flying',m_L4,83,80,75,70,70)
s = p2.__str__()
s2 = '''pidgeot        83             80             75             70             70
normal         flying
wrap           horn-attack    self-destruct  egg-bomb'''
print("Instructor:")
print(s2)
print("Student:")
print(s)
# kludge to compare multi-line strings -- it wasn't working in Mimir
s2_L = s2.split("\n")
s_L = s.split("\n")
for i in range(3):
	assert s2_L[i].strip() == s_L[i].strip()
s = p2.get_name()
assert s == 'pidgeot'
s = p2.get_element1()
assert s == 'normal'
s = p2.get_element2()
assert s == 'flying'
i = p2.get_hp()
assert i == 83
i = p2.get_patt()
assert i == 80
i = p2.get_pdef()
assert i == 75
i = p2.get_satt()
assert i == 70
i = p2.get_sdef()
assert i == 70
#check move list
M = p2.get_moves()
assert M == m_L4
i = p2.get_number_moves()
assert i == 4
# check choose
m = p2.choose(2)
assert m == Move('self-destruct','normal',200,100,2)

# FT add moves
##############################################################################


from pokemon_inst import Move, Pokemon
from proj11 import add_moves,read_file_moves
fp_moves = open("moves.csv")
move_list = read_file_moves(fp_moves)
fp_moves.close()
p = Pokemon('charmeleon','fire','',None,58,64,58,80,65)
success = add_moves(p,move_list)
m_list = p.get_moves()
m_list2 = [Move('slam','normal',80,75,2), Move('fire-blast','fire',110,85,3), Move('fire-spin','fire',35,85,3), Move('ember','fire',40,100,3)]
print("Call #1")
print("Instructor:")
print(m_list2)
print("Student:")
print(m_list)
assert m_list == m_list2
print("-"*30)
print("Call #2")
#p2 = Pokemon('ekans','poison','',None,35,60,44,40,54)
p2 = Pokemon('dragonair','dragon','',None,61,84,65,70,70)
print(p2)
success = add_moves(p2,move_list)
print("the second call to add_moves should fail, i.e. return False")
assert success == False

# FT choose pokemon
##############################################################################
from pokemon_inst import Pokemon
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

# FT read file moves
##############################################################################


from proj11 import read_file_moves
from pokemon_inst import Move
fp = open("moves_tiny.csv")
m_list = read_file_moves(fp)
m_list2 = [Move('pound','normal',40,100,2), Move('karate-chop','fighting',50,100,2), Move('cut','normal',50,95,2), Move('vine-whip','grass',45,100,2)]
print("Instructor:", m_list2)
print("Student:",m_list)
assert m_list == m_list2


# FT read file pokemon
##############################################################################
from pokemon_inst import Pokemon
from proj11 import read_file_pokemon
fp = open("pokemon_tiny.csv")
pokemon_list = read_file_pokemon(fp)
p_list=[Pokemon('bulbasaur','grass','poison',None,45,49,49,65,65), Pokemon('ivysaur','grass','poison',None,60,62,63,80,80), Pokemon('venusaur','grass','poison',None,80,82,83,100,100), Pokemon('charmander','fire','',None,39,52,43,60,50), Pokemon('charmeleon','fire','',None,58,64,58,80,65), Pokemon('charizard','fire','flying',None,78,84,78,109,85), Pokemon('squirtle','water','',None,44,48,65,50,64)]
print("Instructor:")
print(p_list)
print("Student:")
print(pokemon_list)
assert pokemon_list == p_list
