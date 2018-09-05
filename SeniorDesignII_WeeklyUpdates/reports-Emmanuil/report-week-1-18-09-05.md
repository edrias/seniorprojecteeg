# Emmanuil Simkhayev

## Weekly Report 1 - 18-09-04

### What I did:

* Looking through the code Dave Britton gave us.
    * There were many issues on my end running his code. 
        * First off, I discovered it could only be ran on linux machine because of a .so file in a library called libeep that is used to read EEG data in ANT .cnt format.
        * I spent time running his code on my machine, however there were bugs. I experimented with the libeep library alone to debug. I was successful in reading the .cnt files with library but did not do any EDA as the library is limited. I found a github repo that created another library that used libeep with MNE-Python. I thought it could be extremely beneficial to the group if I could figure out how to use it. But unfortunatly, the .so file in libeep is compiled using python2.7, and MNE-Python has upgraded to python3.6 on their site. I have not been able to Find MNE for Python2. 