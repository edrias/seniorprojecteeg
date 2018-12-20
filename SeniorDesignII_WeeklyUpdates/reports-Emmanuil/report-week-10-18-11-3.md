# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 11/3/2018

## Stretch Goals (1-3)

1. Classifiy Audio vs Visual and understand where signals in the brain are.

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Isolate frequency bands of Gamma, Alpha, Theta, and Beta of the EEG data

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* I will have a figure that will display the global field power over time. This is a method magnifying the activity in the brian
at a certain point in time. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* MNE Python has a section with helpful documentation on isolating frequency bands 

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* Studying frequency bands will help us find where signals originate.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
[INSERT]

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
[INSERT]

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
[INSERT]

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
This is relevant because when we worked with Dr. Elmores data, the MNE objects had events assocated with them aand it made classifying
and converting to pandas extremely simple. 


#### T. Time-bound: 
(What’s the deadline and is it realistic?)
[INSERT]

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* Last weeks smart goal was to be able to extract events that describe a trial and create new event_ids that will allow us to classifying 
stimulus concepts, congruency, ect. 
    * I was not able to successfully complete this within the time I set for myself, but I did begin working on it by writing a method to 
      separate trials into lists. This can be later used to compare events of trials that include stim-code combinations. 
    * [Repo location](https://github.com/edrias/seniorprojecteeg/blob/master/Classification/ConcatEpochTrails.ipynb) method is get_trial_index_list 
