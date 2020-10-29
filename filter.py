import pandas as pd
data = pd.read_csv("/Users/woutervanrijmenam/stack/02_Projects/04_Sites/RSL/data/userReviews.csv", sep=";")
# print(data.head())
# print(data[:3])
# print(data.movieName.iloc[1])
column_names = ['movieName', 'Metascore_w', 'Author', 'AuthorHref', 'Summary','origin_rating']
author_db = pd.DataFrame(columns = column_names)
recomendations = pd.DataFrame(columns = column_names)

for i, r in data.iterrows():
    if data.movieName.iloc[i] == "beach-rats":
        current_rating = r["Metascore_w"]
        author_db = author_db.append(pd.DataFrame({'movieName': r['movieName'], 'Metascore_w': r['Metascore_w'] , 'Author': r['Author'], 'AuthorHref': r['AuthorHref'], 'Summary': r['Summary'], 'origin_rating': current_rating}, index=[0]), ignore_index=True)

for index, r in author_db.iterrows():
    author = r["Author"]
    current_rating = r["origin_rating"]

    print(author)
    print(current_rating)
    for i, r in data.iterrows():
        if data.Author.iloc[i] == author:
            if r["Metascore_w"] > current_rating:
                print("--", r['movieName'], "-", r["Metascore_w"])
                recomendations = recomendations.append(pd.DataFrame({'movieName': r['movieName'], 'Metascore_w': r['Metascore_w'] , 'Author': r['Author'], 'AuthorHref': r['AuthorHref'], 'Summary': r['Summary'], 'origin_rating': current_rating}, index=[0]), ignore_index=True)


# print("--- Recom coming -----")
# print(recomendations)
recomendations.to_csv("recomendations.csv", sep=';')