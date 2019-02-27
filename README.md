# Human Trafficking

Increasing numbers of young people are being trafficked online. Machine learning techniques can be used in order to prevent the same. Given a record of all previously identified human trafficking communications, a model can be built in order to identify frequently occurring patterns, such as **{Open for all, Travel expenses reimbursed} -> {Get an amazing experience}**. Normally genuine communications won't promise a reimbursement of travel expenses in case it is open for all.

Once such a model is created, whenever a new website initiates a new domain registration, it can be checked for the occurrence of such suspicious patterns and in case it does contain such patterns, an extensive investigation can be conducted before granting a domain. An app can also be built which can be installed by users in order to scan any mail received by them for the occurrence of such patterns and alert the user on the identification of such patterns.

## Economic Feasibility
The model, once built has to be installed only at the domain registration servers and can also be installed by users who wish to scan their mails in order to detect possible human trafficking communications. However, when a new website is identified as suspicious, an investigation has to be conducted which will incur a cost. Some portion of the cost might not have been necessary as a genuine website might have been identified as suspicious. However, the social benefit which the introduction of this technique will bring in will be much more than the cost incurred and hence, the proposed technique is worth implementing.

## Steps Required to Run the Code
In order to run the code, download all the files in the form of a zip folder, unzip the downloaded zip file, say Technothon-master.zip, and then execute the following commands:

1. cd Technothon-master

2. python3 generateSampleData.py: This command will generate a sample dataset containing the messages of various communications which were attempts of human trafficking. This step may be avoided since the sample dataset has already been generated and uploaded along with the program files.

3. python3 Data_Analysis.py: This command will generate a model from the sample dataset, in order to predict whether a future communication is an attempt of human trafficking or not.

4. python3 predictTraffic.py: This command will use the model generated in order to predict whether a communication is an attempt of human trafficking or not.
