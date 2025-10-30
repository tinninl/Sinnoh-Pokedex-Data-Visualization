import pandas as pd
from config import JSON_CLEAN_FILENAME, CSV_SINNOH_POKEDEX_FILENAME, CSV_SINNOH_POKEDEX_TOP_TENS_FILENAME

df = pd.read_json(JSON_CLEAN_FILENAME)

# export csv
df.to_csv(CSV_SINNOH_POKEDEX_FILENAME, index=False)

# Create a csv with the top ten pokemon in each stat, including total stats
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

top_tens = pd.DataFrame(columns=['No', 'Name', 'Stat', 'Value'])
stats = list(range(4, df.shape[1]))  

# Loop through each stat column 
for col in stats:
    stat_name = df.columns[col]
    top10 = df.sort_values(by=df.columns[col], ascending=False).head(10)

    temp = pd.DataFrame({
        'No': top10.iloc[:, 0],
        'Name': top10.iloc[:, 1],
        'Stat': stat_name,
        'Value': top10.iloc[:, col]
    })

    top_tens = pd.concat([top_tens, temp], ignore_index=True)

# Export to CSV
top_tens.to_csv(CSV_SINNOH_POKEDEX_TOP_TENS_FILENAME,index=False)



