# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 9/26/2018

## Stretch Goals (1-3)

1. classify modalities (audio vs visual) and get a score of 60 - 70% accuracy.  

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.



### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Automate the labeling of stim-code combinations for trials

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* There will be code/methods written and be put in our github.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
Yes, I fully understand how the stim-codes from range 1-24 relate to stim-code combinations. I just need to write out objects that 
define these combinations. 

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* Each trial has 9 events assoicated with them. So separating the events by trial will make it easier to write code to extract stim-code
combinations. 

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* by next meeting

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Classifying visual vs audio. After combining the three stim-codes (events 1-24) of a trial, it will allow for easy classification
of audio vs visual. This is the first stretch goal that we are trying to accomplish.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
* I will write code that outlines the classification pipeline. I will reduce dimensions using PCA and compute variance, skewness, 
and kurtosis for all time points of an event. Classification will be done with logistic regression and I will analyze results with 
confusion matricies

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* Most of the steps in this goal have already been done before, but I am just peicing them together into one pipeline. 

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* Yes this is relevant as it meets the stretch goal. 

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* next meeting

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
