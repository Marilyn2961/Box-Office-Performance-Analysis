# Movie Industry Data Analysis: Box Office Performance & Trends

## Project Overview

This project explores financial and audience patterns across the global movie industry using a blend of publicly available datasets. Our objective was to uncover **what factors contribute most to a movie’s commercial success**, particularly in terms of **Return on Investment (ROI)**, **box office revenue**, and **audience/critic reception**.

We applied a structured data science workflow from data wrangling and exploratory analysis to hypothesis testing and business recommendations to generate valuable insights that can guide film production and release strategies.


## Business Understanding

The film industry is inherently high-risk. Studios invest millions into movie productions without fully understanding which factors drive profitability. This is even more challenging for **new or small studios** that lack historical data or industry experience.

We sought to answer the following key business questions:

- Which **genres** offer the highest return on investment (ROI)?
- What **budget ranges** maximize profitability?
- Do **audience and critic ratings** predict financial success?
- Is there an **optimal release window** for specific types of films?

This project provides data-backed answers to these questions, helping stakeholders **minimize financial risk** and **optimize production strategies**.


##  Data Sources

The data used in this project was sourced from a provided zipped dataset folder not scraped directly from the websites). However, for reference and further exploration, the original data is publicly available from the following platforms:

- **[The Numbers](https://www.the-numbers.com/)**  
  → Source for production budgets and revenue (domestic and international)  
  *Used file: `tn.movie_budgets.csv`*

- **[Box Office Mojo](https://www.boxofficemojo.com/)**  
  → Used for cross-checking box office performance and studio-level insights  
  *Used file: `bom.movie_gross.csv`*

- **[IMDb](https://www.imdb.com/)**  
  → Provided core metadata including titles, release years, genres, runtimes, and ratings  
  *Used tables from SQLite DB: `movie_basics`, `movie_ratings`*

- **[Rotten Tomatoes](https://www.rottentomatoes.com/)**  
  → Supplemented genre classification and aggregated critic reviews  
  *Used file: `rt.movie_info.tsv`*

- **[TMDb (The Movie Database)](https://www.themoviedb.org/)**  
  → Contributed genre tags, popularity scores, and audience sentiment  
  *Used file: `tmdb.movies.csv`*


## Project Objectives

- Analyze ROI trends across genres, release seasons, budgets, languages, and runtimes
- Investigate correlations between ratings and revenue
- Evaluate the impact of release timing and language
- Provide **actionable business recommendations** for studios and investors


## Tools & Technologies

- **Languages**: Python 3
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`
- **Database**: SQLite
- **Visualization**: Tableau, PowerPoint
- **IDE**: Jupyter Notebook
- **Version Control**: Git & GitHub


## Methodology

This project followed a structured, collaborative workflow aimed at generating actionable insights from complex, multi-source movie industry datasets. Our methodology was divided into four key phases:

### 1. Data Exploration

- Conducted initial profiling across datasets from IMDb, TMDb, The Numbers, Rotten Tomatoes, and Box Office Mojo.
- Investigated distributions, missing values, and inconsistencies in key features.
- Mapped common identifiers to link data across platforms.

### 2. Data Preparation & Cleaning

- **Standardized** column names, formats, and merged datasets using shared identifiers.
- **Missing Value Handling**:
  - **Financial columns** : Imputed with **median** values.
  - **Other numeric columns**: Filled with **0**.
  - **Categorical columns**: Replaced with **"Unknown"**.

- **Data Transformation**:
  - Converted categorical values to be compatible with analysis and visualization.


### 3. Data Analysis

This phase involved two parallel and iterative tracks:

#### a) Data Visualization

We created targeted visualizations to explore relationships, trends, and patterns:

##### Financial Performance & ROI Analysis

- 1.1 Statistical summary of movie financials (budget, gross, ROI)
- 1.2 ROI vs Runtime — Identified runtime performance zones
- 1.3 Top 10 Genres by Average ROI and Average Profit
- 1.4 Budget vs ROI — Understanding cost-efficiency
- 1.5 Seasonal ROI Trends — Average ROI by release season

##### Content Quality & Ratings Impact

- 2.1 Audience vs Tomatometer Ratings — by genre

##### Market Dynamics: Timing, Language & Accessibility

- 3.1 Language Popularity — Relationship between language and audience engagement
- 3.2 Top 10 Most Popular Genres (2014–2024) — With trend lines
- 3.3 Long-term Genre Popularity Trends

#### b) Hypothesis Testing

We ran statistical tests and modeling techniques to confirm or refute data-driven assumptions:

- **Correlation Analysis**: Assessed the strength between audience/critic scores and box office performance.
- **T-Tests**: Tested if seasonality significantly impacts ROI.
- **ROI Modeling**: Measured how different budget levels and genres influenced return on investment.
- **Runtime Analysis**: Evaluated if runtime affects profitability.
- **Language Impact**: Compared English vs multilingual film performance.


## Business Recommendations

### 1. ROI & Financials
![Top 10 Genres by Average ROI](https://github.com/Marilyn2961/Box-Office-Performance-Analysis/blob/master/Images/ROI.Genre.png?raw=true)

- **Invest in high-ROI genres** such as Cult Movies, Horror, Special Interest, Documentary, and Classics.
- **Aim for moderate production budgets** ($20M–$60M) and runtimes between 100–120 minutes.

  - These genres consistently outperform in profitability  
  - Mid-range budgets balance cost and return  
  - 100–120 minutes is the optimal runtime performance zone for ROI

### 2. Ratings & Content Quality
![Audience vs Tomatometer Ratings — by genre](https://github.com/Marilyn2961/Box-Office-Performance-Analysis/blob/master/Images/Genre.AudienceRating.png?raw=true)

- Prioritize **high-quality scripts** that resonate with both audiences and critics. Focus on genres like Classics, Western, Documentary, Art House & International, and Drama.

  - Positive ratings are significantly correlated with box office success  
  - High critic scores lead to word-of-mouth and sustained revenue

### 3. Market Dynamics & Timing
![Seasonal ROI Trends — Average ROI by release season](https://github.com/Marilyn2961/Box-Office-Performance-Analysis/blob/master/Images/ROI.Season.png?raw=true?raw=true)

- **Target summer and holiday releases**, and consider **multilingual productions** for broader market reach.

  - Summer releases have significantly higher average gross  
  - Multilingual/English-language films have better global penetration  
  - Thrillers and action genres show growth in global appeal


## Limitations of the Analysis

1. **Missing or Incomplete Data**  
   - We filled missing financials with medians, and other numerical columns such as rating with zeros, and categories with 'Unknown'. This preserves data but may understate extremes, lower averages, and mask true distributions.

2. **Selection Bias**  
   - The focus may be skewed towards mainstream or higher-profile movies with available data.

3. **Simplified Genre Classification**  
   - Movies often belong to multiple genres, but analysis may treat them as a single genre, losing nuance in genre-specific insights.

4. **ROI Calculation Limitations**  
   - ROI does not consider marketing expenses, distribution fees, or other revenue streams (streaming, merchandise).  
   - Product_Budgets, Domestic_Gross and Foreign_Gross are taken as reported without inflation adjustment or currency normalization.

5. **Correlation vs Causation**  
   - Significant correlations (e.g., ratings and worldwide_gross) do not imply causation.  
   - Other factors like Authors, Directors, Star Players, franchise effects, or competition were not included.



## Access Project Materials

- [Jupyter Notebook](https://github.com/Marilyn2961/Box-Office-Performance-Analysis/blob/master/Box_Office_Performance_Analysis.ipynb)  
- [Dashboard on Tableau](https://public.tableau.com/app/profile/rose.miriti/viz/Phase_2_17494760146190/Dashboard?publish=yes)  
- [Presentation Slides](https://github.com/Marilyn2961/Box-Office-Performance-Analysis/blob/master/Presentation.pdf)

