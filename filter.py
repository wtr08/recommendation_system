import pandas as pd

data = pd.read_csv("/Users/woutervanrijmenam/stack/02_Projects/04_Sites/RSL/data/userReviews.csv", sep=";")

# print(data.head())
# print(data[:3])
# print(data.movieName.iloc[1])

column_names = ['movieName', 'Metascore_w', 'Author', 'AuthorHref', 'Summary']

subset = pd.DataFrame(columns = column_names)
recomendations = pd.DataFrame(columns = column_names)

# for movie in range(100):
#     if data.movieName.iloc[movie] == "beach-rats":
#         row=data[movie:movie + 1]
#         print(row['Author'])
#         subset.append(row)

items = []

for index, row in data.iterrows():
    if data.movieName.iloc[index] == "beach-rats":
        print(row["Author"])
        # author_name = row["Author"]

        # print(row["Summary"])
        # print(row["Metascore_w"])
        # if(row["Metascore_w"] >= 6):


        for i,r in data.iterrows():
            if data.Author.iloc[i] == row["Author"]:
                if r["Metascore_w"] > 8:
                    print(r["movieName"])
                    new_row = {'movieName': r['movieName'], 'Metascore_w': r['Metascore_w'] , 'Author': r['Author'], 'AuthorHref': r['AuthorHref'], 'Summary': r['Summary']}
                    items.append(r["movieName"])
                    print("------------")



recomendations = pd.DataFrame(items)
recomendations.to_csv("recomendations.csv", sep=';')
