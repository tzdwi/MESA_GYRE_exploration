import os
from glob import glob
import numpy as np

if __name__ == "__main__":
    
    profile_files = glob('../../23M_mesa/LOGS_to_rsg/profile*.data.GSM') # Now running on pre-RSG profiles
    profile_nums = list(map(int,[s.split('/')[-1].split('.')[0].lstrip('profile') for s in profile_files]))
    profile_min_max = np.percentile(profile_nums,[0,100])
    
    
    profiles = np.arange(*profile_min_max,15,dtype=int)
    
    for n in profiles:
        with open("prersg_gyre_template.txt", "r") as text_file:#open("postrsg_gyre_template.txt", "r") as text_file:
            gyre_file = text_file.readlines()
            for i,l in enumerate(gyre_file):
                gyre_file[i]=l.replace(r'PROF',str(n))
        with open("prersg_gyre.in","w") as text_file:#open("postrsg_gyre.in","w") as text_file:
            text_file.write(''.join(gyre_file))
            
        print(n)
            
        #os.system('$GYRE_DIR/bin/gyre postrsg_gyre.in')
        os.system('$GYRE_DIR/bin/gyre prersg_gyre.in')