
# coding: utf-8

# ## EEG RAW DATA EXPLORATION
# 
# By: Shateesh Bhugwansing 
# 
# data taken from: https://osf.io/j8n4b/ (Early and Late Components of EEG Delay Activity Correlate Differently with Scene Working Memory Performance)
# 
# Only downloaded suj11_wml2_day2 files, for EDA 
# 
# The MNE library is great because it can read a bunch of different file types, just find the corresponding read_<filetype>() fucntion from their documentation. In this example, I use read_raw_brainvision() to read the .vhdr file. 

# In[96]:


import mne
import matplotlib.pyplot as plt
import numpy as np
mne.set_log_level('INFO')

'''
***** NOTE *****
This path variable is only temporary (as of 04/10/18). We are working on setting up a cloud storage space and
a script to access that data virtually
'''
path = "/Users/shateeshbhugwansing/Desktop/seniorprojecteeg/suj11_wml2_day2.vhdr"
raw = mne.io.read_raw_brainvision(path, preload=True)

raw.info


# In[36]:


print(raw.ch_names)


# ## A segment of Raw Data 
# 
# Display all channels from 100 to 115 seconds

# In[37]:


start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
data, times = raw[:, start:stop]
print(data.shape)
print(times.shape)
data, times = raw[2:20:3, start:stop]  # access underlying data
raw.plot()


# ## Individual Channels 

# In[95]:


#choosing channels from the raw.ch_names list 
Fz = raw._data[1]
F2 = raw._data[-5]
print(Fz.shape)


# In[94]:


plt.hist(Fz)

