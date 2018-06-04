import codecs
import ioutils as util
import numpy as np
from representations.sequentialembedding import SequentialEmbedding
from tqdm import tqdm
from scipy.spatial import distance


def build_approximity(word, neighbours, vocab, it, year):
    word_neighbours = neighbours[it].split()
    word_vector = []
    #word_2_neighbours = neighbours2[it].split()
    for token in vocab:
        if token in word_neighbours:
            word_vector.append(fiction_embeddings.get_sim(year, word, token))
        else:
            word_vector.append(0)
    if year == 1900:
        matrix1900[it] = word_vector
    else:
        matrix1990[it] = word_vector


def count_distance(wiki, lurk, file):
    if lurk.any() and wiki.any():
        res = 1 - distance.cosine(wiki, lurk)
    else:
        res = 0
    if np.isnan(res):
        res = 0
    #print(res)
    file.write(str(res))
    file.write(u'\r\n')


if __name__ == "__main__":
    fiction_embeddings = SequentialEmbedding.load("embeddings/eng-fiction-all_sgns", range(1900, 2000, 90))
    with codecs.open('common_words_1.txt', 'r', 'utf-8') as inp:
        common = []
        for line in inp:
            elem = line.strip()
            common.append(elem)
    print(len(common))
    common = common[36000:]

    vocabulary = sorted(util.load_pickle('embeddings/eng-fiction-all_sgns/1900-vocab.pkl'))[5000:]
    #vocabulary2 = vocabulary[16000:32000]
    #vocabulary3 = vocabulary[32000:48000]
    #vocabulary4 = vocabulary[48000:64000]
    #vocabulary5 = vocabulary[64000:80000]
    #vocabulary6 = vocabulary[80000:]

    matrix1900 = np.empty([len(common), len(vocabulary)])
    matrix1990 = np.empty([len(common), len(vocabulary)])
    print(matrix1900.shape)

    with codecs.open('vocabulary1900_1.txt', 'r', 'utf-8') as inp1:
        neighbours_list = []
        for line in inp1:
            elem = line.strip()
            neighbours_list.append(elem)
        print('Neighbours list has been built')
    print(len(neighbours_list))
    neighbours_list = neighbours_list[36000:]
    i = 0
    for item in tqdm(common):
        build_approximity(item, neighbours_list, vocabulary, i, 1900)
        i += 1

    with codecs.open('vocabulary1990_1.txt', 'r', 'utf-8') as inp1:
        neighbours_list = []
        for line in inp1:
            elem = line.strip()
            neighbours_list.append(elem)
        print('Neighbours list has been built')
    print(len(neighbours_list))
    neighbours_list = neighbours_list[36000:]

    i = 0
    for item in tqdm(common):
        build_approximity(item, neighbours_list, vocabulary, i, 1990)
        i += 1
    dist = codecs.open('distances_neighb19.txt', 'w', 'utf-8')
    for i in tqdm(range(len(matrix1900))):
        count_distance(matrix1900[i], matrix1990[i], dist)
    dist.close()
