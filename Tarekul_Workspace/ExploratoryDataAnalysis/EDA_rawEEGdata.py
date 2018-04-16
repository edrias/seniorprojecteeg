
# coding: utf-8

# In[1]:


import numpy as np
import mne
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import scipy
from scipy.stats import hmean,trim_mean


# In[2]:


"""this example shows how to load one nap (day 2) from one subject (subject 1
3)
"""
filename="suj11_l5nap_day1.vhdr"
"""skipping the argument of `scaling`, therefore, the unit of the raw data wo
uld be voltage instead of micro-voltage. """
raw = mne.io.read_raw_brainvision(filename,# file name with 'vhdr'
preload=True)
"""Take a look at the raw data info"""
raw.info


# In[3]:


"""To visualize the data"""
"""As mentioned above, the unit of the raw data is in voltage, not micro-volt
age, thus, the scaling for eeg is 20E-6"""
scalingDict=dict(mag=1e-12, grad=4e-11, eeg=20e-6, eog=150e-6, ecg=5e-4,
                    emg=1e-3, ref_meg=1e-12, misc=1e-3, stim=1,
                    resp=1, chpi=1e-4)
raw.plot(start=0., # initial time to show
            duration = 10.0,# time window (sec) to plot in a given time
            n_channels=20, # number of channels to plot at once
            scalings = scalingDict, # scaling factor for traces
        )


# In[4]:


"""To visualize the power spectral density across data"""
raw.plot_psd(tmin=0.0, # initial time to show
                tmax=60.0, # end time to show
                fmin=0.0, # initial frequency to show
                fmax=200.0, # end frequency to show
                area_mode='std', # change to 'range'
            )

