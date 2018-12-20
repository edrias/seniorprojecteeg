# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 11/7/2018

## Stretch Goals (1-3)

Classify Audio vs Visual and look for signals in brain spatially and over time.

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Using montage files, plot the power of each frequency band and identify the band with most activity.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* There will be a figure with electrode positions for each frequency band. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* Now that we have montage files, MNE python has a method to plot the frequency bands on head map.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* This will provide insight as to which band has the best signal and can help with classifying.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Use the results of the previous goal to isolate the channels that are the most active and use them to classify.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
* A head map with those useful channels will be displayed in the slides for the status update. These locations will be 
used for classification of audio vs visual. There will be code in a jupyter notebook that shows this process.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* It is just a matter of analyzing the signals from the head map image of the frequency bands then extracting specific channels.
Classification is simple as we have already set up the pipeline for that.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* We are trying to identify which parts of the brain are most useful in classification for the Audio vs Visual problem. 

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week.

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* Isoalte frequency bands of Gamma, Alphaa, Theta, and Beta of EGG data.
  * The results of this are shown in this [presentation](https://docs.google.com/presentation/d/16ngSx52-4-3yTKU-x5Jg9A13IuQBDjmZQ6Ei1veXqY4/edit?usp=sharing) within slide 9 
