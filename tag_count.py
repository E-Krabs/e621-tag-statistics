import json
import collections
import pandas as pd
import matplotlib.pyplot as plt

print('# of Words to Display:')
display = input()

directory = 'C:/Scripts/Python/[adjective][species]/'
with open('{}tag-out.json'.format(directory), 'r') as f:
    data = json.load(f)

    wordcount = {}
    for item in data:
        general = item['general']
        for words in general:
            word = words
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(display):
        print('{0}: {1}'.format(word, count))

    lst = word_counter.most_common(display)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')
    plt.title('General (957,625)')
    plt.show()
    plt.savefig('{}General_Tags.png'.format(directory))

    wordcount = {}
    for item in data:
        species = item['species']
        for words in species:
            word = words
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(display):
        print(word, ": ", count)

    lst = word_counter.most_common(display)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')
    plt.title('Species (957,625)')
    plt.show()
    plt.savefig('{}Species_Tags.png'.format(directory))
