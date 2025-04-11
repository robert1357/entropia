# Analysis of Differences in Loan Amounts by Gender

Understanding financial disparities between demographic groups is crucial in various fields, including economics, finance, and the social sciences. This analysis focuses on investigating potential differences in loan amounts obtained by individuals of different genders. Using descriptive statistics and inferential tests, our goal is to quantify and statistically evaluate any observed variations in loan amounts between female and male borrowers. This comprehensive approach allows for a nuanced understanding beyond simple averages, considering the dispersion and distribution of the data within each group.

The analysis begins by calculating key descriptive statistics for both female and male loan amounts. These measures provide a summary of the central tendency and dispersion of the data.

# Descriptive Statistics

## Mean  ($\overline{x}$)


The mean, or average, is a measure of central tendency calculated by summing all individual loan amounts within a group and dividing by the total number of observations (n\) in that group.

## Standard Deviation (s)

The standard deviation is a measure of the dispersion or spread of data points around the mean. A higher standard deviation indicates greater variability within the data. The sample standard deviation is calculated as the square root of the variance:

## Coefficient of Variation (CV)

The coefficient of variation is a normalized measure of dispersion that expresses the standard deviation as a percentage of the mean. It allows for a direct comparison of relative variability between datasets with different means. The CV is calculated as:

## Loan Analysis by Gender in Puno

After conducting studies on loans granted in the city of Puno, a sample of 30 male and female lenders was analyzed. The objective of this analysis is to examine differences in loan amounts between the two genders using descriptive statistical tools. To this end, various comparisons will be presented, such as tables summarizing central tendency and dispersion, as well as box plots that allow us to clearly visualize the distribution of loans. This approach will allow us to identify patterns and potential disparities in loans granted to women and men, and will provide a solid basis for assessing the variability in the data between the two groups.

## Statistical Results

- **Mean (Female)**: 1409.143
- **Mean (Male)**: 1452.357
- **Standard Deviation (Female)**: 889.9336
- **Standard Deviation (Male)**: 662.5917
- **Coefficient of Variation (Female)**: 63%
- **Coefficient of Variation (Male)**: 46%

## Descriptive Statistics Analysis

The analysis of descriptive statistics highlights differences in the loan amounts between female and male groups.

- The mean loan amount for females is approximately 1409.143, while for males, it is slightly higher at 1452.357. This suggests a marginal tendency for males to receive slightly larger loans on average within this dataset.

When examining the variability of loan amounts:

- The standard deviation for females (SD = 889.9336) is significantly larger than that for males (SD = 662.5917). This indicates that the loan amounts for females are more widely dispersed around their mean, whereas for males, the amounts are more closely clustered around their mean.

To understand the relative variability:

- The coefficient of variation (CV) for females is 63%, reflecting a high degree of relative dispersion.
- In contrast, the CV for males is 46%, indicating lower relative variability in their loan amounts.
  
## Female

![female graphic](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000750281.png?raw=true)

### Chart F (Female)

It showed a distribution where the majority of observations were concentrated at relatively
low values up to category 11, followed by a steep and significant increase in categories 12,
13, and 14, reaching the highest values. This suggested greater variability in loan amounts
for women, with a notable proportion receiving significantly larger loans.

### chart M (male)
![malegraphic](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000757194.png?raw=true)

### chart M (male)
This showed a distribution with a more gradual and sustained increase in loan amounts
across categories. While the highest values were also found in the lower categories, the
increase was less pronounced than in the female group. This suggested a smaller relative
dispersion in loan amounts for men.

## comparation chart
![coparacion of means by gender graphic](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000805026.png?raw=true)
### Bar Chart Analysis: Average Loan Amount by Gender
It can be seen that the height of the bar for the male group is slightly higher than the
height of the bar for the female group. This indicates that, on average, the loan amount for
men in this data set is marginally higher than the average loan amount for women. However,
visually, the difference between the heights of the two bars appears to be quite small.

## loan distribution by gender
![distribution graphic](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000813682.png?raw=true)
### Box Plot Analysis: Loan Amount Distribution by Gender
This box plot summarizes the distribution of loan amounts for the female and male groups,
providing information on the median, quartiles, interquartile range (IQR), and potential
outliers.
### Box for the Female Group (Pink)
• The horizontal line inside the box represents the median loan amount for women, which
is around 1000.
• The lower and upper borders of the box indicate the first quartile (Q1) and third
quartile (Q3), respectively. Approximately 25% of female loan amounts are below Q1
(around 800), and 25% are above Q3 (around 1500).
• The height of the box represents the interquartile range (IQR = Q3 - Q1), which
contains the middle 50% of the data. For women, the IQR is approximately 700.
• The vertical lines extending from the box (the ”whiskers”) reach the most extreme
values within a range of 1.5 times the IQR from the quartiles. The lower whisker
reaches approximately 500, and the upper whisker extends to approximately 2000.
• The small circle above the upper whisker indicates an outlier, representing a significantly higher loan amount than the rest of the data for the female group (approximately
3000).
### Box for the Male Group (Blue)
• The median loan amount for men is slightly above 1,100.
• The first quartile (Q1) is around 1,000, and the third quartile (Q3) is close to 2,000.
• The IQR for men is approximately 1,000.
• The whiskers extend from approximately 500 to approximately 2,700.

# evidence
## Data Evidence
![data evidence ](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000932936.png?raw=true)


The following image presents the raw data from the lenders, including both male and female participants, analyzed for this study. The data consists of the loan amounts granted to each individual, which are used to calculate descriptive statistics such as the mean, standard deviation, and coefficient of variation. This image serves as the primary evidence for the analysis, providing a visual representation of the loan amounts for both sexes in the study. The data displayed here support the statistical analysis and the conclusions drawn about the differences in loan amounts between male and female borrowers.

## code Evidence
![codee evidence ](https://github.com/robert1357/entropia/blob/main/imagen_2025-04-11_000952417.png?raw=true)

The following image and code snippet provide evidence of the statistical results and graphs generated from the analysis. The R code used to calculate the descriptive statistics (mean, standard deviation, coefficient of variation) and create visualizations such as box plots is included. These results and visualizations help support the conclusions drawn regarding the differences in loan amounts between female and male borrowers.


