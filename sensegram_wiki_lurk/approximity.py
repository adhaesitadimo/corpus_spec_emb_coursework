import codecs
import math
import numpy as np
import scipy.spatial as sp
from tqdm import tqdm


def count_distance(vect1, vect2, word, file):
    # print(type(vect2))
    # print(vect2.shape)
    # print(type(vect2[0]))
    if len(np.unique(vect1)) == 1 or len(np.unique(vect2)) == 1:
        # print('yes!')
        # print(word)
        res = 0.0
    else:
        res = 1 - sp.distance.cosine(vect1, vect2)
    file.write(str(res))
    file.write(u'\r\n')


def run(vecs_batch_size):
    vocabulary_wiki = []
    with codecs.open('wiki_third_sense_words.txt', 'r', 'utf-8') as vocab:
        for line in vocab:
            vocabulary_wiki.append(line.strip())
    print('Wiki vocabulary has been uploaded')
    #vocabulary_wiki.sort()
    print(len(vocabulary_wiki))
    vocabulary_lurk = []
    with codecs.open('lurk_first_sense_words.txt', 'r', 'utf-8') as vocab:
        for line in vocab:
            vocabulary_lurk.append(line.strip())
    print('Lurk vocabulary has been uploaded')
    #vocabulary_lurk.sort()
    print(len(vocabulary_lurk))
    vocabulary_wiki_set = set(vocabulary_wiki)
    vocabulary_lurk_set = set(vocabulary_lurk)
    vocabulary = list(vocabulary_wiki_set & vocabulary_lurk_set)
    vocabulary.sort()
    print(len(vocabulary))
    indexes_wiki = [vocabulary_wiki.index(word) for word in tqdm(vocabulary)]
    indexes_lurk = [vocabulary_lurk.index(word) for word in tqdm(vocabulary)]
    print(len(indexes_wiki))
    #print(indexes_wiki)
    print(len(indexes_lurk))
    #print(indexes_lurk)
    batches = []
    max_range = max(len(vocabulary_wiki), len(vocabulary_lurk))
    for batch in range(vecs_batch_size - 1):
        batches.append(max_range // vecs_batch_size)
    batches.append(max_range // vecs_batch_size + max_range % vecs_batch_size)
    print(batches)
    dist = codecs.open('neighbours_cosine_distances_31.txt', 'w', 'utf-8')
    batch_count = 0
    for batch in batches:
        vectors_model1 = []
        vectors_model2 = []
        batch_indexes_wiki = indexes_wiki[batch_count:(batch_count + batch)]
        print('Batch: ' + str(len(batch_indexes_wiki)))
        #print(batch_indexes_wiki[-1])
        batch_indexes_lurk = indexes_lurk[batch_count:(batch_count + batch)]
        print('Batch: ' + str(len(batch_indexes_lurk)))
        if len(batch_indexes_wiki):
            print(batch_indexes_wiki[-1])
            print(batch_indexes_lurk[-1])
            batch_count += batch
            model1_matrix = codecs.open('matrix_numbers_wiki3.txt', 'r', 'utf-8')
            model2_matrix = codecs.open('matrix_numbers_lurk.txt', 'r', 'utf-8')
            for i, line in enumerate(model1_matrix):
                if i in batch_indexes_wiki:
                    vect_model1 = np.array(list(map(int, line.strip().split(' '))))
                    vectors_model1.append(vect_model1)
                    if i % 100 == 0:
                        print(i)
                    if i == batch_indexes_wiki[-1]:
                        break
            print('Model1 matrix batch vectors have been downloaded')
            print(len(vectors_model1))
            for i, line in enumerate(model2_matrix):
                if i in batch_indexes_lurk:
                    vect_model2 = np.array(list(map(int, line.strip().split(' '))))
                    vectors_model2.append(vect_model2)
                    if i % 100 == 0:
                        print(i)
                    if i == batch_indexes_lurk[-1]:
                        break
            print('Model2 matrix batch vectors have been downloaded')
            print(len(vectors_model2))
            model1_matrix.close()
            model2_matrix.close()
            for i in tqdm(range(len(vectors_model1))):
                count_distance(vectors_model1[i], vectors_model2[i], vocabulary[i], dist)
            print('Batch distances have been found')
    dist.close()
    with codecs.open('words_senses_31.txt', 'w', 'utf-8') as intersection:
        for word in vocabulary:
            intersection.write(word)
            intersection.write(u'\r\n')


run(12)
