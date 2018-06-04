# -*- coding: utf-8 -*-
import codecs
import sensegram
from tqdm import tqdm

model1 = sensegram.SenseGram.load_word2vec_format('model/lurkmore_plus_lem.txt.senses.w2v', binary=True)
#model2 = sensegram.SenseGram.load_word2vec_format('model/lurk_rus_stem.txt.senses.w2v', binary=True)

words = []
with codecs.open('wiki_lurk common_vocabulary.txt', 'r', 'utf-8') as common:
    for line in common:
        words.append(line.strip())
words.sort()
first_sense = codecs.open('lurk_first_sense_neighbours.txt', 'w', 'utf-8')
second_sense = codecs.open('lurk_second_sense_neighbours.txt', 'w', 'utf-8')
third_sense = codecs.open('lurk_third_sense_neighbours.txt', 'w', 'utf-8')
forth_sense = codecs.open('lurk_forth_sense_neighbours.txt', 'w', 'utf-8')
first_sense2 = codecs.open('lurk_first_sense_neighbours2.txt', 'w', 'utf-8')
second_sense2 = codecs.open('lurk_second_sense_neighbours2.txt', 'w', 'utf-8')
third_sense2 = codecs.open('lurk_third_sense_neighbours2.txt', 'w', 'utf-8')
forth_sense2 = codecs.open('lurk_forth_sense_neighbours2.txt', 'w', 'utf-8')
first_sense_words = []
second_sense_words = []
third_sense_words = []
forth_sense_words = []
for word in tqdm(words):
    sense_counter = 0
    for sense in model1.get_senses(word):
        if sense[1] > 0.2:
            #sense_num = sense[0][]
            if sense_counter == 0:
                first_sense_words.append(word)
                for neighbour in model1.most_similar(sense[0]):
                    if neighbour[1] > 0.5:
                        first_sense.write(neighbour[0][:-2])
                        first_sense.write(' ')
                        for neighbour_of_neighbour in model1.most_similar(neighbour[0]):
                            first_sense2.write(neighbour_of_neighbour[0][:-2])
                            first_sense2.write(' ')
                first_sense.write(u'\r\n')
                first_sense2.write(u'\r\n')
            elif sense_counter == 1:
                second_sense_words.append(word)
                for neighbour in model1.most_similar(sense[0]):
                    if neighbour[1] > 0.5:
                        second_sense.write(neighbour[0][:-2])
                        second_sense.write(' ')
                        for neighbour_of_neighbour in model1.most_similar(neighbour[0]):
                            second_sense2.write(neighbour_of_neighbour[0][:-2])
                            second_sense2.write(' ')
                second_sense.write(u'\r\n')
                second_sense2.write(u'\r\n')
            elif sense_counter == 2:
                third_sense_words.append(word)
                for neighbour in model1.most_similar(sense[0]):
                    if neighbour[1] > 0.5:
                        third_sense.write(neighbour[0][:-2])
                        third_sense.write(' ')
                        for neighbour_of_neighbour in model1.most_similar(neighbour[0]):
                            third_sense2.write(neighbour_of_neighbour[0][:-2])
                            third_sense2.write(' ')
                third_sense.write(u'\r\n')
                third_sense2.write(u'\r\n')
            else:
                forth_sense_words.append(word)
                for neighbour in model1.most_similar(sense[0]):
                    if neighbour[1] > 0.5:
                        forth_sense.write(neighbour[0][:-2])
                        forth_sense.write(' ')
                        for neighbour_of_neighbour in model1.most_similar(neighbour[0]):
                            forth_sense2.write(neighbour_of_neighbour[0][:-2])
                            forth_sense2.write(' ')
                forth_sense.write(u'\r\n')
                forth_sense2.write(u'\r\n')
            sense_counter += 1
print(len(first_sense_words))
print(len(second_sense_words))
print(len(third_sense_words))
print(len(forth_sense_words))
with codecs.open('lurk_first_sense_words.txt', 'w', 'utf-8') as outp:
    for word in first_sense_words:
        outp.write(word)
        outp.write(u'\r\n')
with codecs.open('lurk_second_sense_words.txt', 'w', 'utf-8') as outp:
    for word in second_sense_words:
        outp.write(word)
        outp.write(u'\r\n')
with codecs.open('lurk_third_sense_words.txt', 'w', 'utf-8') as outp:
    for word in third_sense_words:
        outp.write(word)
        outp.write(u'\r\n')
with codecs.open('lurk_forth_sense_words.txt', 'w', 'utf-8') as outp:
    for word in forth_sense_words:
        outp.write(word)
        outp.write(u'\r\n')