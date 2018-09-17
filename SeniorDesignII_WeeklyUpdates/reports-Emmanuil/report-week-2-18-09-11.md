# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 9/11/2018

## Stretch Goals (1-3)

1. classify modalities (audio vs visual) 

2. 1

3. 

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* To remove artifacts from the converted .cnt data using MNE-Python. This needs to be a team effort because we are all held back from making progress until
we can clean the data into something acceptable for machine learning. This is a goal because it is a critical step in starting to do basic classification and getting some results.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* Ideally there will be graphs that show before and after graphs of a sample of EEG. Where the after images have lines that are not haphazard.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* I have Nings code from his github as a starting point. If that does not work, MNE-Python has great documentation and many techniques for artifact removal.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* This goal is relevant with the stretch goal of performing basic classification and the even more long term goal of answering questions in our proposal.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Deadline is by the 18th. If I can't get this done by this date, then we are in trouble. 

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Label data with events using .trg files. Without labeled data we cannot perform classification. 

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
* I will use the .trg files provided by Dave for each .cnt file. I will convert the .trg file into a .txt and parse the file so that 
each event/trigger is in a list. Using MNE-Python I will match up the timestamps in the EEG data with the timestamps in the trigger file. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* I don't exactly know how to interpret the .trg files. If I can't figure it out, I will ask Dave and do research at the same time because
I know he is away and might not answer within a reasonable amount of time.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
This is relevant because when we worked with Dr. Elmores data, the MNE objects had events assocated with them aand it made classifying
and converting to pandas extremely simple. 


#### T. Time-bound: 
(What’s the deadline and is it realistic?)
Would like to get this done by Wednesday the 19th.

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* Last weeks smart goal was to get the .cnt data into a format that can be read by MNE-Python. 
  1. I have code that shows the progress with reading the data with libeep. It led to many issues as a result of my lack of RAM in my computer.
  2. I abandonded this method when I heard Junchen had successfully converted .cnt to an EEGLAB format that can be read by MNE-Python.
  3. github location: {https://github.com/edrias/seniorprojecteeg-master-fork/blob/master/MNE_Conversion_Scripts/ANTCntToMNEArray.ipynb}
* I also planned to remove artifacts, but converting to .cnt took too up too much of my time.  
