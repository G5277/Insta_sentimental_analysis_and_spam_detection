def tokenization(data):
    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    cv = CountVectorizer(stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)
    text_counts = cv.fit_transform(data['text'])

    #split dataset
    X_train, X_test, y_train, y_test = train_test_split(text_counts, data['sentiment'], test_size=0.20, random_state=30)

    return X_train, X_test, y_train, y_test