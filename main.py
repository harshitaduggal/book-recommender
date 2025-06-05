import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("/content/books[1].csv")
data.head()

book_missing=data[~(data["description"].isna()) &
    ~(data["num_pages"].isna()) &
    ~(data["average_rating"].isna()) &
    ~(data["published_year"].isna())
  
]
book_missing

book_missing['categories'].value_counts().reset_index().sort_values('count', ascending=False)

book_missing['words_in_description']=book_missing['description'].str.split().str.len()

book_missing.loc[book_missing['words_in_description'].between(25,34), "description"]

book_missing_25_words=book_missing[book_missing["words_in_description"] >= 25]
book_missing_25_words

book_missing_25_words["title_and_subtitle"]=(
    np.where(book_missing_25_words["subtitle"].isna(),book_missing_25_words["title"],
    book_missing_25_words[['title','subtitle']].astype(str).agg(":".join,axis=1))
)
book_missing_25_words

book_missing_25_words["tagged_description"]= book_missing_25_words[['isbn13','description']].astype(str).agg(" ".join,axis=1)
book_missing_25_words

(book_missing_25_words
 .drop(['subtitle','missing_description','age_of_book','words_in_description'], axis=1)
 .to_csv("books_cleaned.csv",index=False)
)

