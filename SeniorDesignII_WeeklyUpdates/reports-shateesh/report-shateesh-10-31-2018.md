# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 10/31/18

## Stretch Goals (1-3)

1. Figure out a custom way to visualize our data using MNE, because ANT data-type is not supported. 
2. Explore the coefficients used in Logistic Regression, try to map those to electrode positions/channels. 

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Plot the montage of the cap that was used in the experiment to gather our data set. 

#### M. Measurable: 
This goal is measurable by manually reviewing the accuracy of the montage compared to the photo of the electrode positions from the cap's manufacturer.

#### A. Achievable: 
Yes I think so. The methods from MNE are pretty straight forward. 

#### R. Relevant :
This goal is relevant to presenting our machine learning results.   


#### T. Time-bound: 
I aim to get this done by 11/07/2018. 

### S.M.A.R.T. Goal 2.

#### S. Specific: 
I will plot the electrode postiions in a normal matplotlib scatter plot as a reference, in case the MNE montage method doesn't work. 

#### M. Measurable: 
Like goal #1, this is measurable by manually reviewing the accuracy of the montage compared to the photo of the elctrode positions from the cap's manufacturer. 

#### A. Achievable: 
Yes. Using matplotlib is easy. 

#### R. Relevant :
This goal will serve as a sanity check to make sure that the way I'm using the montage points are fine. 

#### T. Time-bound: 
Next week, 11/07/18

### S.M.A.R.T. Goal 3.

#### S. Specific: 
I will use the 2D interpolation example from scipy documentation to generate our own version of a heatmap of the logistic regression coefficients over time. 

#### M. Measurable: 
I will measure this goal by observing the interpolation plots from different time stamps throughout an epoch, and confirming with Dave if that makes sense. 
For example, if at 30ms, the visual cortex appears to light up, does that make sense in an audio vs. visual case? 

#### A. Achievable: 
Yes, prof. Grossberg showed me the documentation for the 2D interpolation. 

#### R. Relevant :
This goal will help to visualize the brain's activity over time. 

#### T. Time-bound: 
Next week, 11/07/18


## S.M.A.R.T. Goals (last week)
1. Work with MNE developers to find a way to visualize the electrode positons: I got it to work, didn't need their help anymore, so I closed the issue on github. 
2. Map the classification coefficients to the channels: I  made a python dictionary doing so, couldn't get it to the actual plot. 
3. Didn't get to generalize the lexicality problem. 
