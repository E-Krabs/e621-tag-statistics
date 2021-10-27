import json
import collections
import pandas as pd
import matplotlib.pyplot as plt

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
                wordcount[word] += 1# Print most common word
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(30):
        print(word, ": ", count)# Close the file

    lst = word_counter.most_common(30)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')
    plt.title('Tags (957,625)')
    plt.show()