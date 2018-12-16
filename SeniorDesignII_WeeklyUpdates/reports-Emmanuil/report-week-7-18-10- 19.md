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
* Re-evaluate current epochs and research how MNE epochs are created. The current format has 180ms of time for each event id. However, some event ids only describe a trial
and don't actually take up any time. I need to understand where that 180ms comes from.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
I will have a jupyter notebook that shows some tests and my conclusions on how epochs are created. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
Yes, I will refer to mne python as their documentation is comprehensive. 

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* After our meeting with Dave, it turns out the epochs we were working with were not in the correct format. They should be in 500ms
periods and begin at the first stim-code event id. 

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* For next meeting

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Create new epochs based on the research from MNE and information provided by Dave. 

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
* I will modify events that only include the start times of each epoch. So, events that describe a trial will not be in the epoch 
object anymore. Methods for preprocessing with frequency filtering and creating epochs will be written. This will all be contained in 
one method so all we need to input is the raw eeglab file.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
Yes, I have done most of this before so I just need to correct the mistake I made last time. Also need to clean up the code to make
it more accessible. 

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* We cannot get accurate results if we are working with 180ms epochs. 

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* For next meeting
## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
