import csv
import re
import pandas as pd

#read SDSS.txt
with open("SDSS.csv",'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    with open('BOSS1441_SDSS','r',encoding = 'utf-8') as f:
        linelist = f.readlines()[10:]
        spamwriter.writerow(['_RAJ2000','_DEJ2000','RA_ICRS','DE_ICRS','mode','q_mode',\
                             'class','SDSS12','m_SDSS!2','ObsDate','Q','umag','e_umag',\
                             'gmag','e_gmag','rmag','e_rmag','imag','e_imag','zmag',\
                             'e_zmag','zsp','zph','e_zph','<zph>'])
        for line in linelist:
            line_list = line.strip('\n').split('\t')
            spamwriter.writerow(line_list)
# df1 = pd.read_csv('SDSS.csv')
# print(df1.info())
# print(df1.head(5))

#read BOSS.txt
with open("BOSS.csv",'w+',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    with open('BOSS1441_cut.cat','r',encoding = 'utf-8') as f:
        linelist = f.readlines()[9:]
        spamwriter.writerow(['NUMBER','X_IMAGE','Y_IMAGE','ALPHA_J2000','DELTA_J2000',\
                            'FLUX_APER','FLUXERR_APER','FLAGS','NITER_MODEL'])
        for line in linelist:
            line_list = line.strip('\n').split()
            spamwriter.writerow(line_list)
# df2 = pd.read_csv('BOSS.csv')
# print(df2.info())
# print(df2.head(5))
