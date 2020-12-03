from Projects.proj10 import cards
from Projects.proj10.proj10 import move_to_foundation

foundation = [[], [], [], []]
print("Initial foundation:", foundation)
deck = [cards.Card(1,1),cards.Card(2,1),cards.Card(3,1),cards.Card(4,1),cards.Card(5,1),cards.Card(6,1),cards.Card(7,1),cards.Card(8,1),cards.Card(9,1),cards.Card(10,1),cards.Card(11,1),cards.Card(12,1),cards.Card(13,1),cards.Card(1,2),cards.Card(2,2),cards.Card(3,2),cards.Card(4,2),cards.Card(5,2),cards.Card(6,2),cards.Card(7,2),cards.Card(8,2),cards.Card(9,2),cards.Card(10,2),cards.Card(11,2),cards.Card(12,2),cards.Card(13,2),cards.Card(1,3),cards.Card(2,3),cards.Card(3,3),cards.Card(4,3),cards.Card(5,3),cards.Card(6,3),cards.Card(7,3),cards.Card(8,3),cards.Card(9,3),cards.Card(10,3),cards.Card(11,3),cards.Card(12,3),cards.Card(13,3),cards.Card(1,4),cards.Card(2,4),cards.Card(3,4),cards.Card(4,4),cards.Card(5,4),cards.Card(6,4),cards.Card(7,4),cards.Card(8,4),cards.Card(9,4),cards.Card(10,4),cards.Card(11,4),cards.Card(12,4),cards.Card(13,4)]
sequence1 = []
for i in range(13):
    sequence1.append(deck.pop())
sequence2 = []
for i in range(13):
    sequence2.append(deck.pop())
c1 = cards.Card(1,1)  # AC
c2 = cards.Card(11,2)  # 2C
c3 = cards.Card(3,1)  # 3C
c4 = cards.Card(12,2)  # QD
c5 = cards.Card(5,1)   # 3D
c6 = cards.Card(6,2)   # 6D
tableau = [[c1,c2,c3],[],sequence1,[c4,c5,c6],[],[],sequence2]
instructor_tableau = [[c1,c2,c3],[],[],[c4,c5,c6],[],[],[]]
instructor_foundation = [sequence1[:],sequence2[:],[],[]]
print("Initial tableau:")
print(tableau)
move_to_foundation(tableau,foundation)
print("Instructor tableau:")
print(instructor_tableau)
print("Student tableau:")
print(tableau)
print("Instructor foundation:")
print(instructor_foundation)
print("Student foundation:")
print(foundation)
assert instructor_foundation==foundation and instructor_tableau==tableau