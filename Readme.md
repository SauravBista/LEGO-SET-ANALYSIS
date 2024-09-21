LEGO Data Analysis Project
This project explores a dataset of LEGO sets to uncover insights about the history of LEGO, their product offerings, and trends over time. Using Python, pandas, and matplotlib, we analyze the number of LEGO sets released each year, the themes they belong to, and the complexity of the sets based on the number of parts.

Introduction
The LEGO company has a long and fascinating history. This project dives into a dataset containing information about LEGO sets and themes spanning multiple decades. The goal is to answer the following questions:

What is the most enormous LEGO set ever created, and how many parts did it have?
In which year were the first LEGO sets released, and what were they called?
Which LEGO theme has the most sets?
How has LEGO expanded its product offerings year-on-year?
Do LEGO sets tend to have more or fewer parts over time?
Data Source
The dataset used in this project is sourced from Rebrickable, which contains a compilation of data on all LEGO sets and themes.

The following CSV files were used:

colors.csv: Contains the list of LEGO colors.
sets.csv: Contains information about each LEGO set, including its name, year of release, theme, and number of parts.
themes.csv: Contains the themes of LEGO sets with theme IDs linking to the sets.csv.
Project Setup
Prerequisites
You need the following libraries to run the project:

pandas
matplotlib
You can install these using pip:

bash
Copy code
pip install pandas matplotlib
Running the Project
To run the analysis, simply execute the Python script or notebook. The project will read the CSV files and generate visualizations to answer the questions mentioned above.

Exploratory Data Analysis
We explored various aspects of the LEGO dataset, such as:

The number of LEGO sets released year-on-year.
The top 5 LEGO sets with the most parts.
The themes that have the most sets.
The evolution of the average number of parts per LEGO set over time.
An in-depth analysis of Star Wars LEGO sets.
Conclusion
This analysis reveals how LEGO has evolved over the years in terms of the number of sets, themes, and parts. From the early days of basic sets to today’s massive, intricate designs, LEGO continues to captivate audiences of all ages. This project provided valuable insights into LEGO’s product development strategy and identified standout themes and sets.