# The method of using NLTK's stopwords lists to detect language is from Alejandro Nolla: https://github.com/z0mbiehunt3r

import sys
import nltk

try:
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print '[!] You need to install nltk (http://nltk.org/index.html)'

def lang_detection():
    danish_sent=[]
    dutch_sent=[]
    english_sent=[]
    finnish_sent=[]
    french_sent=[]
    german_sent=[]
    hungarian_sent=[]
    italian_sent=[]
    norwegian_sent=[]
    portuguese_sent=[]
    russian_sent=[]
    spanish_sent=[]
    swedish_sent=[]
    turkish_sent=[]
    
    
    print "Welcome! Please enter the names of the text file you'd like to analyze in the format [filename].txt"
    text1 = raw_input("Filename: ")
    with open(text1, 'r') as file:
        text = file.read()
        sent_text = nltk.sent_tokenize(text) # This gives us a list of sentences
# Now loop over each sentence and tokenize it separately
        for sentence in sent_text:
            tokenized_text = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(tokenized_text)

            languages_ratios = {}

            tokens = wordpunct_tokenize(sentence)
            words = [word.lower() for word in tokens]
            
            for language in stopwords.fileids():
                stopwords_set = set(stopwords.words(language))
                words_set = set(words)
                common_elements = words_set.intersection(stopwords_set)

                languages_ratios[language] = len(common_elements) # language "score"

                ratios = languages_ratios

                most_rated_language = max(ratios, key=ratios.get)

                language = most_rated_language
            
            
            if language == "danish": 
                danish_sent.append(sentence)
                print language
            
            elif language == "english": 
                english_sent.append(sentence)
                print language
         
            elif language == "french":
                french_sent.append(sentence)
                print language
        
         
        if danish_sent:
            dan_file = open("danish.txt", "w")
            for item in danish_sent:
                dan_file.write(str(item) + '\n')
        
        if dutch_sent:
            dut_file = open("dutch.txt", "w")
            for item in dutch_sent:
                dut_file.write(str(item) + '\n')
                        
        if english_sent:
            eng_file = open("english.txt", "w")
            for item in english_sent:
                eng_file.write(str(item) + '\n')
                
        if finnish_sent:
            fin_file = open("finnish.txt", "w")
            for item in finnish_sent:
                fin_file.write(str(item) + '\n')        
                
        if french_sent:
            fra_file = open("french.txt", "w")
            for item in french_sent:
                fra_file.write(str(item) + '\n')
                
        if german_sent:
            ger_file = open("german.txt", "w")
            for item in german_sent:
                ger_file.write(str(item) + '\n')
        
        if hungarian_sent:
            hun_file = open("hungarian.txt", "w")
            for item in hungarian_sent:
                hun_file.write(str(item) + '\n')
        
        if italian_sent:
            ita_file = open("italian.txt", "w")
            for item in ita_sent:
                ita_file.write(str(item) + '\n')
          
        if norwegian_sent:
            nor_file = open("norwegian.txt", "w")
            for item in norwegian_sent:
                nor_file.write(str(item) + '\n')  
                
        if portuguese_sent:
            por_file = open("portuguese.txt", "w")
            for item in portuguese_sent:
                por_file.write(str(item) + '\n')
                
        if russian_sent:
            rus_file = open("russian.txt", "w")
            for item in russian_sent:
                rus_file.write(str(item) + '\n')        
                
        if spanish_sent:
            spa_file = open("spanish.txt", "w")
            for item in spanish_sent:
                spa_file.write(str(item) + '\n')  
                
        if swedish_sent:
            swe_file = open("swedish.txt", "w")
            for item in swedish_sent:
                swe_file.write(str(item) + '\n')
                
        if turkish_sent:
            tur_file = open("turkish.txt", "w")
            for item in turkish_sent:
                tur_file.write(str(item) + '\n')
        
        start_over = raw_input("Would you like to run the program again? Type 'y' for yes and 'n' for no.")
        if start_over == "y":
            lang_detection()
        if start_over == "n":
            print "Bye!"
            exit(0)
        else: 
            print("Please enter a valid input.")        
            
lang_detection()
