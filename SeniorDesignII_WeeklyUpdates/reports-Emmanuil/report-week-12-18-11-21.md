# Smart and Stretch Goals

**Name:** Emmanuil Simkhayev
**Date:** 11/21/18

## Stretch Goals (1-3)

* Take on the lexical vs non-lexical classification problem

## S.M.A.R.T. Goals (next week)

You should be able to tie this to the strech goals. If you can't perhaps you don't understand the big picture.
Use concise language, but include relevant information. Be positive when answering the questions. You must have
3-5 of these and you will be measured on how you do.


### S.M.A.R.T. Goal 1.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
* I noticed that when plotting data over time in ms, it turned out to be 1949ms per epoch instead of the expected 500ms.
This means that during epoch creation, the time dimension was not in milliseconds. This smart goal is to correct that. 

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
* Do some math to convert 512 samples per second into 500ms. The notebook that I used to generate epochs needs to be
modified.

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* Yes I do, the error occured with a misunderstanding with MNE documentation.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* All of the results from classification up to this point is basically useless because epochs were longer than 500ms.  

#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* next week.

### S.M.A.R.T. Goal 2.

#### S. Specific: 
(What do you want to accomplish? Who needs to be included? When do you want to do this? Why is this a goal?)
Re-do the classification of Audio vs Visual with corrected epochs.

#### M. Measurable: 
(How can you measure progress and know if you’ve successfully met your goal?)
Fill in (this should be crisp like implment a specific function, produce a notebook with certain graphs, etc. If it is not something
obvious to me how I would grade success, partial sucess and failure, then you lose points.)
Following the pipeline layed out in the slides. There will also be a method written out that will make utilizing this pipeline
simple. 

#### A. Achievable: 
(Do you have the skills required to achieve the goal? If not, can you obtain them? What is the motivation for this goal? Is the amount of effort required on par with what the goal will achieve?)
* Since it is a "redo" of old work to see how results differ with corrected epochs, there is not anything new to do here.

#### R. Relevant :
(Why am I setting this goal now? Is it aligned with overall objectives like stretch goals?)
* To make right the in correct results is a necessary step in completing our goal.


#### T. Time-bound: 
(What’s the deadline and is it realistic?)
* Next week

## S.M.A.R.T. Goals (last week)
List the smart goals you completed last week. First list the goal, and then list the locations of the commits or urls of the artificats promised in the smart goal that stand as evidence that what was goal was completed. If there is no such artificat (even if none was promised. This is a zero.)
* Goal 1: Straight forward classification of lexical vs non-lexical
  * [Repo Location](https://github.com/edrias/seniorprojecteeg/blob/master/Classification/WordVsNonWord.ipynb)
* Goal 2: break up problem int audio lexicality - and visual lexicaclity: same as above link.
