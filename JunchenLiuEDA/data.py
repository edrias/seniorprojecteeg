
# coding: utf-8

# In[1]:


import mne


# In[2]:


mne.__version__


# In[3]:


raw = mne.io.read_raw_brainvision("suj11_l5nap_day1.vhdr", preload=True)


# In[4]:


raw.info


# In[5]:


raw.info["ch_names"][:10]


# In[6]:


mne.channels.get_builtin_montages()


# In[6]:


raw.set_eeg_reference("average", projection=False)


# In[12]:


events = mne.find_events(raw)


# In[14]:


import matplotlib.pyplot as plt
plt.plot(raw._data[2])
plt.show()


# In[15]:


raw.plot()


# In[17]:


plt.hist(raw._data[2])
plt.show()

