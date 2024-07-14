import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
df1=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data1.csv')
df2=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data2.csv')


df3=pd.concat([df1,df2])

modelalldepthcov = smf.ols(formula='Coverage ~ C(Species) + Depth', data=df3).fit()
print(modelalldepthcov)
modelalldepthcov=modelalldepthcov.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/modelalldepthcov.txt','w') as f:
    f.write(modelalldepthcov.as_csv())



modelallInfrastructureNcov = smf.ols(formula='Coverage ~ C(Species) + InfrastructureN', data=df3).fit()
print(modelallInfrastructureNcov)
modelallInfrastructureNcov=modelallInfrastructureNcov.summary()

with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/modelallInfrastructureNcov.txt','w') as f:
    f.write(modelallInfrastructureNcov.as_csv())

modelallInfrastructureNchl = smf.ols(formula='AvgChl ~ C(Species) + InfrastructureN', data=df3).fit()
print(modelallInfrastructureNchl)
modelallInfrastructureNchl=modelallInfrastructureNchl.summary()

with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/modelallInfrastructureNchl.txt','w') as f:
    f.write(modelallInfrastructureNchl.as_csv())




#DEPTH
#Orbicella faveolata
Ofaveo= df1[0:23]
df1[0:23]

modelofaveochl = smf.ols(formula='AvgChl ~ Depth', data=Ofaveo).fit()
print(modelofaveochl)
modelofaveocvg= smf.ols(formula='Coverage ~ Depth', data=Ofaveo).fit()
ofaveochl= modelofaveochl.summary()

with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/ofaveochl.txt','w') as f:
    f.write(ofaveochl.as_csv())

ofaveocvg= modelofaveocvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/ofaveocvg.txt','w') as f:
    f.write(ofaveocvg.as_csv())


#Siderastrea siderea
Sidera= df1[23:46]
modelsiderachl = smf.ols(formula='AvgChl ~ Depth', data=Sidera).fit()
siderachl= modelsiderachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/siderachl.txt','w') as f:
    f.write(siderachl.as_csv())
modelsideracvg = smf.ols(formula='Coverage ~ Depth', data=Sidera).fit()
sideracvg= modelsideracvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/sideracvg.txt','w') as f:
    f.write(sideracvg.as_csv())

# Diploria strigosa
Dstrigosa=df1[46:69]
modeldstrigosachl= smf.ols(formula='AvgChl ~ Depth', data=Dstrigosa).fit()
dstrigosachl= modeldstrigosachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/dstrigosaachl.txt','w') as f:
    f.write(dstrigosachl.as_csv())
modeldstrigosacvg= smf.ols(formula='Coverage ~ Depth', data=Dstrigosa).fit()
dstrigosacvg= modeldstrigosacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/dstrigosaacvg.txt','w') as f:
    f.write(dstrigosacvg.as_csv())

#Orbicella annularis
Oannularis=df1[69:92]
modeloannularischl= smf.ols(formula='AvgChl ~ Depth', data=Oannularis).fit()
oannularischl= modeloannularischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/oannularischl.txt','w') as f:
    f.write(oannularischl.as_csv())
modeloannulariscvg= smf.ols(formula='Coverage ~ Depth', data=Oannularis).fit()
oannulariscvg= modeloannulariscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/oannulariscvg.txt','w') as f:
    f.write(oannulariscvg.as_csv())

#Madracis auretenra
Madracis=df1[92:115]
modelmadracischl= smf.ols(formula='AvgChl ~ Depth', data=Madracis).fit()
madracischl=modelmadracischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/madracischl.txt','w') as f:
    f.write(madracischl.as_csv())


modelmadraciscvg= smf.ols(formula='Coverage ~ Depth', data=Madracis).fit()
madraciscvg=modelmadraciscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/madraciscvg.txt','w') as f:
    f.write(madraciscvg.as_csv())

