import os
import regex
import time
from aktalib import get_text, get_lines, extract_turkish_body, trklower, show_time
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

t0 = time.time()
# find all text files in the aktadata directory
aktalist = []
for root, dirs, files in os.walk("./duzyazilar001/project_gutenberg"):
    for file in files:
        if file.endswith(".txt"):
            aktalist.append(os.path.join(root, file))

# create a dictionary to store the word frequencies
wordfreq = Counter()

# loop through each text file and calculate the frequency of each word
for filename in aktalist:
    content = get_text(filename)
    trtext = extract_turkish_body(content)
    trtext = trklower(trtext)
    words = regex.findall(r'[\p{L}\d]+', trtext)
    # words = re.findall(r'\w+', trtext)
    wordfreq.update(words)

# print the results
print("Total word count:", sum(wordfreq.values()))
for word, count in wordfreq.most_common(500):
    print(f"{word}: {count}")

show_time("\nTotal time", t0)

# Generate a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=70).generate_from_frequencies(wordfreq)

# Display the WordCloud using Matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()