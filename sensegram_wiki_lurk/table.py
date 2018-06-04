import codecs
import pandas as pd
from tqdm import tqdm


table = {}

word_struct = {}
with codecs.open('words_senses_11.txt') as sense:
    with codecs.open('neighbours_cosine_distances_11.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki1 -> Lurk1'] = word_struct

word_struct = {}
with codecs.open('words_senses_12.txt') as sense:
    with codecs.open('neighbours_cosine_distances_12.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki1 -> Lurk2'] = word_struct

word_struct = {}
with codecs.open('words_senses_13.txt') as sense:
    with codecs.open('neighbours_cosine_distances_13.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki1 -> Lurk3'] = word_struct

word_struct = {}
with codecs.open('words_senses_14.txt') as sense:
    with codecs.open('neighbours_cosine_distances_14.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki1 -> Lurk4'] = word_struct

word_struct = {}
with codecs.open('words_senses_21.txt') as sense:
    with codecs.open('neighbours_cosine_distances_21.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki2 -> Lurk1'] = word_struct

word_struct = {}
with codecs.open('words_senses_22.txt') as sense:
    with codecs.open('neighbours_cosine_distances_22.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki2 -> Lurk2'] = word_struct

word_struct = {}
with codecs.open('words_senses_23.txt') as sense:
    with codecs.open('neighbours_cosine_distances_23.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki2 -> Lurk3'] = word_struct

word_struct = {}
with codecs.open('words_senses_24.txt') as sense:
    with codecs.open('neighbours_cosine_distances_24.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki2 -> Lurk4'] = word_struct

word_struct = {}
with codecs.open('words_senses_31.txt') as sense:
    with codecs.open('neighbours_cosine_distances_31.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki3 -> Lurk1'] = word_struct

word_struct = {}
with codecs.open('words_senses_32.txt') as sense:
    with codecs.open('neighbours_cosine_distances_32.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki3 -> Lurk2'] = word_struct

word_struct = {}
with codecs.open('words_senses_33.txt') as sense:
    with codecs.open('neighbours_cosine_distances_33.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki3 -> Lurk3'] = word_struct

word_struct = {}
with codecs.open('words_senses_34.txt') as sense:
    with codecs.open('neighbours_cosine_distances_34.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki3 -> Lurk4'] = word_struct

word_struct = {}
with codecs.open('words_senses_41.txt') as sense:
    with codecs.open('neighbours_cosine_distances_41.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki4 -> Lurk1'] = word_struct

word_struct = {}
with codecs.open('words_senses_42.txt') as sense:
    with codecs.open('neighbours_cosine_distances_42.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki4 -> Lurk2'] = word_struct

word_struct = {}
with codecs.open('words_senses_43.txt') as sense:
    with codecs.open('neighbours_cosine_distances_43.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki4 -> Lurk3'] = word_struct

word_struct = {}
with codecs.open('words_senses_44.txt') as sense:
    with codecs.open('neighbours_cosine_distances_44.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Neighbours cosine dist Wiki4 -> Lurk4'] = word_struct

word_struct = {}
with codecs.open('wiki_first_sense_words.txt') as sense:
    with codecs.open('wiki_first_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Wiki first sense neighbours'] = word_struct

word_struct = {}
with codecs.open('wiki_second_sense_words.txt') as sense:
    with codecs.open('wiki_second_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Wiki second sense neighbours'] = word_struct

word_struct = {}
with codecs.open('wiki_third_sense_words.txt') as sense:
    with codecs.open('wiki_third_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Wiki third sense neighbours'] = word_struct

word_struct = {}
with codecs.open('wiki_forth_sense_words.txt') as sense:
    with codecs.open('wiki_forth_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Wiki forth sense neighbours'] = word_struct

word_struct = {}
with codecs.open('lurk_first_sense_words.txt') as sense:
    with codecs.open('lurk_first_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Lurkmore first sense neighbours'] = word_struct

word_struct = {}
with codecs.open('lurk_second_sense_words.txt') as sense:
    with codecs.open('lurk_second_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Lurkmore second sense neighbours'] = word_struct

word_struct = {}
with codecs.open('lurk_third_sense_words.txt') as sense:
    with codecs.open('lurk_third_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Lurkmore third sense neighbours'] = word_struct

word_struct = {}
with codecs.open('lurk_forth_sense_words.txt') as sense:
    with codecs.open('lurk_forth_sense_neighbours.txt') as sense_neighb:
        for line, line_neighb in zip(sense, sense_neighb):
            word = line.strip()
            neighbs = line_neighb.strip()
            word_struct[word] = neighbs
table['Lurkmore forth sense neighbours'] = word_struct
results = pd.DataFrame(data=table)
cols = ['Wiki first sense neighbours', 'Wiki second sense neighbours', 'Wiki third sense neighbours',
        'Wiki forth sense neighbours', 'Lurkmore first sense neighbours', 'Lurkmore second sense neighbours',
        'Lurkmore third sense neighbours', 'Lurkmore forth sense neighbours', 'Neighbours cosine dist Wiki1 -> Lurk1',
        'Neighbours cosine dist Wiki1 -> Lurk2', 'Neighbours cosine dist Wiki1 -> Lurk3',
        'Neighbours cosine dist Wiki1 -> Lurk4', 'Neighbours cosine dist Wiki2 -> Lurk1',
        'Neighbours cosine dist Wiki2 -> Lurk2', 'Neighbours cosine dist Wiki2 -> Lurk3',
        'Neighbours cosine dist Wiki2 -> Lurk4', 'Neighbours cosine dist Wiki3 -> Lurk1',
        'Neighbours cosine dist Wiki3 -> Lurk2', 'Neighbours cosine dist Wiki3 -> Lurk3',
        'Neighbours cosine dist Wiki3 -> Lurk4', 'Neighbours cosine dist Wiki4 -> Lurk1',
        'Neighbours cosine dist Wiki4 -> Lurk2', 'Neighbours cosine dist Wiki4 -> Lurk3',
        'Neighbours cosine dist Wiki4 -> Lurk4']
results = results[cols]
print(results)
results.to_csv('results.csv')