#Corallinales
cca= df2[0:23]
modelccachl = smf.ols(formula='AvgChl ~ Depth', data=cca).fit()
modelccacvg= smf.ols(formula='Coverage ~ Depth', data=cca).fit()
ccachl= modelccachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/ccachl.txt','w') as f:
    f.write(ccachl.as_csv())

ccacvg= modelccacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/ccacvg.txt','w') as f:
    f.write(ccacvg.as_csv())


#Cyanobacterial mat
cmat= df2[23:46]
modelcmatchl = smf.ols(formula='AvgChl ~ Depth', data=cmat).fit()
cmatchl= modelcmatchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/cmatchl.txt','w') as f:
    f.write(cmatchl.as_csv())
modelcmatcvg = smf.ols(formula='Coverage ~ Depth', data=cmat).fit()
cmatcvg= modelcmatcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/cmatcvg.txt','w') as f:
    f.write(cmatcvg.as_csv())

# macroalgae
macroalgae=df2[46:69]
modelmacroalgaechl= smf.ols(formula='AvgChl ~ Depth', data=macroalgae).fit()
macroalgaechl= modelmacroalgaechl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/macroalgaeachl.txt','w') as f:
    f.write(macroalgaechl.as_csv())
modelmacroalgaecvg= smf.ols(formula='Coverage ~ Depth', data=macroalgae).fit()
macroalgaecvg= modelmacroalgaecvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/macroalgaeacvg.txt','w') as f:
    f.write(macroalgaecvg.as_csv())

#Sediment
sediment=df2[69:92]
modelsedimentchl= smf.ols(formula='AvgChl ~ Depth', data=sediment).fit()
sedimentchl= modelsedimentchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/sedimentchl.txt','w') as f:
    f.write(sedimentchl.as_csv())
modelsedimentcvg= smf.ols(formula='Coverage ~ Depth', data=sediment).fit()
sedimentcvg= modelsedimentcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/sedimentcvg.txt','w') as f:
    f.write(sedimentcvg.as_csv())

#Turf algae
turf=df2[92:115]
modelturfchl= smf.ols(formula='AvgChl ~ Depth', data=turf).fit()
turfchl=modelturfchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/turfchl.txt','w') as f:
    f.write(turfchl.as_csv())


modelturfcvg= smf.ols(formula='Coverage ~ Depth', data=turf).fit()
turfcvg=modelturfcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Depth/turfcvg.txt','w') as f:
    f.write(turfcvg.as_csv())


# INFRA
# Orbicella faveolata
Ofaveo = df1[0:23]
df1[0:23]

modelofaveochl = smf.ols(formula='AvgChl ~ InfrastructureN', data=Ofaveo).fit()
print(modelofaveochl)
modelofaveocvg = smf.ols(formula='Coverage ~ InfrastructureN', data=Ofaveo).fit()
ofaveochl = modelofaveochl.summary()

with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/ofaveochl.txt',
        'w') as f:
    f.write(ofaveochl.as_csv())

ofaveocvg = modelofaveocvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/ofaveocvg.txt',
        'w') as f:
    f.write(ofaveocvg.as_csv())

# Siderastrea siderea
Sidera = df1[23:46]
modelsiderachl = smf.ols(formula='AvgChl ~ InfrastructureN', data=Sidera).fit()
siderachl = modelsiderachl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/siderachl.txt',
        'w') as f:
    f.write(siderachl.as_csv())
modelsideracvg = smf.ols(formula='Coverage ~ InfrastructureN', data=Sidera).fit()
sideracvg = modelsideracvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/sideracvg.txt',
        'w') as f:
    f.write(sideracvg.as_csv())

# Diploria strigosa
Dstrigosa = df1[46:69]
modeldstrigosachl = smf.ols(formula='AvgChl ~ InfrastructureN', data=Dstrigosa).fit()
dstrigosachl = modeldstrigosachl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/dstrigosaachl.txt',
        'w') as f:
    f.write(dstrigosachl.as_csv())
