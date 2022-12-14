# W-Method
This repository contains the development of W method calculation. W Method is used to optimize decision tree to solve multicriteria decision making. 

## Versioning History:
- 2022-12-10 - 1.0 - MAJOR : Additional of new W Method with simple logic
- 2022-12-10 - 1.1 - MAJOR : Additional null column to continuous itterations, finalize the singular decision tree method.
- 2022-12-12 - 1.2 - MAJOR : Additional options to query from database, additional function to select function to maximize or minimize, additional input rank to dataframe.
- 2022-12-13 - 1.2 - MINOR : Additional input decision used
- 2022-12-16 - 1.2 - MINOR : bug fix about N/A value and additional elapsed calculation time
- 2022-12-16 - 1.2 - MAJOR : Decision function working but still returning final branch that doesn't the output branch
- 2022-12-17 - 1.3 - MAJOR : Fully working W Method
- 2022-12-17 - 1.3 - MINOR : Adjusted case study

## How to use the repo:
1. This repo use several file such as:
	- **W.py**
	- **output.csv** : use for inputing the output variable and the raw payoff of an output.
	- **data.csv** : the master data that is use for GUI to input event node, output, decision node, and branch probability
	- **criteria.csv** : the interface for entering the criteria category
2. After entering the value to **output.csv and Data.csv**, run the W.py.
3. Enter the function for calculation, whether **maximize or minimization**.
4. Enter the weight for each category based on criteria priority.
5. The result will be generated in **mData.py**.