import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set working directory to the current script's directory
output_dir = r"c:\Users\yashaswini reddy\OneDrive\Desktop\task 2004"
os.chdir(output_dir)

# 1. Synthetic Data Generation
np.random.seed(42)
num_movies = 200
genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Romance', 'Horror']

data = {
    'MovieID': range(1, num_movies + 1),
    'Title': [f'Movie {i}' for i in range(1, num_movies + 1)],
    'Genre': np.random.choice(genres, num_movies),
    'Rating': np.random.uniform(1.0, 10.0, num_movies),
    'BoxOfficeRevenue': np.random.uniform(10_000_000, 500_000_000, num_movies),
    'Budget': np.random.uniform(5_000_000, 200_000_000, num_movies),
    'ReleaseYear': np.random.randint(2000, 2024, num_movies)
}

df_raw = pd.DataFrame(data)

# Introduce missing values for data cleaning
missing_rating_indices = np.random.choice(num_movies, size=15, replace=False)
missing_revenue_indices = np.random.choice(num_movies, size=20, replace=False)
df_raw.loc[missing_rating_indices, 'Rating'] = np.nan
df_raw.loc[missing_revenue_indices, 'BoxOfficeRevenue'] = np.nan

# Save raw dataset
df_raw.to_csv('movies_raw.csv', index=False)
print("Saved movies_raw.csv")

# 2. Data Cleaning
df_clean = df_raw.copy()
# Handle missing values: fill Rating with median and BoxOfficeRevenue with mean
rating_median = df_clean['Rating'].median()
revenue_mean = df_clean['BoxOfficeRevenue'].mean()
df_clean['Rating'] = df_clean['Rating'].fillna(rating_median)
df_clean['BoxOfficeRevenue'] = df_clean['BoxOfficeRevenue'].fillna(revenue_mean)

# Save cleaned dataset
df_clean.to_csv('movies_cleaned.csv', index=False)
print("Saved movies_cleaned.csv")

# 3. Basic Analysis (Mean and Median)
analysis_stats = {
    'Rating_Mean': df_clean['Rating'].mean(),
    'Rating_Median': df_clean['Rating'].median(),
    'BoxOffice_Mean': df_clean['BoxOfficeRevenue'].mean(),
    'BoxOffice_Median': df_clean['BoxOfficeRevenue'].median(),
    'Budget_Mean': df_clean['Budget'].mean(),
    'Budget_Median': df_clean['Budget'].median()
}

print("Basic Analysis Stats:")
for k, v in analysis_stats.items():
    print(f"{k}: {v:.2f}")

# 4. Data Visualization
sns.set_theme(style="whitegrid")

# Plot 1: Rating Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating (1-10)')
plt.ylabel('Frequency')
plt.savefig('rating_distribution.png')
plt.close()
print("Saved rating_distribution.png")

# Plot 2: Average Box Office Revenue by Genre
plt.figure(figsize=(10, 6))
avg_revenue = df_clean.groupby('Genre')['BoxOfficeRevenue'].mean().sort_values(ascending=False)
sns.barplot(x=avg_revenue.index, y=avg_revenue.values, palette='viridis')
plt.title('Average Box Office Revenue by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Box Office Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_by_genre.png')
plt.close()
print("Saved revenue_by_genre.png")

# Plot 3: Budget vs Box Office Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Budget', y='BoxOfficeRevenue', hue='Genre', alpha=0.7)
plt.title('Budget vs Box Office Revenue')
plt.xlabel('Budget ($)')
plt.ylabel('Box Office Revenue ($)')
plt.tight_layout()
plt.savefig('budget_vs_revenue.png')
plt.close()
print("Saved budget_vs_revenue.png")

# 5. Write Insights
insights_text = f"""# Movies Data Analysis Insights

## Data Cleaning
- The raw dataset contained missing values in `Rating` and `BoxOfficeRevenue`.
- Missing values in `Rating` were filled using the median value: {rating_median:.2f}.
- Missing values in `BoxOfficeRevenue` were filled using the mean value: ${revenue_mean:,.2f}.

## Basic Analysis
- **Ratings**: The mean rating is {analysis_stats['Rating_Mean']:.2f}, while the median is {analysis_stats['Rating_Median']:.2f}.
- **Box Office Revenue**: The mean revenue across all movies is ${analysis_stats['BoxOffice_Mean']:,.2f}, and the median is ${analysis_stats['BoxOffice_Median']:,.2f}.
- **Budget**: The average movie budget is ${analysis_stats['Budget_Mean']:,.2f}.

## Key Visual Insights
1. **Rating Distribution**: Most movie ratings are evenly distributed between 1 and 10 due to our synthetic uniform generation, with slight peaks introduced by mean/median filling.
2. **Revenue by Genre**: This plot reveals which movie genres tend to perform best at the box office on average.
3. **Budget vs Revenue**: There is a visualization comparing how a movie's budget impacts its final box office revenue, categorized by genre.
"""

with open('insights.md', 'w') as f:
    f.write(insights_text)

print("Saved insights.md")
print("All tasks completed successfully!")
