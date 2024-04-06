import pandas as pd
import matplotlib.pyplot as plt

bestseller = pd.read_csv('C:/Users/ahsan/OneDrive/Desktop/couch_to_coder/session_4/bestsellers with categories.csv')
bestseller = bestseller.drop_duplicates(subset='Name',keep='last')

number_of_book_written = bestseller.groupby('Author')[['Name']].count().sort_values("Name",ascending=False).head(10).reset_index()
print(number_of_book_written)

# plt.bar(number_of_book_written.Author,number_of_book_written.Name,color='maroon',width=0.4)
# plt.xlabel("Author")
# plt.ylabel("Number of bestselling books")
# plt.title("Number of bestselling books by author")
# plt.show()

number_of_books_by_genre = bestseller.groupby('Genre')[['Name']].count().sort_values("Name",ascending=False).reset_index().head(10)
print(number_of_books_by_genre)

plt.pie(number_of_books_by_genre.Name,labels=number_of_books_by_genre.Genre)
plt.show()


