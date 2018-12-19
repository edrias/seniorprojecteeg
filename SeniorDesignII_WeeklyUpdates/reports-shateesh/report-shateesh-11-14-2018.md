# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 11/14/18

## Stretch Goals (1-3)

1. Make sense of the logistic regression coefficients 

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Build and execute the pipeline for the Logistic regression experiments for audio vs. visual + visualize the coefficients.  


#### M. Measurable: 
This goal is measurable by using the buit in 'scores' method in scikit learn to get the scores for the logistic regression model.  
In terms of measuring the coefficients, I plan on ranking them from highest to lowest in absolute value, then taking the higest ranking coefficients and  
manually highlight which electrode positions correlate to them. 

#### A. Achievable: 
Yes. We've been building binary classification experiements with MNE + scikit learn for a few weeks now. 

#### R. Relevant :
This goal is relevant to making progress in the hierarchy of classification problems we aim to solve with this project. 


#### T. Time-bound: 
Next week, 11/21/18. 

### S.M.A.R.T. Goal 2.

#### S. Specific: 
Compare my custom method of identifying the highest ranking coefficients (electrode positions) with an MNE built-in method of finding patterns in a Logistic regression model over time.

#### M. Measurable: 
This goal is measurable by using an eye test. I'll have to visually compare my results to the plots that Emmanuil provided last week. 


#### A. Achievable: 
Yes. I started to design this pipeline last week, and based on the shape of the coefficient object that I got, I know it'll work. 

#### R. Relevant :
This goal is relevant for us because it'll help us decide on what type of visualization method we should use going forward. 

#### T. Time-bound: 
Next week, 11/21/18

### S.M.A.R.T. Goal 3.

#### S. Specific: 
Repeat smart goal #2 with a different data set, and compare results. 

#### M. Measurable: 
This goal is measurable. The same metrics from goal #2 will be used here. 

#### A. Achievable: 
Yes. 

#### R. Relevant :
This goal is relevant to ensuring that our pipelines work for the entire data set.  

#### T. Time-bound: 
Next week, 11/21/18  
  

## S.M.A.R.T. Goals (last week)
