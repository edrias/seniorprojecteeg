# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 11/07/18

## Stretch Goals (1-3)

1. Integrate the montage file for Dave's EEG cap into MNE so we can use MNE for visualizing our classification results. 

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Edit the montage file in order to successfully load it into a Jupyter Notebook using MNE. 

#### M. Measurable: 
This goal is measurable by manually testing out the read_montage() and plot_montage() methods in MNE. 

#### A. Achievable: 
I hope so. I tried this once before on my laptop, but there was a weird issue with the file type that my mac was converting the montage file into. I'll try this on a different OS and see what happens.  

#### R. Relevant :
This goal is relevant to presenting our machine learning results.   


#### T. Time-bound: 
I aim to get this done before next week. Say, 11/10/2018? 

### S.M.A.R.T. Goal 2.

#### S. Specific: 
I will use Logistic Regression on one subject's data file to generate coefficients. 

#### M. Measurable: 
This goal is measurable by comparing the locations of the coefficients to the expected regions of activity. For example, in the audio vs. visual case, we expect the higher coefficients to appear in the back or the sides of the head, which correlate to the visual cortex and the ears. 


#### A. Achievable: 
Yes, hopefully. I need to figure out a way to map the coefficients to actual electrode positions. 

#### R. Relevant :
Extremely relevant for visualizing the results of our classification experiments. 

#### T. Time-bound: 
Next week, 11/14/18

### S.M.A.R.T. Goal 3.

#### S. Specific: 
Repeat smart goal #2 with a different data set, and compare results. 

#### M. Measurable: 
This goal is measurable. I think short term, I will measure this goal by visually comparing the two results. However I need to develop a more concrete way to do the comparison. 

#### A. Achievable: 
Yes. Once the pipeline is developed from Goal #2, I can re-use it for this goal. 

#### R. Relevant :
This goal is relevant to ensuring that our pipelines work for the entire data set.  

#### T. Time-bound: 
Next week, 11/14/18  
  

## S.M.A.R.T. Goals (last week)
I couldn't get the montage file to load into MNE. Manually plotting the montage using the raw x,y and z coordinates did not go well. We got a shape that somewhat resembled the original montage, but it was not accurate enough to be useful to anyone, really.  
The 2D interpolation example seemed to work, but when plotted against an improper montage shape, we couldn't know for sure. 
