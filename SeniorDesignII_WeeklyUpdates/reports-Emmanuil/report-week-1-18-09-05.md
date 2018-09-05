# Emmanuil Simkhayev

## Weekly Report 1 - 18-09-04

### What I did:

* Looking through the code Dave Britton gave us.
    * There were issues running his code, but the library that he used in his code worked fine. I was able to read the data, look at the channels, and get voltage readings for each channel. The library also allowed me to print triggers and the time they were recorded
        
### Smart Goals

#### Specific:
* I will use the libeep library provided to us by Dave to read the data and convert it to a format that can be read by MNE. Then I remove artifacts using ICA and filtering using MNE assisted methods and the sample code provided to us by Ning during our last semester. Ideally, we would like this data in epochs so it will be a goal but is not as crticial as preprocessing the data.

#### Measurable
* I will write code that will read the eeg data using the library provided as well as code to convert it to an MNE accepted format. There will also be code written for the artifact reduction. I will be in a folder that will contain all preprocessing for this data. 

#### Actionable
* The data is a little under 10GB, so it should not take long to iterate through the files and convert them. This will probably be the hardest part. Preprocessing will be easier with the help of MNE, so that should not take too long.

#### Relevant
* This is critial step before we can feed the data into classifiers to try out some small problems for the following week. Not being able to read the data through MNE will seriously hold us back from making any progress. 

#### Time bound
* I will aim to convert the mne data on Friday, do preprocessing on Saturday. If I have setbacks I will continue to get it done by Tuesday. 
