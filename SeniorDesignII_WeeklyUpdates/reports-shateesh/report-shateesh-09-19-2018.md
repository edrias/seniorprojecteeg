# Smart and Stretch Goals

**Name:** Shateesh Bhugwansing
**Date:** 09/19/18

## Stretch Goals (1-3)

1. Perform binary classification on somewhat clean data. 


## S.M.A.R.T. Goals (next week)
### S.M.A.R.T. Goal 1.

#### S. Specific: 
Perform dimensionality reduction on one data file using PCA. I'll start with reducing the data down to 9 dimensions, as recommended by Prof. Grossberg. I will try doing this on a different number of dimensions and choose one that best represents all of the data. I will do this to simplify the feature space that is fed into the classification algorithm. 

#### M. Measurable: 
The output of the PCA procedure should produce a figure that shows the variance between each component. I will keep increasing the number of target components until there is a significant between the variance in the second to last and last component. This will verify the exact number of components needed to retain enough information from the original dataset. 

#### A. Achievable: 
This goal is achievable because a lot of the code will be based off of MNE and SciKit Learn documentation. 

#### R. Relevant :
This goal is relevant to the first level of classification we are trying to achieve, which is clasifying the modality of the stimulus (audio vs. visual). Dimension reduction is necessary for classification. 

#### T. Time-bound:
Next week : 09/26/2018


### S.M.A.R.T. Goal 2.

#### S. Specific: 
Use bandpass filtering to separate dimension-reduced EEG into the different types of brain waves (Alpha, Beta, Delta, Theta, Gamma). 

#### M. Measurable: 
I can measure this goal by applying bandpass filters to the EEG data and then plotting the resulting frequencies to make sure it is in the specified range. I can plot the averages of each type of brain wave and should see distinct clusters based on the brain wave type. 

#### A. Achievable: 
To my knowledge, I can use MNE documentation to learn how to filter for different types of brain waves. I will need to learn how to visualize the differences. 

#### R. Relevant :
This goal is necessary for reducing the sample size even further for the classification algorithm. If I can separate the data by type of brain wave, I can run the classifier on each type and see which ones produce significant results. 

#### T. Time-bound: 
I aim to get this goal done by next week, 09/26/18. 


### S.M.A.R.T. Goal 3.

#### S. Specific: 
Use K-Nearest Neighbors to classify dimension-reduced data. 

#### M. Measurable: 
This goal can be measured by the classification score of the algorithm. 

#### A. Achievable: 
I can refer to our code from last semester to learn how to use this classifier. 

#### R. Relevant :
This goal is the first step in getting useful results for the classification problem of modality of stimuli. 


#### T. Time-bound: 
I aim to get this goal done by next week: 09/26/2018. 



## S.M.A.R.T. Goals (last week)
1. Improve our project proposal by incorporating Dave's feedback
    * We didn't get any feedback yet. This goal is not completed. 
2. Convert raw data to .set files, which can be read by MNE
    * https://ccnymailcuny-my.sharepoint.com/:f:/g/personal/sbhugwa000_citymail_cuny_edu/EiO1Xr_YTNpGuexyxi0gf90BjttBhk8n0KaOfV5Vj7D7eQ?e=wr826M
3. Research Data visualization techniques
    * We decided to stick with MNE and built-in python tools. For now, there is no need for anything more. 