import pandas as pd

data = pd.read_csv("/Users/woutervanrijmenam/stack/02_Projects/04_Sites/RSL/data/userReviews.csv", sep=";")

# print(data.head())
# print(data[:3])
# print(data.movieName.iloc[1])

column_names = ['movieName', 'Metascore_w', 'Author', 'AuthorHref', 'Summary','origin_rating']

subset = pd.DataFrame(columns = column_names)
author_db = pd.DataFrame(columns = column_names)

recomendations = pd.DataFrame(columns = column_names)

# for movie in range(100):
#     if data.movieName.iloc[movie] == "beach-rats":
#         row=data[movie:movie + 1]
#         print(row['Author'])
#         subset.append(row)

for index, row in data.iterrows():
    if data.movieName.iloc[index] == "beach-rats":
        print(row["Author"])
        # author_name = row["Author"]

        # print(row["Summary"])
        current_rating = row["Metascore_w"]
        # if(row["Metascore_w"] >= 6):
        subset = subset.append(pd.DataFrame({'movieName': row['movieName'], 'Metascore_w': row['Metascore_w'] , 'Author': row['Author'], 'AuthorHref': row['AuthorHref'], 'Summary': row['Summary']}, index=[0]), ignore_index=True)

        for i,r in data.iterrows():
            if data.Author.iloc[i] == row["Author"]:
                author_db = author_db.append(pd.DataFrame({'movieName': r['movieName'], 'Metascore_w': r['Metascore_w'] , 'Author': r['Author'], 'AuthorHref': r['AuthorHref'], 'Summary': r['Summary']}, index=[0]), ignore_index=True)

                
        for i,r in author_db.iterrows():
            if r['Metascore_w'] > current_rating:
                recomendations = recomendations.append(pd.DataFrame({'movieName': r['movieName'], 'Metascore_w': r['Metascore_w'] , 'Author': r['Author'], 'AuthorHref': r['AuthorHref'], 'Summary': r['Summary'], 'origin_rating': current_rating}, index=[0]), ignore_index=True)




# print("--- subset coming -----")
print(author_db)
# print("--- Recom coming -----")
# print(recomendations)
recomendations.to_csv("recomendations.csv", sep=';')
