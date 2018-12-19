# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 11/28/18

## Stretch Goals (1-3)

1. Analyze the coefficients from the time-dimension. 

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Apply the visualization technique that I've used last week for the audio vs. visual question, but take the average across all channels, for each time point. 

#### M. Measurable: 
This goal is really measurable by making a similar plot as the averaged coefficients for each channel, but instead this time, I want to see which samples (along the time axis) are most important. 

#### A. Achievable: 
Yes, since the pipeline is already in place for what I want to do. I need to alter the dimension that I'm averaging over-- instead of taking the average for all time samples for each channel, I want to take the average of all channels for each time sample. 

#### R. Relevant :
This goal is relevant for trying to identify the most important pieces of the signal that are relevant to our classification question. 


#### T. Time-bound: 
Next week, 12/05/18. 


### S.M.A.R.T. Goal 3.

#### S. Specific: 
Repeat smart goal #1 but with a different data set, and for the language vs. non-language problem. 

#### M. Measurable: 
This goal is measurable. The same metrics from goal #1 will be used here. 

#### A. Achievable: 
Yes. 

#### R. Relevant :
This goal is relevant for trying to identify the most important pieces of the signal that are relevant to our classification question. 

#### T. Time-bound: 
Next week, 11/28/18  

### S.M.A.R.T. Goal 2.

#### S. Specific: 
Use the "Linear Classification on sensor data with plot patterns" example from MNE to visalize patterns in the coefficients.

#### M. Measurable: 
This goal will be measured by the sensor plot that MNE includes in this example.

#### A. Achievable: 
Executing the code is achievable, but I need to read the documentation and the design paradigm of MNE to understand exactly what a 'pattern' is in this context. Scikitlearn's logistic regression model has an attribute 'coef_' that I've been using. I've never used the MNE version, with the attribute 'patterns_'.

#### R. Relevant :
This goal is relevant to deciding on what method to use to visualize our results to Dave. 

#### T. Time-bound: 
Next week, 12/05/18 
  

## S.M.A.R.T. Goals (last week)
The method I used to visualize the highest average coefficients according to their electrode position works, and seems to be roughly accurate in terms of the location in the brain where language processing occurs. Dave hasn't confirmed it with us though, but he will be there at next week's meeting so he can give us feedback then. 
