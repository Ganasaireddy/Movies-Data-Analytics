# Movies Data Analysis Insights

## Data Cleaning
- The raw dataset contained missing values in `Rating` and `BoxOfficeRevenue`.
- Missing values in `Rating` were filled using the median value: 5.23.
- Missing values in `BoxOfficeRevenue` were filled using the mean value: $259,968,313.04.

## Basic Analysis
- **Ratings**: The mean rating is 5.39, while the median is 5.23.
- **Box Office Revenue**: The mean revenue across all movies is $259,968,313.04, and the median is $259,968,313.04.
- **Budget**: The average movie budget is $104,683,095.39.

## Key Visual Insights
1. **Rating Distribution**: Most movie ratings are evenly distributed between 1 and 10 due to our synthetic uniform generation, with slight peaks introduced by mean/median filling.
2. **Revenue by Genre**: This plot reveals which movie genres tend to perform best at the box office on average.
3. **Budget vs Revenue**: There is a visualization comparing how a movie's budget impacts its final box office revenue, categorized by genre.
