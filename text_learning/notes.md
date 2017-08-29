### `parse_out_text(f)`

- extract text of an email;
- remove punctuation;
- stem with `nltk.SnowballStemmer`; (1)

### `vectorize_text()`

- remove signature words;
- remove english stopwords with `sklearn tf-idf`; (2)
- vectorize with `sklearn tf-idf`; (3)



    