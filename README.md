# getawestats

Due to issues with the AWE stats page online, I had to come up with a creative solution.

We are having to go right now to each machine and manually grab the CSV files.
This is a python script to parse through them all at once and spit out a report with stats based on sessions only.

If you know how to work with python, just drop all the AWE .csv files into a folder called "files" and run the script.
The only non-built-in module I'm using is alive_progress, so you will have to pip install that one if you want to use it.

The Python script spits out a file called stats.txt which is a simple report with stat sections for each csv file that looks like the following:

---------------files\ERLSP1.csv---------------
 
Total Sessions for 1/2022:   107
Total Time For Month 1/2022: 7:35:31
Average Session Time: 0:04:15
 
Total Sessions for 2/2022:   113
Total Time For Month 2/2022: 7:49:0
Average Session Time: 0:04:09
 
Total Sessions for 3/2022:   101
Total Time For Month 3/2022: 4:7:43
Average Session Time: 0:02:27
 
Total Sessions for 4/2022:   113
Total Time For Month 4/2022: 11:49:50
Average Session Time: 0:06:16
 
Total Sessions for 5/2022:   10
Total Time For Month 5/2022: 7:17:5
Average Session Time: 0:43:42
