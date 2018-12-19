# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 11/21/18

## Stretch Goals (1-3)

1. Make sense of the logistic regression coefficients, for the Language vs. Non-Language problem

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Apply the same custom pipeline that I've built for the audio vs. visual classification problem and apply it to the Language vs. Non-Language case. 

#### M. Measurable: 
This goal is measurable by the same metrics from last week-- using the buit in 'scores' method in scikit learn to get the scores for the logistic regression model.  
In terms of measuring the coefficients, I plan on ranking them from highest to lowest in absolute value, then taking the higest ranking coefficients and  
manually highlight which electrode positions correlate to them. 

#### A. Achievable: 
Yes, since the pipeline is already in place for what I want to do. I just have to work on a new method of labeling the data for language vs. non-langauge, which shouldn't be too hard.  

#### R. Relevant :
This goal is relevant to making progress in the hierarchy of classification problems we aim to solve with this project. 


#### T. Time-bound: 
Next week, 11/28/18. 


### S.M.A.R.T. Goal 2.

#### S. Specific: 
Repeat smart goal #1 with a different data set, and compare results. 

#### M. Measurable: 
This goal is measurable. The same metrics from goal #2 will be used here. 

#### A. Achievable: 
Yes. 

#### R. Relevant :
This goal is relevant to ensuring that our pipelines work for the entire data set.  

#### T. Time-bound: 
Next week, 11/28/18  

### S.M.A.R.T. Goal 3.

#### S. Specific: 
Compare my results from goals #1 and #2 with neuroscience research about language processing.

#### M. Measurable: 
This goal will be measured by the eye test. I'll have to do research about where language processing happens in the brain, and see if it matches up with the regions that have the highest coefficients in the logistic regresison experiments.

#### A. Achievable: 
I think so. This goal will come down to how easy it is for me to understand the neuroscience research that I find on this topic. 

#### R. Relevant :
This goal is relevant to ensuring that our pipeline is accurate with what the rest of the neuroscience realm already understands about the brain and language processing. 

#### T. Time-bound: 
Next week, 11/28/18 
  

## S.M.A.R.T. Goals (last week)
The method I used to visualize the highest average coefficients according to their electrode position works. I chose to use the top 20 coefficients because of the PCA analysis that Tarekul did, which showed that the most variance is contained in 20 components. I need to get this work verified by Dave, though -- I'm not sure if it's useful to him in this form. 
