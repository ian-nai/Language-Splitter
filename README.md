# Language-Splitter
### Python scripts to detect languages in a text and split the text into its component languages. All language detection is done using NLTK's stopwords lists, using a method from [Alejandro Nolla](https://github.com/z0mbiehunt3r).

[line_splitter.py](https://github.com/ian-nai/Language-Splitter/blob/master/line_splitter.py) detects the language of each new line in a .txt file, and [sentence_splitter.py](https://github.com/ian-nai/Language-Splitter/blob/master/sentence_splitter.py) detects the language of each sentence. After completing language detection the scripts will save the lines or sentences in each language to separate text files (e.g., "english.txt").

The following languages are currently supported: Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Russian, Spanish, Swedish, and Turkish.
