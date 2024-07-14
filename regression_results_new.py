import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
df1=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data1.csv')
df2=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data2.csv')
df1

df3=pd.concat([df1,df2])
df3
modelall = smf.ols(formula='Coverage ~ C(Species) + Depth * InfrastructureN', data=df3).fit()
print(modelall)
modelall.summary()

modelofaveocvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Ofaveo).fit()
ofaveochl= modelofaveochl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ofaveochl.txt','w') as f:
    f.write(ofaveochl.as_csv())


#CORAL (df1)
#*
#Orbicella faveolata
Ofaveo= df1[0:23]

df1[0:23]

modelofaveochl = smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Ofaveo).fit()
print(modelofaveochl)
modelofaveocvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Ofaveo).fit()
ofaveochl= modelofaveochl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ofaveochl.txt','w') as f:
    f.write(ofaveochl.as_csv())

ofaveocvg= modelofaveocvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ofaveocvg.txt','w') as f:
    f.write(ofaveocvg.as_csv())


#Siderastrea siderea
Sidera= df1[23:46]
modelsiderachl = smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Sidera).fit()
siderachl= modelsiderachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/siderachl.txt','w') as f:
    f.write(siderachl.as_csv())
modelsideracvg = smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Sidera).fit()
sideracvg= modelsideracvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sideracvg.txt','w') as f:
    f.write(sideracvg.as_csv())

# Diploria strigosa
Dstrigosa=df1[46:69]
modeldstrigosachl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Dstrigosa).fit()
dstrigosachl= modeldstrigosachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/dstrigosaachl.txt','w') as f:
    f.write(dstrigosachl.as_csv())
modeldstrigosacvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Dstrigosa).fit()
dstrigosacvg= modeldstrigosacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/dstrigosaacvg.txt','w') as f:
    f.write(dstrigosacvg.as_csv())

#Orbicella annularis
Oannularis=df1[69:92]
modeloannularischl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Oannularis).fit()
oannularischl= modeloannularischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/oannularischl.txt','w') as f:
    f.write(oannularischl.as_csv())
modeloannulariscvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Oannularis).fit()
oannulariscvg= modeloannulariscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/oannulariscvg.txt','w') as f:
    f.write(oannulariscvg.as_csv())

#Madracis auretenra
Madracis=df1[92:115]
modelmadracischl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Madracis).fit()
madracischl=modelmadracischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/madracischl.txt','w') as f:
    f.write(madracischl.as_csv())


modelmadraciscvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Madracis).fit()
madraciscvg=modelmadraciscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/madraciscvg.txt','w') as f:
    f.write(madraciscvg.as_csv())



###++++

#Orbicella faveolata
Ofaveo= df1[0:23]
modelofaveochl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Ofaveo).fit()
modelofaveocvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Ofaveo).fit()
ofaveochl2= modelofaveochl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ofaveochl2.txt','w') as f:
    f.write(ofaveochl2.as_csv())

ofaveocvg2= modelofaveocvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ofaveocvg2.txt','w') as f:
    f.write(ofaveocvg2.as_csv())


#Siderastrea siderea
Sidera= df1[23:46]
modelsiderachl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Sidera).fit()
siderachl2= modelsiderachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/siderachl2.txt','w') as f:
    f.write(siderachl2.as_csv())
modelsideracvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Sidera).fit()
sideracvg2= modelsideracvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sideracvg2.txt','w') as f:
    f.write(sideracvg2.as_csv())

# Diploria strigosa
Dstrigosa=df1[46:69]
modeldstrigosachl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Dstrigosa).fit()
dstrigosachl2= modeldstrigosachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/dstrigosaachl2.txt','w') as f:
    f.write(dstrigosachl2.as_csv())
modeldstrigosacvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Dstrigosa).fit()
dstrigosacvg2= modeldstrigosacvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/dstrigosaacvg2.txt','w') as f:
    f.write(dstrigosacvg2.as_csv())

#Orbicella annularis
Oannularis=df1[69:92]
modeloannularischl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Oannularis).fit()
oannularischl2= modeloannularischl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/oannularischl2.txt','w') as f:
    f.write(oannularischl2.as_csv())
modeloannulariscvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Oannularis).fit()
oannulariscvg2= modeloannulariscvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/oannulariscvg2.txt','w') as f:
    f.write(oannulariscvg2.as_csv())

