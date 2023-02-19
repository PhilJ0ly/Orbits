import pandas as pd
planets = [
    "mercury",
    "venus",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "sun"
]

def cleanData(planet):

    df = pd.read_csv(f'../DATA/{planet}.csv')


    df = df.drop([' deltadot', ' skyMotion', ' skyMotionPa', ' relVelAng', 'Unnamed: 8'], axis=1)
    df = df.rename(columns={' rightAsc':'RA',' dec':'dec', ' dist':'dist'})

    for index, row in df.iterrows():
        for column in df.columns:
            if str(row[column]).startswith(" "):
                df.at[index, column] = str(row[column]).lstrip()


    df.to_csv(f'../CleanData/{planet}.csv', index=False)

def treatAng(planet):
    df = pd.read_csv(f'../CleanData/{planet}.csv')
    print(df.head())
    for index, row in df.iterrows():
        ra = str(row['RA']).split(' ')
        decKey = 1
        if str(row['dec']).startswith('-'):
            decKey = -1
        dec = str(row['dec']).strip('+').strip('-').split(' ')
        print(ra)
        degRa = (float(ra[0])+float(ra[1])/60+float(ra[2])/3600)*360/24
        degDec = decKey*(float(dec[0])+float(dec[1])/60+float(dec[2])/3600)
        df.at[index, 'RA'] = degRa
        df.at[index, 'dec'] = degDec
    df.to_csv(f'../CleanData/{planet}.csv', index=False)
    print(df.head())


# for i in planets:
    # treatAng(i)
    # cleanData(i)