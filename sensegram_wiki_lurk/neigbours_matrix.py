import codecs
from tqdm import tqdm


def build_approximity(neighbours, neighbours2, file, vocab, it):
    word_neighbours = neighbours[it].split()
    word_2_neighbours = neighbours2[it].split()
    for token in vocab:
        if token in word_neighbours:
            file.write(' 2')
        elif token in word_2_neighbours:
            file.write(' 2')
        else:
            file.write(' 0')
    file.write(u'\r\n')


def run():
    with codecs.open('wiki_lurk common_vocabulary.txt', 'r', 'utf-8') as inp:
        vocabulary = []
        for line in inp:
            elem = line.strip()
            vocabulary.append(elem)
        print('Vocabulary has been loaded')
    with codecs.open('wiki_first_sense_words.txt', 'r', 'utf-8') as inp:
        iter_vocabulary = []
        for line in inp:
            elem = line.strip()
            iter_vocabulary.append(elem)
        print('Vocabulary has been loaded')
    neighbours_list = []
    with codecs.open('wiki_first_sense_neighbours.txt', 'r', 'utf-8') as inp1:
        for line in inp1:
            elem = line.strip()
            neighbours_list.append(elem)
        print('Model1 neighbours list has been loaded')
    neighbours_2_list = []
    with codecs.open('wiki_first_sense_neighbours2.txt', 'r', 'utf-8') as inp2:
        for line in inp2:
            elem = line.strip()
            neighbours_2_list.append(elem)
        print('Model1 neighbours of neighbours list has been loaded')
    with codecs.open('matrix_numbers_wiki.txt', 'w', 'utf-8') as outp:
        i = 0
        for item in tqdm(iter_vocabulary):
            build_approximity(neighbours_list, neighbours_2_list, outp, vocabulary, i)
            i += 1


run()
