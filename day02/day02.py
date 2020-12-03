# find passwords that match a pattern

import pandas as pd

df = pd.read_csv('day2_passwords.csv',sep=': ')
df[['lims', 'letter']] = df["rule"].str.split(" ", 1, expand=True)
df[['min_char','max_char']] = df["lims"].str.split("-", 1, expand=True)
df['min_char'] = df.min_char.astype(int)
df['max_char'] = df.max_char.astype(int)
df['valid'] = False

for i, row in df.iterrows():
    counts = row.password.count(row.letter)
    if (counts>= row.min_char) & (counts<=row.max_char):
        df['valid'][i] = True
        
print("Solution 1 is "+str(len(df[df.valid])))

df['valid_two'] = False

for i, row in df.iterrows():
    pwd = row.password
    if (pwd[row.min_char-1]==row.letter) ^ (pwd[row.max_char-1]==row.letter):
        df['valid_two'][i] = True
print("Solution 2 is "+str(len(df[df.valid_two])))
