# SF Bulk TA #
Automate adding multiple TA instances to SalesForce database.

## Background ##
Every time I have communication with the various healthcare facilities that I work with, I have to document the technical assistance in SalesForce.  Not a big deal for "one off" encounters, but when I do a mass email or mailing, I have to put the exact same information into the system for every single facility.  That can get agonizingly tedious and error prone.

It really makes me not want to do that kind of thing, which I really can't do.  The system does have a "bulk activities" form, but "bulk" is used loosely.  You can only enter up to 10 facilities at a time, and you still have to go through and check all eleven of the Yes and No combo boxes for every individual location.  Doesn't really save any time.

I decided to give Python using Selenium a try, and to tell you the truth, I think my first stab at it worked pretty good.

## Impressions ##
I documented with comments in the file throughout the course of the learning process.  You can view some of the comments over the course of time by viewing History.  Overall, this was a pretty easy project and I learned a lot doing it.  I'm glad I did it and I think it's given me the confidence to try some more complex projects.

## Files ##
sfbulkta.py - The script that runs the whole thing.
hha_data.csv - The csv data file that contains a list of all the facilities, points of contact, and the URL for each TA page.  This file has been added to .gitignore to prevent the real data from being shared in public.
campaign.json - This file has "campaign specific" data that can be changed with every run of the script.
.gitignore - The usual stuff.
README.md - this file.

## TODO ##
Make the code cleaner, neater, and more efficient
Add some logic to detect errors while running the script
Add some logic to allow for the individual rows in the csv to be selected or deselected for inclusion in the loop
Add function to update the Venue for each campaign

