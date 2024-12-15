# Data Analysis Report

# README.md

## Dataset Analysis: World Happiness and Life Quality Indicators

This document outlines the analysis performed on a dataset containing 2363 entries with various indicators of life quality and happiness across different countries and years.

### Dataset Details

- **Entries**: 2363
- **Features**: 11
- **Numeric Columns**: 10
- **Categorical Columns**: 1 (Country name)
  
### Features

1. **Country name**: Name of the country.
2. **year**: Year of the observation.
3. **Life Ladder**: Measure of well-being and happiness on a scale from 0 to 10.
4. **Log GDP per capita**: Natural logarithm of GDP per capita.
5. **Social support**: Support individuals feel they have.
6. **Healthy life expectancy at birth**: Average number of years a newborn is expected to live, assuming current mortality rates persist.
7. **Freedom to make life choices**: The degree of freedom individuals feel in making life choices.
8. **Generosity**: A measure of the generosity of individuals within the country.
9. **Perceptions of corruption**: Level of corruption perceived in the country.
10. **Positive affect**: Measure of positive emotions experienced.
11. **Negative affect**: Measure of negative emotions experienced.

### Data Quality and Missing Values

- **Total Missing Values**:
  - Log GDP per capita: 28
  - Social support: 13
  - Healthy life expectancy at birth: 63
  - Freedom to make life choices: 36
  - Generosity: 81
  - Perceptions of corruption: 125
  - Positive affect: 24
  - Negative affect: 16

### Summary Statistics 

- **Mean Life Ladder**: 5.48
- **Mean Log GDP per capita**: 9.40
- **Mean Social support**: 0.81
- **Mean Healthy life expectancy at birth**: 63.40
- **Mean Freedom to make life choices**: 0.75

### Correlation Analysis

The correlation between various features reveals:

- **Strong positive correlations**:
  - Life Ladder and Log GDP per capita (0.78)
  - Life Ladder and Social support (0.72)
  - Life Ladder and Healthy life expectancy (0.71)

- **Strong negative correlations**:
  - Perceptions of corruption and Life Ladder (-0.43)
  - Negative affect and Life Ladder (-0.35)

### Trends and Insights

1. **Economic Factors**: There is a significant association between economic prosperity (Log GDP per capita) and happiness levels (Life Ladder). Higher GDP tends to lead to happier populations.

2. **Social Connectivity**: Positive correlations between social support and happiness indicators suggest stronger community ties enhance feelings of well-being.

3. **Health and Well-being**: Countries with higher life expectancy also report higher happiness indices, illustrating health's pivotal role in personal happiness.

4. **Freedom and Choices**: There appears to be a correlation between the freedom to make choices and individual happiness, with higher freedom linked to better well-being metrics.

5. **Outliers**: Further investigation is warranted to identify countries with high Life Ladder scores yet low GDP or vice versa, as these could represent unique social variance.

### Visualizations

Several visualizations have been created to showcase the correlations and trends identified during the analysis. These include:

- Scatter plots showing relationships between Life Ladder and other variables (GDP, Social Support).
- Correlation heatmaps.

### Output Files

- Analysis Visualizations:
  - `correlation_matrix.png`
  - `scatter_plot_life_ladder_gdp.png`
  - `scatter_plot_life_ladder_social_support.png`

### Conclusion

This dataset provides critical insights into the factors influencing life quality and happiness across various nations. Analyzing these attributes can help policymakers and social scientists to devise strategies for improving citizens' well-being.

---

### Visualizations

Here are the PNG files generated from the analysis that illustrate the relationships between different variables in the dataset.

1. **Correlation Matrix**: Illustrates how various factors correlate, highlighting significant relationships.
   ![](correlation_matrix.png)

2. **Scatter Plot - Life Ladder vs. Log GDP per capita**: Shows the relationship between economic prosperity and happiness.
   ![](scatter_plot_life_ladder_gdp.png)

3. **Scatter Plot - Life Ladder vs. Social Support**: Depicts the impact of social support on happiness levels.
   ![](scatter_plot_life_ladder_social_support.png)

---

**End of Document**