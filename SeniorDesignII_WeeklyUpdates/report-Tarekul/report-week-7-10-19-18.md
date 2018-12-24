# Smart and Stretch Goals

**Name:** Tarekul Islam
**Date:** 10/19/18

## Stretch Goals

1.9 event trials made no sense as the events overlapped each other.
The understanding is that their really isnt 9 seperate events but some events happen within other events. The main events are related to the subject seeing stimulus, and clicking correct response. Data needs to be reorganized, because we only need the flanker,target, and flanker events. 

2. Each epoch is not supposed to be 180 ms but 500 ms according to Dave, the data needs to reformatted.

## S.M.A.R.T. Goals (next week)


### S.M.A.R.T. Goal 1.

#### S. Specific: 
Resample data to 500 ms. Filter data for only stim code combination events.

#### M. Measurable: 
Goal can be measured if data is correctly formatted. When we print the shape of the epoch data it should be epoch x channels x 500 ms.

#### A. Achievable: 
This goal will take some researching on how the epoch samples are created and what is the sampling rate.  

#### R. Relevant :
This is relevant because the data needs to be formatted correctly otherwise data is useless.


#### T. Time-bound: 
Next Week

### S.M.A.R.T. Goal 2.

#### S. Specific: 
Combine epochs flanker,target,flanker, and match the combinations to audio or visual. Classify using PCA to compare results.

#### M. Measurable: 
We can measure by plotting the data and see if we only have stim events and we can plot to see if we have only audio or visual combinations in data. We can plot confusion matrix for the classification score. We can use many different classifiers to compare results.

#### A. Achievable: 
Yes we have classified before but with wrongly formatted data. I have used PCA before too. 


#### T. Time-bound: 
Next Week


## S.M.A.R.T. Goals (last week)
Group events, validate stim codes
Filtered Stim ids and classified visual versus audio
Confusion matrix

seniorprojecteeg/Tarekul_Workspace/capstone2/CombineNineEpoch.ipynb
seniorprojecteeg/Tarekul_Workspace/capstone2/visual_audio.ipynb