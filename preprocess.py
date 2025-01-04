def preprocess_batch(batch_data):
    import pandas as pd
    from data_func import remove_numbers, remove_character, remove_emoji, remove_short_form, remove_multiple_space, detect_english, remove_freqwords
    from nltk.corpus import stopwords
    stop_words = stopwords.words()

    batch_data.drop([
        "number",
        "review_id",
        "pseudo_author_id",
        "author_name",
        "review_likes",
        "author_app_version",
        "review_timestamp",
    ], inplace=True, axis=1)

    batch_data.rename(columns={'review_text': 'text'}, inplace=True)
    batch_data.rename(columns={'review_rating': 'sentiment'}, inplace=True)

    # Apply preprocessing steps
    batch_data['text'] = batch_data['text'].apply(remove_numbers)
    batch_data['text'] = batch_data['text'].apply(remove_character)
    batch_data['text'] = batch_data['text'].apply(remove_short_form)
    batch_data['text'] = batch_data['text'].apply(remove_multiple_space)

    # Remove empty records and duplicates
    batch_data.drop_duplicates(inplace=True)
    batch_data.dropna(inplace=True)

    # Remove non-English records
    batch_data['is_english'] = batch_data['text'].apply(detect_english)
    batch_data = batch_data[batch_data['is_english']]
    batch_data = batch_data.drop(columns=['is_english'])

    # Remove stop words
    batch_data['text'] = batch_data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

    # Remove most frequent words
    batch_data["text"] = batch_data["text"].apply(lambda text: remove_freqwords(text))

    # Change Rating (0 for negative and 1 for positive sentiment)
    batch_data['sentiment'] = [0 if each in (1, 2, 3) else 1 for each in batch_data.sentiment]

    print("done")

    return batch_data


def preprocess_in_batches(input_file, output_file, batch_size=10000, preprocess_batch = preprocess_batch):
    from preprocess import preprocess_batch
    import pandas as pd
    # Initialize an empty list to store the processed batches
    processed_data = []

    # Read the input file in chunks
    for batch_data in pd.read_csv(input_file, chunksize=batch_size):
        # Preprocess each batch and append the result to the list
        processed_batch = preprocess_batch(batch_data)
        processed_data.append(processed_batch)

    # Concatenate all processed batches
    final_data = pd.concat(processed_data, ignore_index=True)

    # Save the final processed data to a CSV file
    final_data.to_csv(output_file, index=False)
    print(f"Processed data saved to: {output_file}")