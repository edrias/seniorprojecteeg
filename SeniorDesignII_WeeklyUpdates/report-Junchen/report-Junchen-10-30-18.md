# Smart and Stretch Goals

**Name:** Junchen Liu
**Date:** 10/31/18

## Stretch Goals (1-3)

1. Be able to turn our data into a two class problem data since our data right now contains a lots of labels.
2. Explore the coefficients used in LDA, understanding why we got low classficaiton scores.

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Use Scrw, Kurtosis, Variance to convert the data from 500 points to 3 points and do classfication.

#### M. Measurable: 
This goal is measurable by manually checking the shape of our data. which from (987,129,500) -> (987,129,3)

#### A. Achievable: 
Yes this is achievable because our epoch data can support various array operations which allow us to do statistic in our data.

#### R. Relevant :
This goal is relevant because we have to see which part of the data fluctuate the most.

#### T. Time-bound: 
I aim to get this done by 11/07/2018. 

### S.M.A.R.T. Goal 2.

#### S. Specific: 
I will run pca 28 components in our data and then do Screw, Kurtosis, Variance to do EEG analysis on our data.

#### M. Measurable: 
Like goal #1, this is measurable by manually checking the shape of our data, which from (987,129,500) -> (987,28,3)

#### A. Achievable: 
Yes. This is achievable because we can loop through our data by looking at each epoch and channel and and then do EEG data analysis on single data point and appends those back to the array.

#### R. Relevant :
This goal is relevant because we want to be able to find the useful signals of our data, and the reduce of dimension of our data will help us to narrorw down our search.

#### T. Time-bound: 
Next week, 11/07/18

### S.M.A.R.T. Goal 3.

#### S. Specific: 
I will use LDA to do classfication on both the date (987,129,3) on Goal#1 and (987,28,3) on Goal#2 and compare the result. I will also map the coefficient of LDA intend to find out how the coefficient leads to the classfication scores.

#### M. Measurable: 
I will measure this goal by comparing classfication scores of last Week to this week and see if dimension redection will give higher classfication scores or not.

#### A. Achievable: 
Yes, This is achievable because I have Skilearn library that provides us with different classfication algorithmn.

#### R. Relevant :
This goal will help because it allows us to see what is causing the classfication socres to be low.

#### T. Time-bound: 
Next week, 11/07/18


## S.M.A.R.T. Goals (last week)
1. Relabeling 6 epoch as 1 trials and set them as either language 4 , and nonlanguage 5.
2. Use KNN to classfify our labeled data lanaguage vs. Nonlanguage
3. The classfication scores were around 50,60%.
