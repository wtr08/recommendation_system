import pandas as pd


data = pd.read_csv("/Users/woutervanrijmenam/stack/02_Projects/04_Sites/RSL/data/userReviews.csv", sep=";")


# Setting up the column names for storing. 
# Additional the origin_rating is added for storing the score that the author gives for the specific movie and to compare it later on
column_names = ['movieName', 'Metascore_w', 'Author', 'AuthorHref', 'Summary','origin_rating']

df = pd.DataFrame(columns = column_names)
# Setting up author DB to store temporairy authors 
author_db = pd.DataFrame(columns = column_names)

# Output database. Here the recomendations of films will be stored
recomendations = pd.DataFrame(columns = column_names)

# Loop through the all the data 
for r in data.itertuples():
    # Specify the movie 
    if r.movieName == "i-am-legend":
        # Store the current current rating into current_rating variable. Just for convenience 
        current_rating = r.Metascore_w
        # Store all authors that reacted on the specifice movie
        author_db = author_db.append(pd.DataFrame({'movieName': r.movieName, 'Metascore_w': r.Metascore_w , 'Author': r.Author, 'AuthorHref': r.AuthorHref, 'Summary': r.Summary, 'origin_rating': current_rating}, index=[0]), ignore_index=True)

# Loop through the author Database
for r in author_db.itertuples():
    # Setup variables to test and compare later on
    author = r.Author
    current_rating = r.origin_rating

    print(author)
    print(current_rating)

    # Loop through the data set again and specify if the right author
    for r in data.itertuples():
        if r.Author == author:
            # Compare all the movies that author reacted and if it is higher than the given score on the previous specific film 
            if r.Metascore_w > current_rating:
                print("--", r.movieName, "-", r.Metascore_w)
                # Store the result in the recomendations database 
                recomendations = recomendations.append(pd.DataFrame({'movieName': r.movieName, 'Metascore_w': r.Metascore_w, 'Author': r.Author, 'AuthorHref': r.AuthorHref, 'Summary': r.Summary, 'origin_rating': current_rating}, index=[0]), ignore_index=True)


# print("--- Recom coming -----")
# print(recomendations)

# Export to CSV 
recomendations.to_csv("recomendations.csv", sep=';')