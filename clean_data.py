import pandas as pd
import json

url = "https://github.com/mdrilwan/datasets/raw/master/flights.csv"
df = pd.read_csv(url)


def parse_location(location_str):
    location = json.loads(location_str.replace('""', '"'))
    return float(location["lat"]), float(location["lon"])


df["DestLatitude"], df["DestLongitude"] = zip(*df["DestLocation"].apply(parse_location))

df["OrigLatitude"], df["OrigLongitude"] = zip(
    *df["OriginLocation"].apply(parse_location)
)

df.drop(columns=["DestLocation", "OriginLocation"], inplace=True)

df["AvgTicketPrice"] = (
    df["AvgTicketPrice"].replace({"\$": "", ",": ""}, regex=True).str.strip()
)

df["AvgTicketPrice"] = pd.to_numeric(df["AvgTicketPrice"], errors="coerce")

df.to_csv("clean_flights.csv", index=False)

print("Cleaned data has been saved to 'clean_flights.csv'")
