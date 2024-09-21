# Introduction
# In this project, we'll explore a dataset about LEGO and ask interesting questions about the history and products of the LEGO company:
# - What is the most enormous LEGO set ever created, and how many parts did it have?
# - In which year were the first LEGO sets released, and how many sets did the company sell when it first launched?
# - Which LEGO theme has the most sets, and how did the product offering change over time?
# - Did LEGO sets grow in size and complexity over time?

# Data Source: The dataset comes from Rebrickable and includes data on LEGO pieces, sets, and themes.

# Import Statements
import pandas as pd
import matplotlib.pyplot as plt

# Data Exploration

# Load colors.csv to explore the different LEGO colors.
colors = pd.read_csv("data/colors.csv")

# Check for transparent vs opaque colors.
# Uncomment if needed to inspect.
# print(colors.is_trans.value_counts())

# Challenge: Find the number of transparent colors where is_trans == 't' 
# versus the number of opaque colors where is_trans == 'f'.
# Uncomment to explore.
# transparent_colors = colors[colors.is_trans == 't'].shape[0]
# opaque_colors = colors[colors.is_trans == 'f'].shape[0]

# Understanding LEGO Themes vs. LEGO Sets
# A theme can have multiple sets, e.g., Star Wars has many individual LEGO sets.

# Load sets.csv
sets = pd.read_csv("data/sets.csv")

# Display first few rows of the dataset for understanding structure.
# Uncomment if needed for inspection.
# print(sets.head())

# Finding the first LEGO sets released
# This will show us the first sets released by sorting them by year.
first_sets = sets.sort_values('year').head()
# Uncomment if needed for inspection.
# print(first_sets[['year', 'name']])

# Challenge: How many different sets did LEGO sell in their first year (1949)?
# Uncomment to inspect.
# print(sets[sets['year'] == 1949])

# Finding the top 5 LEGO sets with the most parts
max_num_parts = sets.sort_values('num_parts', ascending=False).head(5)
# Uncomment if needed for inspection.
# print(max_num_parts)

# Aggregating the number of LEGO sets released year-on-year.
sets_by_year = sets.groupby('year').count()['set_num']

# Comparing the number of sets released in 1955 vs 2019
sets_1955 = sets_by_year.loc[1955]
sets_2019 = sets_by_year.loc[2019]
# Uncomment to inspect.
# print(sets_1955)
# print(sets_2019)

# Plotting the number of LEGO releases on a line chart
# Exclude data beyond 2018 for full calendar years.
sliced_sets = sets_by_year.loc[:2018]
plt.plot(sliced_sets)
plt.title("Number of LEGO Sets Released Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Sets")
plt.show()

# Aggregating the number of themes released by year
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)

# Plotting the number of themes released by year
# Plot two axes: one for sets, one for themes
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.loc[1949:2019], 'g')
ax2.plot(themes_by_year.loc[1949:2019], 'b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
plt.title("Number of Sets and Themes Released by Year")
plt.show()

# Calculating the average number of parts per set
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})

# Comparing the average number of parts in 1954 and 2017
# Uncomment to inspect.
# print(parts_per_set.loc[1954])
# print(parts_per_set.loc[2017])

# Scatter plot: Do LEGO sets grow in complexity over time?
x = parts_per_set.index[:-2]   # Exclude the last two years
y = parts_per_set.num_parts[:-2]  # Exclude the last two average part counts

plt.scatter(x, y)
plt.title("Average Number of Parts per LEGO Set Over Time")
plt.xlabel("Year")
plt.ylabel("Average Number of Parts")
plt.show()

# Finding Star Wars themes and corresponding sets
themes = pd.read_csv("data/themes.csv")

# Find Star Wars theme IDs in themes.csv
star_war_theme = themes[themes['name'] == 'Star Wars']
star_war_theme_id = star_war_theme['id'].tolist()

# Find corresponding sets in sets.csv
star_war_sets = sets[sets['theme_id'].isin(star_war_theme_id)]
# Uncomment if needed for inspection.
# print(star_war_sets)

# Merging DataFrames to show the number of sets per theme
set_theme_count = sets['theme_id'].value_counts()
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})

# Merging set counts with theme names
merged_df = pd.merge(set_theme_count, themes, on='id')

# Bar plot showing the top 10 themes with the most sets
plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df['name'][:10], merged_df['set_count'][:10], color='red')
plt.title("Top 10 Themes with the Most Sets")
plt.show()
