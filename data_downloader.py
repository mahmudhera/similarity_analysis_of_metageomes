import pandas as pd
import os

df = pd.read_csv('HMASM.csv')

f = open('downloaded_files_metadata.txt', 'w')

urls_to_download = []
unique_body_sites = df['Body Site'].unique()
for body_site in unique_body_sites:
    body_site_df = df[df['Body Site'] == body_site]
    body_site_df = body_site_df.sort_values('Reads File Size')
    for srs_id, location in zip (body_site_df[:5]['SRS ID'].tolist(), body_site_df[:5]['Reads file location'].tolist()):
        filename = location.split('/')[-1]
        print(f'{body_site}, {srs_id}, {filename}')
        f.write(f'{body_site}, {srs_id}, {filename}\n')
        url_to_download = "https://downloads.hmpdacc.org" + location
        urls_to_download.append(url_to_download)

for url in urls_to_download:
    # download the file using wget
    os.system(f'wget {url}&')
    

