import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
df1=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data1.csv')
df3=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data3.csv')
df4=pd.read_csv('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Data4.csv')

#CORAL (DF3)
#*
#Orbicella faveolata
Ofaveo= df3[0:23]

df3[0:23]

modelofaveochl = smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=Ofaveo).fit()
print(modelofaveochl)
modelofaveocvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=Ofaveo).fit()
ofaveochl= modelofaveochl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ofaveochl.txt','w') as f:
    f.write(ofaveochl.as_csv())

ofaveocvg= modelofaveocvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ofaveocvg.txt','w') as f:
    f.write(ofaveocvg.as_csv())


#Siderastrea siderea
Sidera= df3[23:46]
modelsiderachl = smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=Sidera).fit()
siderachl= modelsiderachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/siderachl.txt','w') as f:
    f.write(siderachl.as_csv())
modelsideracvg = smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=Sidera).fit()
sideracvg= modelsideracvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sideracvg.txt','w') as f:
    f.write(sideracvg.as_csv())

# Diploria strigosa
Dstrigosa=df3[46:69]
modeldstrigosachl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=Dstrigosa).fit()
dstrigosachl= modeldstrigosachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/dstrigosaachl.txt','w') as f:
    f.write(dstrigosachl.as_csv())
modeldstrigosacvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=Dstrigosa).fit()
dstrigosacvg= modeldstrigosacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/dstrigosaacvg.txt','w') as f:
    f.write(dstrigosacvg.as_csv())

#Orbicella annularis
Oannularis=df3[69:92]
modeloannularischl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=Oannularis).fit()
oannularischl= modeloannularischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/oannularischl.txt','w') as f:
    f.write(oannularischl.as_csv())
modeloannulariscvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=Oannularis).fit()
oannulariscvg= modeloannulariscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/oannulariscvg.txt','w') as f:
    f.write(oannulariscvg.as_csv())

#Madracis auretenra
Madracis=df3[92:115]
modelmadracischl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=Madracis).fit()
madracischl=modelmadracischl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/madracischl.txt','w') as f:
    f.write(madracischl.as_csv())


modelmadraciscvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=Madracis).fit()
madraciscvg=modelmadraciscvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/madraciscvg.txt','w') as f:
    f.write(madraciscvg.as_csv())



###++++

#Orbicella faveolata
Ofaveo= df3[0:23]
modelofaveochl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=Ofaveo).fit()
modelofaveocvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=Ofaveo).fit()
ofaveochl2= modelofaveochl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ofaveochl2.txt','w') as f:
    f.write(ofaveochl2.as_csv())

ofaveocvg2= modelofaveocvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ofaveocvg2.txt','w') as f:
    f.write(ofaveocvg2.as_csv())


#Siderastrea siderea
Sidera= df3[23:46]
modelsiderachl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=Sidera).fit()
siderachl2= modelsiderachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/siderachl2.txt','w') as f:
    f.write(siderachl2.as_csv())
modelsideracvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=Sidera).fit()
sideracvg2= modelsideracvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sideracvg2.txt','w') as f:
    f.write(sideracvg2.as_csv())

# Diploria strigosa
Dstrigosa=df3[46:69]
modeldstrigosachl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=Dstrigosa).fit()
dstrigosachl2= modeldstrigosachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/dstrigosaachl2.txt','w') as f:
    f.write(dstrigosachl2.as_csv())
modeldstrigosacvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=Dstrigosa).fit()
dstrigosacvg2= modeldstrigosacvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/dstrigosaacvg2.txt','w') as f:
    f.write(dstrigosacvg2.as_csv())

#Orbicella annularis
Oannularis=df3[69:92]
modeloannularischl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=Oannularis).fit()
oannularischl2= modeloannularischl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/oannularischl2.txt','w') as f:
    f.write(oannularischl2.as_csv())
modeloannulariscvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=Oannularis).fit()
oannulariscvg2= modeloannulariscvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/oannulariscvg2.txt','w') as f:
    f.write(oannulariscvg2.as_csv())

#Madracis auretenra
Madracis=df3[92:115]
modelmadracischl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=Madracis).fit()
madracischl2=modelmadracischl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/madracischl2.txt','w') as f:
    f.write(madracischl2.as_csv())


modelmadraciscvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=Madracis).fit()
madraciscvg2=modelmadraciscvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/madraciscvg2.txt','w') as f:
    f.write(madraciscvg2.as_csv())


#MACROALGAE CCA (DF4)

#*
#Corallinales
cca= df4[0:23]
modelccachl = smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=cca).fit()
modelccacvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=cca).fit()
ccachl= modelccachl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ccachl.txt','w') as f:
    f.write(ccachl.as_csv())

ccacvg= modelccacvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ccacvg.txt','w') as f:
    f.write(ccacvg.as_csv())


#Cyanobacterial mat
cmat= df4[23:46]
modelcmatchl = smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=cmat).fit()
cmatchl= modelcmatchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/cmatchl.txt','w') as f:
    f.write(cmatchl.as_csv())
modelcmatcvg = smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=cmat).fit()
cmatcvg= modelcmatcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/cmatcvg.txt','w') as f:
    f.write(cmatcvg.as_csv())

