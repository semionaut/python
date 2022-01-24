# Election Analysis

## Project Overview
Tom represents the Colorado Board of Elections. He reached out and [requested](https://courses.bootcampspot.com/courses/1023/pages/3-dot-0-4-welcome-to-pypoll?module_item_id=390331) we conduct an analysis auditing recent tabulated election results for the vote in select congressional precincts in the state.

The Board usually conducts such analysis using Excel, but has requested we automate this process using Python.

Their instructions were to calculate the following:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

## Resources
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.63.2

## Outputs
* PyPoll.py (initial script)
* PyPoll_Challenge.py (challenge script)
* election_analysis.txt (results)
* terminal_output.jpg (screenshot)

## Summary of Election Outcomes
This analysis revealed the following outcomes:
- There were a total of **369,711** ballots cast in this election.
- The counties represented in this sample were:
  - Jefferson
  - Denver
  - Arapahoe
- The voting results by county were:
  - Jefferson returned 38,855 votes; 23.0% of ballots.
  - Denver returned 306,055 votes; 82.8% of ballots.
  - Arapahoe returned 24,801 votes; 6.7% of ballots.
- The county that returned the most votes was **Denver**, with **306,055** [82.8%] of the total votes in this sample.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 85,213 votes; 23.0% of the vote.
  - Diana DeGette received 272,892 votes; 73.8% of the vote.
  - Raymon Anthony Doane received 11,606 votes; 3.1% of the vote.
- The winner of the election was:
  - The winning candidate was **Diana DeGette**, with **272,892** [73.8%] of the total votes.

## Challenge Overview
The challenge sought to expand on the project specification outlined above by including a geographic dimension in the analysis, adding the following deliverables:
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

The Colorado Independent [Congressional](https://redistricting.colorado.gov/content/congressional-redistricting) and Legislative Redistricting Commissions were established via state amendments in 2018, and carried out a process of [redrawing Colorado's congressional district boundaries that concluded in 2021](https://projects.fivethirtyeight.com/redistricting-2022-maps/colorado/). The appointment of an independent Commission is consquential since Democrats currently control all levels of government in the state and would have been able to draw the maps to their advantage had voters not approved the formation of an independent redistricting commission.

![Colorado Congressional Districts map](https://github.com/semionaut/python/blob/main/Election-Analysis/Resources/Colorado_Congressional_Districts.JPG)

The code we provided to Tom and the Board should be able to analyze any data set following their standard format and return a breakdown of: total votes cast, number of votes and percentage of total votes by county, county with the largest number of votes, number of votes and percentage of total votes by candidate, and determine which candidate won the election, along with their vote count and percentage of total votes.

## Future Directions
As future work, we might consider:
* Looking at voter turnout as a percentage of registered voters for those precincts that were analyzed. As Colorado's largest urban center, one might expect Denver to return the highest number of ballots, but for the sake of accuracy that metrics ought to be expressed as a proportion to eligible voters. In addition, Denver and Arapahoe constitute single-precinct districts (Colorado's 1st and 6th Congressional district respectively) whereas Jefferson is just one of nine precincts that make up the 7th Congressional district, therefore it might be expected that its smaller aggregate turnout is normal relative to the overall size and population of that region.
* Operations to reorder the county and/or candidate lists in descending order by total votes or vote percentage, rather than the order these entries first appeared in the extract.
* We also didn't consider candidate selection by district to see where the balance of voters for a particular candidate was distributed. It is often the case that US voters choose a candidate along urban/rural lines and it might be interesting to compare the % of votes by county for each candidate and look for differences between Denver and Arapahoe/Jefferson as well as any major trends.
* Lastly, as these pre-tabulated election results contain a mix of hand-counted, machine-counted, and DRE computer-counted ballots, it would be worthwhile to check and verify for unique ballot IDs in the results, in the event of any miscounting or double-counting of the vote. For this analysis, we assume there is no irregularity in the process but this has presented issues before during very high-profile US elections and there's no reason to assume everything was completely above-board.

## Challenge Summary

As detailed above, the findings of the election audit successfully summarized the relevant total, county-level, candidate-level, top county, and top candidate data that the Board requested. Moreover, it allows a summary of the data to be rapidly printed to the terminal and also written to an output `election_analysis.txt` file.

![election_analsis terminal output](https://github.com/semionaut/python/blob/main/Election-Analysis/Resources/terminal_output.JPG)

The Python script provided to the board here is deliberately flexible in order to be applied to other data the Board may wish to analyze. Two examples below:

- List with more candidates:
For this example, two more imaginary candidates joined the running, Shetland "Shet" Pony and Emden Goose. This added 135,351 new ballots to the sample. Both candidates ran in Denver only. As you can see in `election_analysis_example1.txt` and the screenshot below, PyPoll seamlessly ingests and reads the new dataset and returns the following result.

![election_analsis terminal output example 1](https://github.com/semionaut/python/blob/main/Election-Analysis/Resources/terminal_output_example1.JPG)

- List with additional counties:
This time, Shetland and Emden made their push in Broomfield and El Paso. As new counties are added to the dataset they are naturally appended to the list compiled by the script.

![election_analsis terminal output example 2](https://github.com/semionaut/python/blob/main/Election-Analysis/Resources/terminal_output_example2.JPG)

As these two tests show, the script can be applied to any dataset that conforms to the same header rows as the sample data. You can expect it to correctly compute a new largest county or new winner in the same way!
