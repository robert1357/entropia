data <- read.csv("loans.csv")

female_loans <- data$female
male_loans <- data$male

mean_female <- mean(female_loans)
mean_male <- mean(male_loans)

# SD
sd_female <- sd(female_loans)
sd_male <- sd(male_loans)

# CV
cv_female <- (sd_female / mean_female) * 100
cv_male <- (sd_male / mean_male) * 100

# results
cat("Mean Female:", mean_female)
cat("Mean Male:", mean_male)
cat("SD Female:", sd_female)
cat("SD Male:", sd_male)
cat("CV Female:", round(cv_female, 0), "%")
cat("CV Male:", round(cv_male, 0), "%")

# bar plots
barplot(female_loans, main = "F", col = "pink", names.arg = 1:length(female_loans))
barplot(male_loans, main = "M", col = "lightblue", names.arg = 1:length(male_loans))

# Comparison
barplot(c(mean_female, mean_male),
        names.arg = c("Female", "Male"),
        col = c("pink", "lightblue"),
        main = "Comparison of Means by Gender",
        ylab = "Average Loan Amount")

# Boxplot
values <- c(female_loans, male_loans)
groups <- c(rep("Female", length(female_loans)), rep("Male", length(male_loans)))
boxplot(values ~ groups,
        col = c("pink", "lightblue"),
        main = "Loan Distribution by Gender",
        ylab = "Loan Amount")

# t-test
print(t.test(female_loans, male_loans))


