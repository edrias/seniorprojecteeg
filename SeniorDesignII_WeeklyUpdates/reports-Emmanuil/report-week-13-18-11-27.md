# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 11/27/2018

## Stretch Goals (1-3)

* Looking for signals in the brain in the time and spatial domain during classification.

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Find a way to plot results of coefficients from logsitic regression onto the brain map. This will be over time and show
the channels of the brain with these coefficients.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* There will be a notebook with the work and the slides will show the figures of the results.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* I will research mne python documentation on how to plot these results. There is a section under *Classification* that has an example
with plotting coefficients onto the brain using logistic regression.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* To be most helpful to Dave, we need to find where and when in the brain these signals originate.

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* Generate an ROC plot to show classification results over time. Plot the coefficients as evoked and confirm results of first
 smart goal.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
* A notebook will contain the code. The slides will contain figures of these head maps, and ROC graphs.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* MNE also has an example with that I will try to make work with our data.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* Same reason as the first goal, to find a signal over time and spatially.


#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* Smart goal one: fix epoched data.
    * [Repo location](https://github.com/edrias/seniorprojecteeg/blob/master/preprocessing/Artifact_Removal/Batch_ArtifactFilter_Epoch.ipynb) The method *create_epochs* has a line that computes the time in samples required for 500 ms.
    * This [presentation](https://docs.google.com/presentation/d/17n2SON4eSC3M0cXW-B2UyPOT4nCbaaDAqjdbrGkwUuQ/edit?usp=sharing) has the figures and results starting from slides 3 - 7
