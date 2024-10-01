import pandas as pd

url = "./data/clean_flights.csv"
df = pd.read_csv(url)

print(df.columns)

# print(df.dtypes)

df["AvgTicketPrice"] = df["AvgTicketPrice"].astype("float")
print(df.dtypes)

df.to_csv("./data/clean_code.csv", index=False)
