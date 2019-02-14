
<img width="220" alt="portfolio_view" align="right" src="https://github.com/FCrSTATS/SportsCodeR/blob/master/img/SportsCodePy.png">

# SportsCodeR

Sporstcode is one of the leading video analysis software in the performance analysis field today, used by thousands of analysts, coaches and athletes around the world. The platform allows analysts and coaches to visually identify what went well and what could be improved in a training session or game by providing a quick and easy way to create interactive reports linked to key highlights. The process is very simple: capture your video into Sportscode, code the different events that take place in the footage, evaluate the results of the relevant events captured and present the insights to coaches and athletes. 

A powerful feature of Sportscode is the ability to import an XML file that creates timelines of clips from the related data. This is a largely under-utilised feature that has huge potential. The SportsCodePy functions aim to increase it's usage by making it easy from turning a pandas dataframe of metrics into a SportsCode ready XML file. 
SportsCodeR.png
This is a beta version, with more functions to be added at a later date. Feedback will be gratefully received to improve the package. 

## Not a Package

I aim to build a package for the functions to be much easier to access. In the meantime you will have to use the functions as individual files. 

## Functions 

### players_as_rows()
**Convert a dataframe into a SportsCode XML file:** Creates an XML file that will put players on rows and put one metric as a value. 

##### Parameters 

dat - A pandas dataframe of information to use

period1_start - Second value of the period 1 start within the SportsCode game footage, numeric value

period2_start - Second value of the period 2 start within the SportsCode game footage, numeric value 

player - The name of the column containing the player name values, string value

team - The name of the column containing the team name values, string value

time - The name of the column with the time of the event occuring, numeric value

lead_time - Number of seconds of video needed prior to the event, numeric value

lag_time - Number of seconds of video needed after to the event, numeric value

metric_val - The name of the column with the value of the metric being displayed, numeric or string value

period_id - The name of the column with the period information (period 1 must be 1, period 2 must be 2, period 3 must be 3, period 4 must be 4], numeric value

ID - The name of the column containing the ID values, string value

metric_label - Name of the metric i.e. "xGChain"

export_filename - Name of file name to save to, must end in ".xml"

period3_start - Second value of the period 3 start within the SportsCode game footage (default =0, edit only if needed), numeric value

period4_start - Second value of the period 4 start within the SportsCode game footage (default =0, edit only if needed), numeric value 

### teams_as_rows()
**Convert a dataframe into a SportsCode XML file:** Creates an XML file that will put teams on rows and put one metric as a value. 

##### Parameters 

dat - A pandas dataframe of information to use

period1_start - Second value of the period 1 start within the SportsCode game footage, numeric value

period2_start - Second value of the period 2 start within the SportsCode game footage, numeric value 

team - The name of the column containing the team name values, string value

start - The name of the column with the time of the beginning of the clip, numeric value

end - The name of the column with the time of the end of the clip, numeric value

metric_val - The name of the column with the value of the metric being displayed, numeric or string value

period_id - The name of the column with the period information (period 1 must be 1, period 2 must be 2, period 3 must be 3, period 4 must be 4], numeric value

ID - The name of the column containing the ID values, string value

metric_label - Name of the metric i.e. "xGChain"

export_filename - Name of file name to save to, must end in ".xml"

period3_start - Second value of the period 3 start within the SportsCode game footage (default =0, edit only if needed), numeric value

period4_start - Second value of the period 4 start within the SportsCode game footage (default =0, edit only if needed), numeric value 
              
## SportsCode Usage 

1. Import XML file 
<img src="https://github.com/FCrSTATS/SportsCodeR/blob/master/img/import.png">

2. Successfully Added to Timeline
<img src="https://github.com/FCrSTATS/SportsCodeR/blob/master/img/imported.png">

3. Clipped With Labels
<img src="https://github.com/FCrSTATS/SportsCodeR/blob/master/img/clipped.png">
