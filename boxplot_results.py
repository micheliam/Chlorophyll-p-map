import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1= pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data1.csv')
df2= pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data2.csv')

#COVERAGE
#depth coverage plot
#Coral
plt.figure()
sns.boxplot(data=df1, y='Coverage', hue='Depth', x='Species')
plt.title('Top 5 Coral Species in different depths')
plt.xlabel("Species")
plt.ylabel("Coverage(%)")
plt.show()
plt.savefig('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/results_boxplot_coral_depth_coverage.png')
#Others
plt.figure()
sns.boxplot(data=df2, y='Coverage', hue='Depth', x='Species')
plt.title('Macroalgae, Corallinales and Microbial mats in different depths')
plt.xlabel("Reef Groups")
plt.ylabel("Coverage(%)")
plt.show()
plt.savefig('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/results_boxplot_microbialmacroalgae_depth_coverage.png')

#infra coverage plot
#Coral
plt.figure()
f=sns.boxplot(data=df1, y='Coverage', hue='InfrastructureN', x='Species')
plt.title('Top 5 Coral Species in different levels of infrastructure')
plt.xlabel("Species")
plt.ylabel("Coverage(%)")
f.legend(title="Infrastructure Density")
plt.show()
plt.savefig('results_boxplot_coral_infra_coverage.png')
#Others
plt.figure()
f=sns.boxplot(data=df2, y='Coverage', hue='InfrastructureN', x='Species')
plt.title('Macroalgae, Corallinales and Microbial mats in different levels of infrastructure')
plt.xlabel("Reef Groups")
plt.ylabel("Coverage(%)")
f.legend(title="Infrastructure Density")
plt.show()

plt.savefig('results_boxplot_microbialmacroalgae_infra_coverage.png')


#CHL
#depth chl plot
#Coral
plt.figure()
sns.boxplot(data=df1, y='AvgChl', hue='Depth', x='Species')
plt.title('Top 5 Coral Species in different depths')
plt.xlabel("Species")
plt.ylabel("Chl-p")
plt.show()
plt.savefig('results_boxplot_top5coral_depth_chl.png')
#Others
plt.figure()
sns.boxplot(data=df2, y='AvgChl', hue='Depth', x='Species')
plt.title('Macroalgae, Corallinales and Microbial mats in different depths')
plt.xlabel("Reef Groups")
plt.ylabel("Chl-p")
plt.show()
plt.savefig('results_boxplot_macrobialmicroalgae_depth_chl.png')

#infra chl plot
#Coral
plt.figure()
f=sns.boxplot(data=df1, y='AvgChl', hue='InfrastructureN', x='Species')
plt.title('Top 5 Coral Species in different levels of infrastructure')
plt.xlabel("Species")
plt.ylabel("Chl-p")
f.legend(title="Infrastructure Density")
plt.show()
plt.savefig('results_boxplot_top5coral_infran_chl.png')
#Others
plt.figure()
f=sns.boxplot(data=df2, y='AvgChl', hue='InfrastructureN', x='Species')
plt.title('Macroalgae, Corallinales and Microbial mats in different levels of infrastructure')
plt.xlabel("Reef Groups")
plt.ylabel("Chl-p")
f.legend(title="Infrastructure Density")
plt.show()
plt.savefig('results_boxplot_macrobialmicroalgae_infra_chl.png')


#pxsum2.to_excel('pixel count chl.xlsx')

########
Dual Panels
for class_group in class_groups: # 2 groupings of 5 classes each
    for class_name in class_group:
         for variable in [chl, coverage]:
                  a dual panel plot with top-panel is a box-whisker plot for variable, and bottom panel is the bar plot for the mean of the variable.





#
#import pandas as pd

#dx1= pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data.csv')

#depth
#pxsum = dx1.groupby(['Species', 'Depth']).sum()["Coverage transect2"]
#pxsumx = dx1.groupby(['Species', 'Depth'])
#print(pxsumx)
#pxsumx

#print(pxsum)
#pxsum2 = pxsum.reset_index()
#print(pxsum2)
#print(pxsum2.describe())

#infrastructure
#pxsumB = dx1.groupby(['Species', 'Infrastructure']).sum()["Coverage transect2"]
#print(pxsumB)
#pxsum2B = pxsumB.reset_index()
#print(pxsum2B)
#print(pxsum2B.describe())


#example
#plt.figure()
#ax = sns.boxplot(x="Species", y="Coverage", hue='Depth', data=dx1)
#plt.show()
#dx1["Pixels"]