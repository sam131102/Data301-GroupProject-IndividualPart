import pandas as pd

def unprocessed(csv_file):
    df = pd.read_csv(csv_file, delimiter = ';')
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
     ##Loads and cleans data by removing redundancy, unused columns and null values
    df1=(df.copy().drop(["player_id","nationality","team","potential"],axis=1,inplace=True).sort_values("overall", ascending = False).reset_index(drop=True)
        ) 
    
    conditions = [
    (df['overall'] >= 85),
    (df['overall'] < 85) & (df['overall'] >=70),
    (df['overall'] < 70)
    ]
    values = ['Gold', 'Silver', 'Bronze']
    df2=(df1.copy())
    df2['Rating'] = np.select(conditions, values)
    
    df3=(df2.copy().rename(columns={"potential": "potential growth"}))
    return df3
    
dfa = unprocessed('/Users/sambhavgarg/Desktop/DATA301/project-group24-project/FIFA-21 Complete.csv')