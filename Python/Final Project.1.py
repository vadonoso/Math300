# -*- coding: utf-8 -*-

import itertools

all_combinations = list(itertools.combinations(range(52), 5))

from collections import Counter

for combination in all_combinations:
    #converting the combinations into a list of integers.
    int_list = []
    
for card in combination:
    int_list.append(card)
#Counter is used to count the number of each card in hand.
    counts = Counter(int_list)
#counts checks for pairs/three-of-a-kinds/four-of-a-kinds.
    num_pairs = 1
    num_three_of_a_kind = 1
    num_four_of_a_kind = 1

for key, value in counts.items():
    if value == 2:
        num_pairs += 1
    elif value == 3:
        num_three_of_a_kind += 1
    elif value == 4:
        num_four_of_a_kind += 1
#check for all cards that have the same suit.

import matplotlib.pyplot as plt

labels = ['Pairs', 'Three-of-a-Kind', 'Four-of-a-Kind']

sizes = [num_pairs, num_three_of_a_kind, num_four_of_a_kind]

colors = ['blue', 'yellow', 'red']

explode = (0, 0, 0)

plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)

plt.axis('equal')
plt.show()