#Madracis auretenra
Madracis=df1[92:115]
modelmadracischl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Madracis).fit()
madracischl2=modelmadracischl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/madracischl2.txt','w') as f:
    f.write(madracischl2.as_csv())


modelmadraciscvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Madracis).fit()
madraciscvg2=modelmadraciscvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/madraciscvg2.txt','w') as f:
    f.write(madraciscvg2.as_csv())


#MACROALGAE CCA (df2)

#*
#Corallinales
cca= df2[0:23]
modelccachl = smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=cca).fit()
modelccacvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=cca).fit()
ccachl= modelccachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ccachl.txt','w') as f:
    f.write(ccachl.as_csv())

ccacvg= modelccacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ccacvg.txt','w') as f:
    f.write(ccacvg.as_csv())


#Cyanobacterial mat
cmat= df2[23:46]
modelcmatchl = smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=cmat).fit()
cmatchl= modelcmatchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/cmatchl.txt','w') as f:
    f.write(cmatchl.as_csv())
modelcmatcvg = smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=cmat).fit()
cmatcvg= modelcmatcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/cmatcvg.txt','w') as f:
    f.write(cmatcvg.as_csv())

# macroalgae
macroalgae=df2[46:69]
modelmacroalgaechl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=macroalgae).fit()
macroalgaechl= modelmacroalgaechl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/macroalgaeachl.txt','w') as f:
    f.write(macroalgaechl.as_csv())
modelmacroalgaecvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=macroalgae).fit()
macroalgaecvg= modelmacroalgaecvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/macroalgaeacvg.txt','w') as f:
    f.write(macroalgaecvg.as_csv())

#Sediment
sediment=df2[69:92]
modelsedimentchl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=sediment).fit()
sedimentchl= modelsedimentchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sedimentchl.txt','w') as f:
    f.write(sedimentchl.as_csv())
modelsedimentcvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=sediment).fit()
sedimentcvg= modelsedimentcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sedimentcvg.txt','w') as f:
    f.write(sedimentcvg.as_csv())

#Turf algae
turf=df2[92:115]
modelturfchl= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=turf).fit()
turfchl=modelturfchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/turfchl.txt','w') as f:
    f.write(turfchl.as_csv())


modelturfcvg= smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=turf).fit()
turfcvg=modelturfcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/turfcvg.txt','w') as f:
    f.write(turfcvg.as_csv())



###++++

#Corallinales
cca= df2[0:23]
modelccachl2= smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=cca).fit()
modelccacvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=cca).fit()
ccachl2= modelccachl2.summary()
modelccachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ccachl2.txt','w') as f:
    f.write(ccachl2.as_csv())

ccacvg2= modelccacvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/ccacvg2.txt','w') as f:
    f.write(ccacvg2.as_csv())


#Cyanobacterial mat
cmat= df2[23:46]
modelcmatchl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=cmat).fit()
cmatchl2= modelcmatchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/cmatchl2.txt','w') as f:
    f.write(cmatchl2.as_csv())
modelcmatcvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=cmat).fit()
cmatcvg2= modelcmatcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/cmatcvg2.txt','w') as f:
    f.write(cmatcvg2.as_csv())

# macroalgae
macroalgae=df2[46:69]
modelmacroalgaechl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=macroalgae).fit()
macroalgaechl2= modelmacroalgaechl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/macroalgaeachl2.txt','w') as f:
    f.write(macroalgaechl2.as_csv())
modelmacroalgaecvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=macroalgae).fit()
macroalgaecvg2= modelmacroalgaecvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/macroalgaeacvg2.txt','w') as f:
    f.write(macroalgaecvg2.as_csv())

#Sediment
sediment=df2[69:92]
modelsedimentchl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=sediment).fit()
sedimentchl2= modelsedimentchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sedimentchl2.txt','w') as f:
    f.write(sedimentchl2.as_csv())
modelsedimentcvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=sediment).fit()
sedimentcvg2= modelsedimentcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/sedimentcvg2.txt','w') as f:
    f.write(sedimentcvg2.as_csv())

#Turf algae
turf=df2[92:115]
modelturfchl2= smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=turf).fit()
turfchl2=modelturfchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/turfchl2.txt','w') as f:
    f.write(turfchl2.as_csv())


modelturfcvg2= smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=turf).fit()
turfcvg2=modelturfcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/InfrastructureN/turfcvg2.txt','w') as f:
    f.write(turfcvg2.as_csv())