# macroalgae
macroalgae=df4[46:69]
modelmacroalgaechl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=macroalgae).fit()
macroalgaechl= modelmacroalgaechl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/macroalgaeachl.txt','w') as f:
    f.write(macroalgaechl.as_csv())
modelmacroalgaecvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=macroalgae).fit()
macroalgaecvg= modelmacroalgaecvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/macroalgaeacvg.txt','w') as f:
    f.write(macroalgaecvg.as_csv())

#Sediment
sediment=df4[69:92]
modelsedimentchl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=sediment).fit()
sedimentchl= modelsedimentchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sedimentchl.txt','w') as f:
    f.write(sedimentchl.as_csv())
modelsedimentcvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=sediment).fit()
sedimentcvg= modelsedimentcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sedimentcvg.txt','w') as f:
    f.write(sedimentcvg.as_csv())

#Turf algae
turf=df4[92:115]
modelturfchl= smf.ols(formula='AvgChl ~ Depth * C(Infrastructure)', data=turf).fit()
turfchl=modelturfchl.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/turfchl.txt','w') as f:
    f.write(turfchl.as_csv())


modelturfcvg= smf.ols(formula='Coverage ~ Depth * C(Infrastructure)', data=turf).fit()
turfcvg=modelturfcvg.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/turfcvg.txt','w') as f:
    f.write(turfcvg.as_csv())



###++++

#Corallinales
cca= df4[0:23]
modelccachl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=cca).fit()
modelccacvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=cca).fit()
ccachl2= modelccachl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ccachl2.txt','w') as f:
    f.write(ccachl2.as_csv())

ccacvg2= modelccacvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/ccacvg2.txt','w') as f:
    f.write(ccacvg2.as_csv())


#Cyanobacterial mat
cmat= df4[23:46]
modelcmatchl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=cmat).fit()
cmatchl2= modelcmatchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/cmatchl2.txt','w') as f:
    f.write(cmatchl2.as_csv())
modelcmatcvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=cmat).fit()
cmatcvg2= modelcmatcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/cmatcvg2.txt','w') as f:
    f.write(cmatcvg2.as_csv())

# macroalgae
macroalgae=df4[46:69]
modelmacroalgaechl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=macroalgae).fit()
macroalgaechl2= modelmacroalgaechl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/macroalgaeachl2.txt','w') as f:
    f.write(macroalgaechl2.as_csv())
modelmacroalgaecvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=macroalgae).fit()
macroalgaecvg2= modelmacroalgaecvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/macroalgaeacvg2.txt','w') as f:
    f.write(macroalgaecvg2.as_csv())

#Sediment
sediment=df4[69:92]
modelsedimentchl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=sediment).fit()
sedimentchl2= modelsedimentchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sedimentchl2.txt','w') as f:
    f.write(sedimentchl2.as_csv())
modelsedimentcvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=sediment).fit()
sedimentcvg2= modelsedimentcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/sedimentcvg2.txt','w') as f:
    f.write(sedimentcvg2.as_csv())

#Turf algae
turf=df4[92:115]
modelturfchl2= smf.ols(formula='AvgChl ~ Depth + C(Infrastructure)', data=turf).fit()
turfchl2=modelturfchl2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/turfchl2.txt','w') as f:
    f.write(turfchl2.as_csv())


modelturfcvg2= smf.ols(formula='Coverage ~ Depth + C(Infrastructure)', data=turf).fit()
turfcvg2=modelturfcvg2.summary()
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/turfcvg2.txt','w') as f:
    f.write(turfcvg2.as_csv())



#TRIAL
#df1
df1
Ofaveosidera= df1[0:46]
Ofaveosidera
#CHL
#interaction
modelofsichl = smf.ols(formula='AvgChl ~ Depth * InfrastructureN', data=Ofaveosidera).fit()
modelofsichl = modelofsichl.summary()
modelofsichl
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/modelofsichl.txt',
          'w') as f:
    f.write(modelofsichl.as_csv())

#no interaction
modelofsichl2 = smf.ols(formula='AvgChl ~ Depth + InfrastructureN', data=Ofaveosidera).fit()
modelofsichl2 = modelofsichl2.summary()
modelofsichl2
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/modelofsichl2.txt',
          'w') as f:
    f.write(modelofsichl2.as_csv())

#COVERAGE
#interaction
modelofsicvg = smf.ols(formula='Coverage ~ Depth * InfrastructureN', data=Ofaveosidera).fit()
modelofsicvg = modelofsicvg.summary()
modelofsicvg
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/modelofsicvg.txt',
          'w') as f:
    f.write(modelofsicvg.as_csv())

#no interaction
modelofsicvg2 = smf.ols(formula='Coverage ~ Depth + InfrastructureN', data=Ofaveosidera).fit()
modelofsicvg2 = modelofsicvg2.summary()
modelofsicvg2
with open('/home/michelia.wibowo/labspaces/curacao-reef-mapping/data/work/Michelia/Results/Regression/modelofsicvg2.txt',
          'w') as f:
    f.write(modelofsicvg2.as_csv())