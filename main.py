'''
Created on Jun 11, 2015

@author: Oli
'''
'''
Created on Jun 11, 2015

@author: Oli
'''
import sys
import os
import numpy as np
import csv
import pandas as pd
# import str





sys.path.append('/Users/Oli/work/python/minions')
sys.path.append('/Users/Oli/work/Timber/Timber_python_MFitterer/rdmstores/')
sys.path.append('/Users/Oli/work/Timber/Timber_python_MFitterer/')



from log_file_setup import log_files
# from analysis_modules import data
from log_file_setup import Tee
import matplotlib.pyplot as plt
from gen_class import gen
from data_import import imp
from plotter_class import plotter
from ana_data import ana_data
from ana_res import ana_res
from plotter import *

from rdmstores import * 

a = ana_data()
ar = ana_res()
g = gen()
l = log_files()
i = imp() 
p = plotter()
hp = histplot()

# d = data()
# c = csv_list()


cwd = '/Users/Oli/work/python/rosy'

data_fold = 'data'
plot_fold = 'plots' 
ana_res_fold = 'ana_res' 

data_path  = '/Users/Oli/work/dBLM_readout/IP4/ROSYAX106E20028/test_env'
# data_path = os.path.join(cwd,data_fold)
plot_path = os.path.join(cwd,plot_fold)
ana_res_path = os.path.join(cwd,ana_res_fold) 


l.log_file_set(cwd,'log')
  
f = open(l.log_path(),'a')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)


pflag=1

ana_file_save_interval = 5


g.printer(data_path,pflag)

i.path(data_path,pflag)
i.path_check(pflag)
i.data_list_creator('_TL.csv',pflag)
p.set_save_path(plot_path,pflag)
ar.infrastruc(ana_res_path,pflag)

header=[['time_stamp','year','month','day','hour','minute','second','time sec','time zero','delta time zero','beam','ip','loc','dcum','type','daq_name','mode','beamstatus',
         't_count','t_count_inc','t_count_start','restart','counts','dcounts','dtime','run','analysed',
         'file_name','file_name_path']]
rosy_conf = [['daq_name'        ,'ip'   ,'beam' ,'loc'  ,'dcum'     ,'type'],
             ['ROSYAX106E20028' ,'4'    ,'1'    ,'1'    ,'9929.46'  ,'BCM1F' ],
             ['ROSYAX106E20021' ,'4'    ,'1'    ,'2'    ,'9936.93'  ,'BCM1F' ],
             ['ROSYAX106E20028A' ,'4'    ,'2'    ,'2'    ,'10057.23'  ,'CIVIDEC' ],
             ['ROSYAX106E20028A' ,'4'    ,'2'    ,'1'    ,'10064.71'  ,'CIVIDEC' ],
             ['ROSYAX106E20028A' ,'7'    ,'1'    ,'1'    ,'19799.784'  ,'CIVIDEC' ],
             ['ROSYAX106E20028A' ,'7'    ,'2'    ,'1'    ,'20188.54'  ,'CIVIDEC' ]
             ]


ar.header_set(header,pflag)
ar.ana_file_check(1,pflag)
ar.ana_file_loader(pflag)
ar.ana_file_writer(i.data_list,pflag)
ar.ana_file_saver(1,pflag)

# sys.exit('stop')
max_it = len(ar.ana_file)
# print ar.ana_file[0]

a.header(ar.ana_file[0],pflag)


# sys.exit('stop')
for k in range(1,max_it):
# for k in range(len(i.data_list)):
    g.loop_info(k,i.len_data_list,pflag)
    print ar.ana_file[k]
    line = ar.ana_file[k]
    ana_flag = a.tba_check(line,1,pflag)
    if ana_flag == 1:
        g.tprinter('start analysis',pflag)
        a.name_info_hist(line,rosy_conf,pflag)
        a.time_cor(line,pflag)
         
# #         break
        a.data_loader(line,pflag)
        
        a.data_check(pflag)
        a.bin_time_cor(pflag)
        a.c_counter(line,pflag)
        a.set_t_zero(line,pflag)
        a.time_sec(line,pflag)
        a.delta_time_zero(line,pflag)
        a.dc_counter(line,pflag)
        a.dt_counter(line,pflag)
        
#         name ='test.pdf'
#         hp.shist(a.data,1,plot_path,a.time_stamp+'_'+a.daq_name,pflag)

#         a.t_delta(line,a.data,pflag)
#         a.offset_corr(line,a.data,pflag)
#         a.noise_finder(line,a.data,pflag)
#         a.max_finder(line,a.data,pflag)
    else:
        pass
    
    
    a.analysed(ar.ana_file[k],pflag)
 
ar.ana_file_saver(1,pflag)   
    
# for i in ar.ana_file:
#     print i    
#     i.data_importer(i.data_list[k][0],pflag)
#     p.set_save_path(plot_path,pflag)
# #     for q in range(10):
# #         print i.data[q,3:]
#     p.simple_plotter(i.data[:,3:],i.data_list[k][1],0,pflag)
#     max_y_index=a.max_find(i.data[:,3:],1,pflag)
#     p.zoom_plotter(i.data[:,3:],i.data_list[k][1],max_y_index,1000,0,pflag)
#     print a.trig_finder(i.data[:,3:],1,2,pflag)








