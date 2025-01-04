def remove_numbers(text):
    import re,string
    if isinstance(text, str):
        return ''.join(char for char in text if not char.isdigit())
    else:
        return     

def remove_character(text):
    import re,string
    if isinstance(text, str): 
        text = text.lower()  
        text = re.sub('https?://\S+|www\.\S+', '', text)  
        text = re.sub(r"\b\d+\b", "", text)  
        text = re.sub('<.*?>+', '', text) 
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text) 
        text = re.sub('\n', '', text)
        text = re.sub('[’“”…]', '', text)
        return text
    else:
        return text

def remove_emoji(text):
    import re,string
    if isinstance(text, str):
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F700-\U0001F77F"
                           u"\U0001F780-\U0001F7FF"    
                           u"\U0001F800-\U0001F8FF"
                           u"\U0001F900-\U0001F9FF"  
                           u"\U0001FA00-\U0001FA6F"  
                           u"\U0001FA70-\U0001FAFF"  
                           u"\U00002702-\U000027B0"  
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    else:
        return text


def remove_short_form(text):
    import re,string
    if isinstance(text, str):
        # removing short form:
        text = re.sub("isn't", 'is not', text)
        text = re.sub("he's", 'he is', text)
        text = re.sub("wasn't", 'was not', text)
        text = re.sub("there's", 'there is', text)
        text = re.sub("couldn't", 'could not', text)
        text = re.sub("won't", 'will not', text)
        text = re.sub("they're", 'they are', text)
        text = re.sub("she's", 'she is', text)
        text = re.sub("There's", 'there is', text)
        text = re.sub("wouldn't", 'would not', text)
        text = re.sub("haven't", 'have not', text)
        text = re.sub("That's", 'That is', text)
        text = re.sub("you've", 'you have', text)
        text = re.sub("He's", 'He is', text)
        text = re.sub("what's", 'what is', text)
        text = re.sub("weren't", 'were not', text)
        text = re.sub("we're", 'we are', text)
        text = re.sub("hasn't", 'has not', text)
        text = re.sub("you'd", 'you would', text)
        text = re.sub("shouldn't", 'should not', text)
        text = re.sub("let's", 'let us', text)
        text = re.sub("they've", 'they have', text)
        text = re.sub("You'll", 'You will', text)
        text = re.sub("i'm", 'i am', text)
        text = re.sub("we've", 'we have', text)
        text = re.sub("it's", 'it is', text)
        text = re.sub("don't", 'do not', text)
        text = re.sub("that´s", 'that is', text)
        text = re.sub("I´m", 'I am', text)
        text = re.sub("it’s", 'it is', text)
        text = re.sub("she´s", 'she is', text)
        text = re.sub("he’s'", 'he is', text)
        text = re.sub('I’m', 'I am', text)
        text = re.sub('I’d', 'I did', text)
        text = re.sub("he’s'", 'he is', text)
        text = re.sub('there’s','there is',text)
        return text
    else:
        return text


def remove_multiple_space(text):
    import re,string
    if isinstance(text, str):
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        return text
    else:
        return text


def detect_english(text):
    from langdetect import detect
    import re,string
    try:
        return detect(text) == 'en'
    except Exception as e:
        #print(f"Error detecting language: {e} - {text}")
        return False

def remove_freqwords(text):

    import re,string
    from collections import Counter
    cnt = Counter()
    FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])
    return " ".join([word for word in str(text).split() if word not in FREQWORDS])
