import yaml
import pickle
import matplotlib

matplotlib.use('agg')
from matplotlib import colors as mcolors

with open('colormap.yml', 'r') as stream:
    color_mapping = yaml.safe_load(stream)

label_encoder = {}
encoded_colormap = {}
listed_colors = []
for i, (label, color) in enumerate(color_mapping.items(), 1):
    label_encoder[label] = i
    encoded_colormap[i] = color
    listed_colors.append(color)

with open('label_encoder.yml', 'w') as stream:
    yaml.safe_dump(label_encoder, stream)

print(f'Saved label encoder to label_encoder')

with open('encoded_colormap.yml', 'w') as stream:
    yaml.safe_dump(encoded_colormap, stream)

print(f'Saved label encoder to encoded_colormap')

N = len(listed_colors)
cmap_name = f'curacao_detailed'
cmap = mcolors.ListedColormap(listed_colors,
                              name=cmap_name,
                              N=len(encoded_colormap)
                              )
cmap.set_bad('k')  # Set NaN pixels to black
cmap.set_under('k')

print(f'Made colormap {cmap}: detailed')
with open('colormap.pkl', 'wb') as fp:
    pickle.dump(cmap, fp)

