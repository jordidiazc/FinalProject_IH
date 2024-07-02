SUMMER BOOK RECOMMENDER
In this project, from a database and with the help of Streamlit I have created a website that recommends books. 
In addition, I have carried out a data analysis of the database that has helped me later to be able to design the website in the most optimal way.

To carry out this project I have used this database 'GoodReads_100k_books.csv', which you will find in the link below.
https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k/code

I have done the part of cleaning and preparing the database with Jupyter Notebook (Python)
These are the main changes I have made:
1) The genres of the books were all together in a column, I have separated each one into a column and then I have done a mapping to create a list of 18 genres and their subgenres.
2) You have grouped the values of the 'pages' column into -300, 300-600 and more than 600 pages.
3) I have created a column where the percentage of worst books on the list appears

I have done the part of analyzing the database mainly with Tableau.
Since I had to present the project and I did not want there to be excessive graphics, what I have sought is to try to optimize each of them by putting the most important information in the smallest number of graphics as long as it is understood and the information has correlation.

For the design of the website I used Streamlit, which was the first time I used it and it was quite a challenge.
1) First I focused on trying to understand how it worked and testing a little
2) Once I understood a little what was going on, I started creating the structure of the website
3) Finally, once I had the main structure, I worked on the details so that the website looked as pleasant to the eyes as possible.


The conclusions of my analysis are the following:
    - The most popular books are those that have less than 400 pages
    - Curiously, the books best valued by readers are those with the most pages
    - If we want a light book with a paperback format to go to the beach, it would be best to opt for a drama or romance book

I hope you found my work interesting, if you have any questions do not hesitate to contact me.

I leave you the link of the website below so that you can evaluate the result of my work.

                        https://summerbookrecommender.streamlit.app/