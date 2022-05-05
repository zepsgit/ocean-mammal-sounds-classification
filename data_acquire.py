###################################
# read the data information file data.csv to get the file names
###############################
import pandas as pd
metadata = pd.read_csv('./src/data.csv')
metadata_sample=metadata.head(11)
print(metadata_sample)

import requests
filename="61025001.wav"
url = 'https://cis.whoi.edu/science/B/whalesounds/WhaleSounds/{filename}'.format(filename=filename)
r = requests.get(url, allow_redirects=True)
open('./data/{filename}'.format(filename=filename), 'wb').write(r.content)
