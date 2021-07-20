import csv
import json
import requests
import pandas as pd
import click
from os.path import join

@click.command()
@click.option('--prov', default=None, help='Filter the dataset by selecting an italian province')
def scrape(prov):
    """Simple program that scrapes the ISS/INFN dashboard and generates
        a csv file with all the data or filtering out only provinces of
        interest. The list of provinces is available in the
        data/province.csv file.
    """
    # Importing province names
    with open(join('data', 'province.csv'), newline='') as f:
        reader = csv.reader(f)
        province = [provincia[0] for provincia in reader]
    dataset_names = ['positivi', 'ricoveri', 'terapia_intensiva', 'deceduti']
    if (province==None):
        # Making the dataframe
        prov_dfs=[]
        i=0
        tot=len(province)
        for provincia in province:
            datasets=[]
            for dataset_name in dataset_names:
                url=f'https://covid19.infn.it/iss/plots/iss_bydate_{provincia}_{dataset_name}.div'
                s=requests.get(url).text
                datasets.append(json.loads(s.split('\n')[11].strip()[:-1])[0]['y'])
            datasets.insert(0, json.loads(s.split('\n')[11].strip()[:-1])[0]['x'])
            df = pd.DataFrame.from_records(zip(*datasets), columns=['datetime', 'new_cases', 'hospitalizations', 'intensive', 'deaths']).dropna()
            df['province'] = provincia
            prov_dfs.append(df)
            print(f'Downloading files and preparing dataframe... {i}/{tot}', end='\r')
            i+=1
        df = pd.concat(prov_dfs)
        print('\nDataframe complete! Converting to csv...')
        # Exporting dataset to csv file
        df.to_csv(join('data', 'covid_iss.csv'), index=False)
        print('Csv file is complete! You can find it under the name data/covid_iss.csv')
    elif (prov in province):
        # Making the dataframe
        datasets=[]
        for dataset_name in dataset_names:
            url=f'https://covid19.infn.it/iss/plots/iss_bydate_{prov}_{dataset_name}.div'
            s=requests.get(url).text
            datasets.append(json.loads(s.split('\n')[11].strip()[:-1])[0]['y'])
        datasets.insert(0, json.loads(s.split('\n')[11].strip()[:-1])[0]['x'])
        df = pd.DataFrame.from_records(zip(*datasets), columns=['datetime', 'new_cases', 'hospitalizations', 'intensive', 'deaths']).dropna()
        df['province'] = prov
        print(f'Downloading file and preparing dataframe for {prov}...')
        print('Dataframe complete! Converting to csv...')
        # Exporting dataset to csv file
        df.to_csv(join('data', f'covid_iss_{prov}.csv'), index=False)
        print(f'Csv file is complete! You can find it under the name data/covid_iss_{prov}.csv')
    elif (prov=='all'):
        i=0
        tot=len(province)
        for provincia in province:
            datasets=[]
            for dataset_name in dataset_names:
                url=f'https://covid19.infn.it/iss/plots/iss_bydate_{provincia}_{dataset_name}.div'
                s=requests.get(url).text
                datasets.append(json.loads(s.split('\n')[11].strip()[:-1])[0]['y'])
            datasets.insert(0, json.loads(s.split('\n')[11].strip()[:-1])[0]['x'])
            df = pd.DataFrame.from_records(zip(*datasets), columns=['datetime', 'new_cases', 'hospitalizations', 'intensive', 'deaths']).dropna()
            df['province'] = provincia
            print(f'Downloading and preparing csv files... {i}/{tot}', end='\r')
            df.to_csv(join('data', f'covid_iss_{provincia}.csv'), index=False)
            i+=1
        print('Csv files are complete! You can find them in the data folder.')
    else:
        print('ERROR: You should specify a valid province, all or not use the option at all.')

if __name__=='__main__':
    scrape()