# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 9/21/2018

## Stretch Goals (1-3)

1. classify modalities (audio vs visual) and get a score of 60 - 70% accuracy.  

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.

Write batch scripts for
Removing artifacts (frequency filtering + ICA)
Creating epoched data with labels
Isolate labels based on modalities
Identify missing event ids 


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Incorporate ICA into the preprocessing I have done with frequency filtering. I am doing this because it became apparant from our Google Hangouts discussion that
I was missing a key step in the artifact removal process. 

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
There will be code in within the seniorprojecteeg/preprocessing folder that shows this. I will use exerpts from Nings code as well as 
MNE-Python documentation ICA. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
Yes, I have already done ICA but did not get good results because I had not applied notch and frequency filters before hand.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* This goal is relevant with the stretch goal of performing basic classification and the even more long term goal of answering questions in our proposal.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* I'm setting a deadline is by the 22th.  

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Label data with events using .trg files. Without labeled data we cannot perform classification. 

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
I will write batch scripts for creating epoched and event labaled data for all files, then distribute to group members via OneDrive. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
Yes, I have already started this process on one file for testing purposes, so writing a batch script will be simple, but time consuming to run.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
To get immediate results, we can just use one fully preprocessed file, but eventually we will need to classify all subjects together.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
Would like to get this done by September 23rd

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* goal for labeling events: https://github.com/edrias/seniorprojecteeg/blob/master/preprocessing/Events.ipynb
* goal for artifact removing : https://github.com/edrias/seniorprojecteeg/blob/master/preprocessing/Artifact_Removal/Filtering_Resampling.ipynb
