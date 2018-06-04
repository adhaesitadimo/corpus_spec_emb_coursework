import codecs
import ioutils as util
from multiprocessing.dummy import Pool as ThreadPool
from representations.sequentialembedding import SequentialEmbedding
from tqdm import tqdm


dict_neighbours_1900 = {}
dict_neighbours_1990 = {}


def res(word):
    construct_neighbours_list_1900(word)


def res1990(word):
    construct_neighbours_list_1990(word)


def construct_neighbours_list_1900(word):
    neighbours_list = []
    for neighbour in fiction_embeddings.get_seq_closest(word, 1900):
        if neighbour != word and fiction_embeddings.get_sim(1900, word, neighbour) > 0.25:
            neighbours_list.append(neighbour)
            for neighbour_of_neighbour in fiction_embeddings.get_seq_closest(neighbour, 1900):
                if neighbour_of_neighbour not in neighbours_list and \
                                fiction_embeddings.get_sim(1900, neighbour, neighbour_of_neighbour) > 0.25 and \
                        neighbour_of_neighbour != word:
                    neighbours_list.append(neighbour_of_neighbour)
    if len(neighbours_list):
        print(word + ' ' + str(len(neighbours_list)))
        dict_neighbours_1900[word] = neighbours_list


def construct_neighbours_list_1990(word):
    neighbours_list = []
    for neighbour in fiction_embeddings.get_seq_closest(word, 1990):
        if neighbour != word and fiction_embeddings.get_sim(1990, word, neighbour) > 0.25:
            neighbours_list.append(neighbour)
            for neighbour_of_neighbour in fiction_embeddings.get_seq_closest(neighbour, 1990):
                if neighbour_of_neighbour not in neighbours_list and \
                                fiction_embeddings.get_sim(1990, neighbour, neighbour_of_neighbour) > 0.25 and \
                                neighbour_of_neighbour != word:
                    neighbours_list.append(neighbour_of_neighbour)
    if len(neighbours_list):
        print(word + ' ' + str(len(neighbours_list)))
        dict_neighbours_1990[word] = neighbours_list


if __name__ == "__main__":
    fiction_embeddings = SequentialEmbedding.load("embeddings/eng-fiction-all_sgns", range(1900, 2000, 90))
    vocab1900 = sorted(util.load_pickle('embeddings/eng-fiction-all_sgns/1900-vocab.pkl'))
    #construct_neighbours_list(vocab1900)
    '''
    for word in tqdm(vocab1900[5000:]):
        list1900 = []
        for neighbour in fiction_embeddings.get_seq_closest(word, 1900):
            if neighbour != word and fiction_embeddings.get_sim(1900, word, neighbour) > 0.4:
                list1900.append(neighbour)
        if len(list1900):
            dict_neighbours_1900[word] = list1900
    '''
    pool = ThreadPool(8)
    pool.map(res, vocab1900[5000:99965])
    pool.close()
    pool.join()
    print(len(dict_neighbours_1900))

    #with codecs.open('vocabulary1900.txt', 'w', 'utf-8') as outp:
    #    for word in dict_neighbours_1900:
    #        #print(' '.join(dict_neighbours_1900[word]))
    #        outp.write(' '.join(dict_neighbours_1900[word]))
    #        outp.write('\r\n')

    vocab1990 = sorted(util.load_pickle('embeddings/eng-fiction-all_sgns/1990-vocab.pkl'))
    pool = ThreadPool(8)
    pool.map(res1990, dict_neighbours_1900)
    pool.close()
    pool.join()
    '''
    for word in tqdm(dict_neighbours_1900):
        list1990 = []
        for neighbour in fiction_embeddings.get_seq_closest(word, 1990):
            if neighbour != word and fiction_embeddings.get_sim(1990, word, neighbour) > 0.4:
                list1990.append(neighbour)
        if l+en(list1990):
            dict_neighbours_1990[word] = list1990

    #with codecs.open('vocabulary1900.txt', 'utf-8', 'w') as outp:
    #    for word in dict_neighbours_1990:
    #        outp.write(' '.join(dict_neighbours_1990[word]))
    #        outp.write('\r\n')
    '''
    common_words = []
    with codecs.open('common_words_1.txt', 'w', 'utf-8') as outp:
        for word in tqdm(dict_neighbours_1990):
            if word in dict_neighbours_1900:
                common_words.append(word)
                outp.write(word)
                outp.write('\r\n')

    print(len(common_words))

    with codecs.open('vocabulary1900_1.txt', 'w', 'utf-8') as outp:
        for word in common_words:
            outp.write(' '.join(dict_neighbours_1900[word]))
            outp.write('\r\n')
   
    with codecs.open('vocabulary1990_1.txt', 'w', 'utf-8') as outp:
        for word in common_words:
            outp.write(' '.join(dict_neighbours_1990[word]))
            outp.write('\r\n')

