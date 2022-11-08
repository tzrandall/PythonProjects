# Python Projects

## This is a collection of Python projects to show as a portfolio. I will also include a brief explanation of each of the projects here.

## Virtual Dice
This was a final for a Python class in university (Fall 2021). The idea is that it is a virtual dice set that allows you to roll dice (with an auto sum of what the dice rolls are), repeat a previous roll (useful for things like D&D where you may roll 3 10-sided dice multiple times in a row), generate a history of rolls, and allow the user to view their preferred amount of history (e.g. last 3 rolls, last 10 rolls, etc.). I also added the history.txt that I had used for testing so you could see an example of the dice history with timestamp, sums, and what my rolls had been.

## Weekly Food Planner
This was a personal project that I created for my significant other and me. We go grocery shopping every two weeks so this generates a food schedule for those two weeks and generates a grocery list for those meals without repeated ingredients. I have included the two .txt files to show an example of both the food schedule (2022-11-08.txt) and the grocery list (grocery_list_for_2022-11-08.txt). I use the variable "daysForMeals" to control how many days are in the schedule if we are going on vacation, so we don't buy groceries for meals we won't be home to make, and there are items hard coded into the grocery list that we will get every time we go grocery shopping.

## Log Scrubber
This project was intended to scrub an error log file to count the frequency of errors (an example of this error log is log_scrubber_test.txt). Using the re package to combine separators used to split the errors within the file (In this case "Test: " and "\n") and then use the Counter function from the collections package to create a dictionary of the frequency of errors and their count of how often they occured. I then format these results to create a clean output that is easy to read, an example of this output is displayed in scrubber_results.txt.
