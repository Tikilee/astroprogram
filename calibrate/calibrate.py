import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


df_BOSS = pd.read_csv('D:/study/pythoncode/practice/venv/BOSS.csv')
df_SDSS = pd.read_csv('D:/study/pythoncode/practice/venv/SDSS.csv')

#data screening
df_SDSS = df_SDSS.loc[df_SDSS['class'] == 6]
df_SDSS = df_SDSS.loc[df_SDSS.gmag < 24].reset_index()
df_BOSS = df_BOSS.loc[df_BOSS.FLUX_APER > 0].reset_index()


print(df_BOSS.info())
print(df_SDSS.info())

SDSS_match = []
BOSS_match = []


for i in range(len(df_SDSS._RAJ2000)):
    for j in range(len(df_BOSS.NUMBER)):
        if (df_BOSS.ALPHA_J2000[j] - df_SDSS._RAJ2000[i])**2 + \
                (df_BOSS.DELTA_J2000[j] - df_SDSS._DEJ2000[i])**2 <= 0.0000001:
            SDSS_match.append(i)
            BOSS_match.append(j)


print(SDSS_match)
print(len(SDSS_match))
print(len(set(SDSS_match)))
print(BOSS_match)
print(len(BOSS_match))

SDSS_mag = [(df_SDSS.umag[i]) - 0.8116 * (df_SDSS.umag[i] - df_SDSS.gmag[i]) \
            + 0.1313 for i in SDSS_match]
#SDSS_mag = [(df_SDSS.gmag[i]) + 0.3130 * (df_SDSS.gmag[i] - df_SDSS.rmag[i]) \
#          + 0.2271 for i in SDSS_match]
BOSS_mag = [-2.5 * math.log(df_BOSS.FLUX_APER[i], 10) for i in BOSS_match]
substract = [SDSS_mag[i] - BOSS_mag[i] for i in range(len(SDSS_mag))]


plt.figure()
plt.scatter(SDSS_mag, substract,s = np.pi * 1.75**2, c = '#00CED1', alpha=0.2)
# plt.plot(np.arange(len(SDSS_mag)), BOSS_mag,'.',label = 'BOSS')
# plt.plot(np.arange(len(SDSS_mag)), SDSS_mag,'.', label = 'SDSS')
plt.xlabel('SDSS_mag')
plt.ylabel('$\Delta$m(SDSS-BOSS)')
plt.legend()
plt.show()
#plt.plot(np.linspace(1,len(SDSS_mag), SDSS_mag))

