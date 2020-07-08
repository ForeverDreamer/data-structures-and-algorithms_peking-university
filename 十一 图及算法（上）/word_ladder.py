"""词梯问题"""
from dag import Vertex
from dag import Graph


def extractor(file_name, word_length):
    with open(file_name, 'rt') as rf, open(f'words_{word_length}.txt', 'wt', encoding='utf-8') as wf:
        for line in rf:
            if len(line)-1 == word_length:
                wf.write(line)


def build_graph(word_file):
    d = {}
    g = Graph()

    # Create buckets of words that differ by one letter
    with open(word_file, 'rt') as rf:
        for line in rf:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    # Add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
        # if Graph._num_of_vertex%1000 == 0:
        #     print(g)
    # with open('words_bfs_graph.txt', 'wt', encoding='utf-8') as wf:
    #     wf.write(str(g))

    return g


if __name__ == '__main__':
    # extractor('words_alpha.txt', 4)
    build_graph('words_bfs.txt')
