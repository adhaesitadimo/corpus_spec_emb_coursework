import codecs
import math
from tqdm import tqdm


def count_distance(wiki, lurk, word, file):
    length_wiki = 0
    length_lurk = 0
    product = 0
    for j in range(len(wiki)):
        length_wiki += int(wiki[j]) * int(wiki[j])
        length_lurk += int(lurk[j]) * int(lurk[j])
        product += int(wiki[j]) * int(lurk[j])
    norm_length_wiki = math.sqrt(length_wiki)
    norm_length_lurk = math.sqrt(length_lurk)
    norm = norm_length_wiki * norm_length_lurk
    if norm != 0:
        res = product / norm
    else:
        res = 0
    file.write(str(res))
    file.write(u'\r\n')


if __name__ == "__main__":
    wiki_file = codecs.open('matrix_numbers1900.txt', 'r', 'utf-8')
    lurk_file = codecs.open('matrix_numbers1990.txt', 'r', 'utf-8')
    vectors_wiki = []
    vectors_lurk = []
    for line in tqdm(wiki_file):
        vect_wiki = line.strip().split(' ')
        vectors_wiki.append(vect_wiki)
    print('1900 vectors have been downloaded')
    print(len(vectors_wiki))
    for line in tqdm(lurk_file):
        vect_lurk = line.strip().split(' ')
        vectors_lurk.append(vect_lurk)
    print('1990 vectors have been downloaded')
    wiki_file.close()
    lurk_file.close()
    vocabulary = []
    with codecs.open('common_words.txt', 'r', 'utf-8') as vocab:
        for line in vocab:
            vocabulary.append(line.strip())
    print('Vocabulary has been uploaded')
    dist = codecs.open('distances.txt', 'w', 'utf-8')
    for i in tqdm(range(len(vectors_wiki))):
        count_distance(vectors_wiki[i], vectors_lurk[i], vocabulary[i], dist)
    dist.close()
