

df = pd.read_excel('../data/work/Michelia/Chl value and Coverage in Pixels.xlsx')

class_mask = df['Reef Groups'].isin(['Sediment', 'Turf Algae', 'Cyanobacterial mat'])

pxsum = df1.groupby(['Reef Groups', 'Depth']).sum()["Number of Pixels"]
print(pxsum)
pxsum2 = pxsum.reset_index()
print(pxsum2)
print(pxsum2.describe())

import matplotlib.pyplot as plt

import seaborn as sns

sns.barplot(data=pxsum2, x='Number of Pixels', hue='Depth', y='Reef Groups',)
#plt.xscale('log')
plt.tight_layout()
plt.savefig('pixel count chl.jpg')

pxsum2.to_excel('pixel count chl.xlsx')