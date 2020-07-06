#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:34:41 2020

@author: mati
"""
import pandas as pd
import numpy as np
import sys
sys.path.append('/home/mati/Storage/Tesis/AnalisisGo-Tesis/')
import trueskill as ts
import TTT2 as th2
import TTT as thM
import time
from importlib import reload 
reload(th2)
reload(thM)
env2 = th2.TrueSkill(draw_probability=0)
envM = thM.TrueSkill(draw_probability=0)
df = pd.read_csv('/home/mati/Storage/Tesis/AnalisisGo-Tesis/DatosPurificados/summary_filtered_handicapPositive.csv')
df=df[:1]
env = ts.TrueSkill(draw_probability=0.0)
t1 = env.Rating()
t2 = env.Rating()
a, b = env.rate([[t1],[t2]],ranks=[0, 1])



#%%
start = time.time()
tw2 = env2.Team([env2.Rating()])
tb2 = env2.Team([env2.Rating()]) 
history2 = env2.Game([tw2,tb2], [0, 1])
end = time.time()
print('TTT', end-start)
start = time.time()
twM = envM.Team([envM.Rating()])
tbM = envM.Team([envM.Rating()]) 
historyM = envM.Game([twM,tbM], [0, 1])
end = time.time()
print('Mati', end-start)
#history.trueSkill()
#%%
print('Funciona', history.posterior)
print('Cambiado', historyM.posterior)
# %%

composition = [ [[1],[2,3]] ]
results = [[0,1]]
start = time.time()
i = 0
while i < 10000:
    history2 = env2.history(composition,[[1,1]] ,results)
    history2.through_time(online=False)
    i +=1
print('TTT', history2.times[0].posteriors)
end = time.time()
print('TTT', end-start)

 # %%
startM = time.time()
i = 0
while i < 10000:
    historyM = envM.history(composition,[[1,1]] ,results)
    historyM.through_time(online=False)
    i +=1
print('Mati',historyM.times[0].posteriors)
endM = time.time()
print('Mati', endM-startM)

# %% 
startM = time.time()
i = 0

while i < 1000:
    a = np.exp(321.32)
    i +=1
endM = time.time()
print('Mati', endM-startM)
# %%

twM = envM.Team([envM.Rating()])
tbM = envM.Team([envM.Rating(),env2.Rating(0,25/3)]) 
historyM = envM.history([[twM,tbM]],[[1,1]] ,[[0, 1]])
historyM.through_time(online=False)

#%%
0.09
0.006
a = [ 8.153915405273438e-05 ,7.62939453125e-05 ,7.557868957519531e-05 ,4.8160552978515625e-05
 ,3.790855407714844e-05 ,5.4836273193359375e-05 ,3.9577484130859375e-05 ,3.337860107421875e-05 ,5.817413330078125e-05
, 0.0001227855682373047, 4.553794860839844e-05
, 3.457069396972656e-05
, 3.409385681152344e-05
, 4.220008850097656e-05
, 3.314018249511719e-05
, 5.936622619628906e-05
, 3.314018249511719e-05
, 3.266334533691406e-05
, 3.0994415283203125e-05
, 2.8133392333984375e-05
, 3.0994415283203125e-05
, 2.7418136596679688e-05
, 2.9325485229492188e-05
, 2.7418136596679688e-05
, 2.9802322387695312e-05
, 2.765655517578125e-05
, 2.9087066650390625e-05
, 2.7179718017578125e-05
, 3.218650817871094e-05
, 2.9325485229492188e-05
, 6.985664367675781e-05
, 7.843971252441406e-05
, 6.127357482910156e-05
, 5.817413330078125e-05
, 2.8848648071289062e-05
, 2.4318695068359375e-05
, 2.5510787963867188e-05
, 2.3603439331054688e-05
, 2.5033950805664062e-05
, 2.288818359375e-05
, 2.7179718017578125e-05
, 2.4080276489257812e-05
, 3.4809112548828125e-05
, 2.5033950805664062e-05
, 4.553794860839844e-05
, 2.9325485229492188e-05
, 4.601478576660156e-05
, 2.765655517578125e-05
, 2.5272369384765625e-05
, 2.1457672119140625e-05
, 2.193450927734375e-05
, 2.0503997802734375e-05
, 3.647804260253906e-05
, 3.0040740966796875e-05
, 2.2172927856445312e-05
, 2.1457672119140625e-05
, 2.3126602172851562e-05
, 2.0742416381835938e-05
, 2.2411346435546875e-05
, 2.0503997802734375e-05
, 2.2411346435546875e-05
, 8.320808410644531e-05
, 2.3365020751953125e-05
, 2.09808349609375e-05
, 2.3126602172851562e-05
, 2.0742416381835938e-05
, 2.1696090698242188e-05
, 2.002716064453125e-05
, 2.09808349609375e-05
, 2.0265579223632812e-05
, 2.1696090698242188e-05
, 2.0742416381835938e-05
, 2.2172927856445312e-05
, 2.288818359375e-05
, 2.193450927734375e-05
, 2.09808349609375e-05
, 2.1696090698242188e-05
, 2.0265579223632812e-05
, 2.193450927734375e-05
, 2.0503997802734375e-05
, 2.1696090698242188e-05
, 0.00025653839111328125
, 2.2411346435546875e-05
, 2.0742416381835938e-05
, 2.1696090698242188e-05
, 2.6702880859375e-05
, 2.5033950805664062e-05
, 2.193450927734375e-05
, 2.384185791015625e-05
, 2.1696090698242188e-05
, 4.124641418457031e-05
, 2.2649765014648438e-05
, 2.3603439331054688e-05
, 2.0742416381835938e-05
, 2.5510787963867188e-05
, 4.601478576660156e-05
, 3.0279159545898438e-05
, 2.2649765014648438e-05
, 2.6464462280273438e-05
, 2.1696090698242188e-05
, 4.38690185546875e-05
, 2.5987625122070312e-05
, 3.910064697265625e-05
, 2.3126602172851562e-05
, 2.384185791015625e-05
, 2.3365020751953125e-05
, 2.4318695068359375e-05
, 2.1457672119140625e-05
, 2.2411346435546875e-05
, 2.0503997802734375e-05
, 2.3603439331054688e-05
, 2.1219253540039062e-05
, 2.2172927856445312e-05
, 2.1219253540039062e-05
, 2.2172927856445312e-05
, 2.0742416381835938e-05
, 2.193450927734375e-05
, 2.2649765014648438e-05
, 2.3365020751953125e-05
, 2.1219253540039062e-05
, 3.7670135498046875e-05
, 2.193450927734375e-05
, 2.193450927734375e-05
, 2.0265579223632812e-05
, 2.1696090698242188e-05
, 2.0742416381835938e-05
, 2.2172927856445312e-05
, 2.09808349609375e-05
, 2.2411346435546875e-05
, 3.4809112548828125e-05
, 2.4318695068359375e-05
, 2.1457672119140625e-05
, 0.00012731552124023438
, 3.886222839355469e-05
, 3.337860107421875e-05
, 4.8160552978515625e-05
, 2.574920654296875e-05
, 2.0742416381835938e-05
, 2.193450927734375e-05
, 2.0742416381835938e-05
, 2.1457672119140625e-05
, 3.6716461181640625e-05
, 2.1696090698242188e-05
, 2.0503997802734375e-05
, 2.1696090698242188e-05
, 2.09808349609375e-05
, 2.4080276489257812e-05
, 2.1219253540039062e-05
, 3.647804260253906e-05
, 2.193450927734375e-05
, 2.2649765014648438e-05
, 2.288818359375e-05
, 2.288818359375e-05
, 2.09808349609375e-05
, 2.5033950805664062e-05
, 2.3365020751953125e-05
, 2.2411346435546875e-05
, 2.2411346435546875e-05
, 2.1696090698242188e-05
, 2.1457672119140625e-05
, 2.384185791015625e-05
, 2.2411346435546875e-05
, 2.288818359375e-05
, 2.0742416381835938e-05
, 2.1696090698242188e-05
, 2.0742416381835938e-05
, 2.1696090698242188e-05
, 2.1219253540039062e-05
, 2.193450927734375e-05
, 2.1219253540039062e-05
, 2.2172927856445312e-05
, 2.09808349609375e-05
, 2.1219253540039062e-05
, 7.43865966796875e-05
, 2.384185791015625e-05
, 2.1457672119140625e-05
, 2.3365020751953125e-05
, 2.0742416381835938e-05
, 2.2172927856445312e-05
, 2.0503997802734375e-05
, 3.2901763916015625e-05
, 2.0742416381835938e-05
, 3.695487976074219e-05
, 2.4080276489257812e-05
, 4.1484832763671875e-05
, 3.814697265625e-05
, 3.314018249511719e-05
, 2.2172927856445312e-05
, 2.574920654296875e-05
, 2.4318695068359375e-05
, 2.47955322265625e-05
, 2.384185791015625e-05
, 2.2172927856445312e-05
, 2.288818359375e-05
, 2.2411346435546875e-05
, 2.09808349609375e-05
, 2.2649765014648438e-05
, 2.3365020751953125e-05
, 2.288818359375e-05
, 2.1457672119140625e-05]