modeldstrigosacvg = smf.ols(formula='Coverage ~ InfrastructureN', data=Dstrigosa).fit()
dstrigosacvg = modeldstrigosacvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/dstrigosaacvg.txt',
        'w') as f:
    f.write(dstrigosacvg.as_csv())

# Orbicella annularis
Oannularis = df1[69:92]
modeloannularischl = smf.ols(formula='AvgChl ~ InfrastructureN', data=Oannularis).fit()
oannularischl = modeloannularischl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/oannularischl.txt',
        'w') as f:
    f.write(oannularischl.as_csv())
modeloannulariscvg = smf.ols(formula='Coverage ~ InfrastructureN', data=Oannularis).fit()
oannulariscvg = modeloannulariscvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/oannulariscvg.txt',
        'w') as f:
    f.write(oannulariscvg.as_csv())

# Madracis auretenra
Madracis = df1[92:115]
modelmadracischl = smf.ols(formula='AvgChl ~ InfrastructureN', data=Madracis).fit()
madracischl = modelmadracischl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/madracischl.txt',
        'w') as f:
    f.write(madracischl.as_csv())

modelmadraciscvg = smf.ols(formula='Coverage ~ InfrastructureN', data=Madracis).fit()
madraciscvg = modelmadraciscvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/madraciscvg.txt',
        'w') as f:
    f.write(madraciscvg.as_csv())

# Corallinales
cca = df2[0:23]
modelccachl = smf.ols(formula='AvgChl ~ InfrastructureN', data=cca).fit()
modelccacvg = smf.ols(formula='Coverage ~ InfrastructureN', data=cca).fit()
ccachl = modelccachl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/ccachl.txt',
        'w') as f:
    f.write(ccachl.as_csv())

ccacvg = modelccacvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/ccacvg.txt',
        'w') as f:
    f.write(ccacvg.as_csv())

# Cyanobacterial mat
cmat = df2[23:46]
modelcmatchl = smf.ols(formula='AvgChl ~ InfrastructureN', data=cmat).fit()
cmatchl = modelcmatchl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/cmatchl.txt',
        'w') as f:
    f.write(cmatchl.as_csv())
modelcmatcvg = smf.ols(formula='Coverage ~ InfrastructureN', data=cmat).fit()
cmatcvg = modelcmatcvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/cmatcvg.txt',
        'w') as f:
    f.write(cmatcvg.as_csv())

# macroalgae
macroalgae = df2[46:69]
modelmacroalgaechl = smf.ols(formula='AvgChl ~ InfrastructureN', data=macroalgae).fit()
macroalgaechl = modelmacroalgaechl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/macroalgaeachl.txt',
        'w') as f:
    f.write(macroalgaechl.as_csv())
modelmacroalgaecvg = smf.ols(formula='Coverage ~ InfrastructureN', data=macroalgae).fit()
macroalgaecvg = modelmacroalgaecvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/macroalgaeacvg.txt',
        'w') as f:
    f.write(macroalgaecvg.as_csv())

# Sediment
sediment = df2[69:92]
modelsedimentchl = smf.ols(formula='AvgChl ~ InfrastructureN', data=sediment).fit()
sedimentchl = modelsedimentchl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/sedimentchl.txt',
        'w') as f:
    f.write(sedimentchl.as_csv())
modelsedimentcvg = smf.ols(formula='Coverage ~ InfrastructureN', data=sediment).fit()
sedimentcvg = modelsedimentcvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/sedimentcvg.txt',
        'w') as f:
    f.write(sedimentcvg.as_csv())

# Turf algae
turf = df2[92:115]
modelturfchl = smf.ols(formula='AvgChl ~ InfrastructureN', data=turf).fit()
turfchl = modelturfchl.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/turfchl.txt',
        'w') as f:
    f.write(turfchl.as_csv())

modelturfcvg = smf.ols(formula='Coverage ~ InfrastructureN', data=turf).fit()
turfcvg = modelturfcvg.summary()
with open(
        '/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/Terpisah/Infra/turfcvg.txt',
        'w') as f:
    f.write(turfcvg.as_csv())

