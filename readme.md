
## Statistics

- is the science of conducting studies to collect, organize, summarize, analyze, and draw a conclusion out of data.
- deals with collective informative data, interpreting those data, and drawing a conclusion from that data.

## Probability

- Probability is the likelihood of an event occurring.
- Its about quantifying how likely each event is on its own.
- We measure probability with numeric values between 0 and 1, because we like to compare the relative likelihood of events.
- We’ll use probability theory to build models.
- We’ll use probability theory to evaluate models. 

- independent events
- dependent events
- conditional probability
- bayes theorem

## Types Of Statistics

- Descriptive
    1.	Helps us to organize and summarize data using numbers and graphs to look for a pattern in the data set.
    2.	Measures of Central tendency: Mean, Median, Mode.
    3.	The measure of Variability: Standard Deviation, Variance & Range
    (*Central Tendency- it is the single value which attempts to describe a set of data)
- Inferential
    1.	To make an inference or draw a conclusion from the population, sample data is used.
    2.	Using probability to determine how confident we can be that the conclusion we make is correct. (Confidence Interval & margin of error)
    Example: Our primary concern is to find out how many people like blue cars in the data set.

## Types of Data / Levels of measurement

- Categorical/Qualitative
    - Represents groups or categories
    - Categorical divided into two categories
        - Nominal
            - Represents categories that cannot be put in any ordered.
        - Ordinal
            - Represents categories that can be ordered.
- Numerical/Quantitative
    - Numerical divided into two categories
        - Discrete 
            - Separate and distinct.
            - Counted finitely.
            - Integers
            - Example: 
                - Number of students in class: 60
                - Number of accounts in bank: 2
        - Continuous
            - Can't be counted but can be measured.
            - Continous in infinite.
            - Fractional numbers: 2.4, 5.7, 6.7.
            - Example: 
                - Height of students in class: 161cm, 165cm, 171cm
                - Distance
                - Speed
            - Numerical Continuos further divided into:
                - Interval
                    - Ordered units having the same difference
                    - No true zero
                    - Can't apply descriptive or inferential stats
                - Ratio
                    - Same as interval data
                    - Has true zero

## Measures of Central Tendency

Refers to the measure used to determine the centre of the distribution of data.

- Mean
    - Most used and stable measure
    - Affected by extreme values
    - May not exist as a data point in the set
- Median
    - Value that divides ranked data points into halves. Median is the middle value in the list of numbers.
    - The median for the sample data arranged in increasing order is defined as :
        - If"n" is an odd number - Middle value 
        - If "n" is an even number - Midway between the two middle values
    - May not exist as data point in the set
    - Influenced by position of items, but not their values
- Mode
    - Most frequent data point i,e mode is the value that occurs most often.
    - If no number is repeated, then there is no mode for the list.
    - Mode exists as a data point
    - Unaffected by extreme values
    - Usefull for qualitative data
    - May have more than 1 value

- Measures of Central Tendency is usually not sufficient measure to reveal the shape of a distribution of data set
- We need a measure that can provide some info about the variation among the data set values

- The measure that help us to know about the spred of a data set are called measures of dispersion.

- The measure of central tendency and dispersion taken together give a better picture of a data set.


- Population
    - The entire set of objects or individuals or interests or the measurements obtained from all individuals or objects of interest.
- Sample
    - A portion, or part, of the population of interest.
    - Sampling techniques:
        - Simple Random Sampling
            - Every member of population has equal chance of being selected in sample.
            - Ex: Election exit poll.
        - Stratified Sampling
            - Population is split into non-overlaping groups.
            - Ex: Based on age, profession etc.
        - Systematic Sampling
            - nth interval is picked.
            - Ex: Covid survey, every 9th person is picked.
        - Convenience Sampling
            - Domain/Experienced people are involved.
            - Ex: Survey on specific topic

## Measures of Dispersion (Dispersion == Spread) or 

- Range
    - The difference between the smallest and the largest observations in the sample is called Range.
    - For example, the minimum and maximum blood pressure are 113 and 170, respectively. Hence the range is 57.
    - Pros
        - It is easy to calculate.
        - It’s implemented for both "best" or " worst" case scenarios.
    - Cons
        - Too sensitive for extreme values.
- Variance
    - Variance is a measure of spread of data around the mean.
    - It is measured by first finding the Deviation of each element in a data set from the mean, and then by squaring it. 
    - Variance is an average of all squared deviations.
    - Sample Variance
        - The sample variance, s squared, is the arithmetic mean of the squared deviations from the sample mean
- Standard Deviation
    - Square root of variance
    - Why SD ?
        - Variance is too large for any viz or comparison
    - Standard deviation tells us about the concentration of data around the mean of the data set.
    - Standard deviation (S) is the square root of the variance.
    - Sample Standard Deviation
        - The sample standard deviation has the advantage of being in the same units as the original variable (x).
    - Facts about SD:
        - If the standard deviation is small, the data has little spread (i.e., the majority of points fall very near the mean).
        - If standard deviation = 0, there is no spread. This only happens when all data items are the same value.
        - The standard deviation is significantly affected by outliers and skewed distributions.

## Coefficient of Variation
    - Standard deviation divided by mean
    - Dispersion of data relative to its mean
    - Usefull in comparing two dataset

## Random Variables

- A random variable is a set of all the possible values from a random experiment.
- A random variable is a variable whose possible values are outcomes of a random phenomenon. 
- Random variables can be discrete or continuous.   
    - Discrete variables can only take specific values
    - Continuous random variables can take any value (within a range).
- Discrete Random Variable
    - A random variable can take a value within a set, is called as discrete RV 
    - The discrete random variable is one that may take on only a countable number of distinct values.
	- If the random variable can take only the finite number of distinct values, then it must be a discrete random variable.
    - Examples of discrete random variables :
        * Number of children in the family. 
        * The Friday night attendance at a Multiplex. 
        * The number of patients in the doctor's surgery. 
        * The number of defective light bulbs in the box.
    - The probability distribution of the discrete variable is the list of the probabilities associated with every possible value. 
- Continuous Random Variable
    - A random variable where it can take any real value, is called as continous RV
    - It is the one that takes an infinite number of possible values. 
    - Continuous random variables usually are the measurements. 
    - For example:
        - the height of a person
        - the weight of a machine
        - the amount of sugar in tea, etc.
    - we represent a continuous distribution with a probability density function (pdf) such that the probability of seeing a value in a certain interval equals the integral of the density function over the interval
    - A continuous random variable is defined throughout values and is represented by the area under a curve.

## Variable Measurement Scales

- Nominal 
    - Categorical data
    - Ex: colors, gender, types of flowers
- Ordinal 
    - Order of data matters, than its values
    - Assign a rank based on value, utilize the rank info.
- Interval
    - Order and value of data matters. Natural zero is not present.
    - Example: Degree celsius & Fahrenheit. 0 Degree celsius doesnt make any sense!
- Ratio
    - Example: Degree kelvin

# Measure of variable relationship

- Covariance
    - Measures the directional relationship between two variables
    - Three types:
        - Positive CoV
            - If 1 variable increase, second variable also increases.
        - Negative CoV
            - If 1 variable increase, second variable decreases.
        - Zero Cov
            - No relation
    - Ex: https://images.app.goo.gl/z5kf64ZZr2GwmnTk7
- Correlation
    - Correlation tells us the type of relationship two variables have
    - But how strong is this relationship?
    - Correlation provides a value to know how positive/negative the relationship is.

## Set 

- A set is a well-defined collection of objects.
- A set that contains zero elements is called a  null set (empty set).
    - An empty set is denoted by { }, which is called a null set.
- Let A and B be two sets. Then A is said to be a subset of B (or B is a superset of A) if every element of A belongs to B.
- A set may be defined by mentioning its elements written in brackets. 
- For example, if Set X consists of the numbers 1, 2, 3, and 8, we may say X = {1, 2, 3, 8}.

- Operations of Set

    - Union
        - The union of two sets is defined as the set of elements that are present in one or both sets. Thus, if A is {1, 2} and B is {2, 3, 4}, the union of sets A and B is:
        A ∪ B = {1, 2, 3, 4}

    - Intersection
        - The common elements that are present in both sets are known as the intersection of two sets. Thus, if A is {1, 2,5} and Y is {2, 3, 4,5}, the union of sets A and B is: The intersection of two sets is 
        A ∩ B = {2,5}

    - Complement
        - The complement of an event is defined as it is the set of all the elements but not in the event. 
        - Thus, if the sample space is {0, 2, 3, 4, 8, 9}, and X is {2, 3, 4}, then the complement of set X is
        X' = {0, 8, 9}

# Inference stats

## Distributions

- A distribution is a function that shows possible values for a variable & the frequency of their occurence
- Divided into two main categories:
    - Discrete
        - Same concept as Discrete variable
    - Continuous
        - Same concept as Continuous variable

## Skewness

- Measures imbalance or Asymmetry from the mean of a data distribution
- Skewness is defined as a measure of the dataset’s symmetry. 
- Values concentrated on one side of the data distribution
- A perfectly symmetrical data set will have zero skewness.   

- Positive Skewness with Dataset
    - Tail on the right side is longer
    - Tells that outliers on the right side
- Negative Skewness with Dataset
    - Tail on the left side is longer
    - Tells that outliers on the left side
- If the skewness is between -0.5 and 0.5, the data are fairly symmetrical. 
- If the skewness is between -1 and – 0.5 or between 0.5 and 1, the data is moderately skewed.
- If the skewness is greater than 1 or less than -1, the data is highly skewed.

## Probability Density Function

- A Probability Distribution is a mathematical function through which the probability of occurrence of different possible outcomes in an experiment can be calculated.
- If the probability of an event is higher, it’s more likely that the event will occur.

### Types of the probability distribution

- Normal Distribution (Gaussian Distribution)
    - Is a type of Continous Distribution
    - Normal Distribution is one of the most common continuous probability distribution. 
    - Used to represent random variables whose distribution is not known.
    - This type of distribution is symmetric, and it's mean, median, and mode are equal.
    - Mathematically, Gaussian Distribution is represented as:
                        N~(μ, σ2 )
        - Where N stands for Normal
        - symbol ~ for distribution
        - μ stands for mean and 
        - σ2 stands for the variance

    - ### Empirical Formula
        - The empirical rule states that for the Normal Distribution, nearly all of the data will fall within three range of standard deviations of a mean. 
        - The Empirical Rule is often used to forecast when obtaining the right data is difficult or impossible to get. 
        - The empirical rule can be understood through the following:
            - 68% of the data falls within the 1st standard deviation from the mean.
            - 95% fall within two standard deviations.
            - 99.7% fall within three standard deviations.
    - ### Standard Normal Distribution
        - Understanding Standardization in the context of statistics. 
        - Every distribution can be standardized based on mean and variance of a variable are μ and σ2.
        - Standardization is the process of transforming the distribution to one with a mean of 0 and a standard deviation of 1.
        i.e.,  (μ, σ2 ) → ~ (0, 1)
        - When a Normal Distribution is standardized, a result is called a Standard Normal Distribution.
        i.e., N (μ, σ2 ) → ~ N(0, 1)
        
        - Formula for standardization https://images.app.goo.gl/WgADfaCTaDFgtbRF7      

        - Where x is a data element, μ is mean & ‘σ’ is the standard deviation, and Z is used to denote standardization, and Z is known as the z-score.
        - With the help of Z scores, we can come to know how far a value is from the mean. 
        - Essence of z-score  is tells use the score is above/below the mean
        - When you standardize a random variable, its μ becomes 0, and its standard deviation becomes 1.
        - If the Z score of x is 0, then the value of x is equal to the mean.
        - Using this standardized normal distribution makes inferences & predictions much easier.
    - ### Probability Density Function and Mass Function 
        - Probability density function and Probability mass function defines a Probability Distribution for a random variable.
        - If we know the variance and the mean of the dataset, then we can calculate the PDF and PMF. - PDF and PMF tell how well data is distributed around mean and standard deviation within a particular curve.
    - ### Cumulative Density Function
        - The cumulative distribution function (CDF) of a random variable is another method to describe the distribution of random variables.
        - The cumulative frequency is the sum of the frequencies. 
        - Cumulative frequency starts at the frequency of the 1st brand, and then we add the 2nd, then 3rd, and so on until it finishes 100%.
        - For all kinds of random variables (discrete, continuous, and mixed), CDF can be defined.

- Bernoulli’s Distribution

    - Bernoulli distribution is a discrete probability distribution of a random variable that has only two outcomes., namely 1 (success) and 0 (failure). 
    - where n = 1 occurs with probability p and n = 0 (usually called a “failure”) occurs with probability q = 1 – p, where 0 < p < 1. 

- Binomial Distribution
    - Is a type of Descrete Distribution
    - The binomial distribution is used when there is more than one outcome of a trial. These outcomes are labeled as “Success” and “Failure.”
    - Here, the probability of both outcomes is the same for all the trials.
    - Each trial is independent. 
    - The parameters of a binomial distribution are:
        - p; where p is the probability of success in the individual trial
        - n; where n is the total number of trials.
    - Python binomial distribution tells us the probability how often there will be a success in ‘n’ independent experiments. 
    - Such experiments are yes-no questions. One example may be tossing a coin.

- Uniform Distribution
    - Is a type of Descrete Distribution
    - The probability distribution function of the continues uniform distribution:
    - https://images.app.goo.gl/EtdaPw2X75Kp6nmP7 
    - Since the area under the curve must be equal to 1, and the length of the interval determines the height of the curve, the following figure shows a uniform distribution (a,b). 
    - Note that since the area needs to be 1. The height is set to 1/(b−a)1/(b−a).
    - Ref image https://images.app.goo.gl/4SeRmheVip3iGqoJ6
    - EXAMPLE:  
        - If we roll a die(numbered 1 to 8), then the probability of getting 1 is one out of 8.
        - Similarly, the probability of getting 2 to 6 is 1/6. There is an equal chance to get each of 8 results (outcomes).
        - When we plot in histogram, we get to see uniform distribution
- Student T Distribution
    - The T distribution is bell-shaped & symmetric, like the normal distribution, but has more massive tails. - The T distribution is the family of distributions that looks identical to the normal distribution curve.
    - Only a bit shorter and fatter.
    - It is used in place of the normal distribution when we have small samples. (n<30)
    - The T distribution similar is to the normal distribution if the sample size increases. 

    - The t distribution has the following properties:
        - The distribution’s mean = 0 .
        - v / ( v - 2 ) is equal to variance, where v is the degrees of freedom.
        - The variance is although close to 1, but it is always greater than 1 when degrees of freedom is greater. 
        - The t distribution is similar to the standard normal distribution, with infinite degrees of freedom.
    - Student t distribution and Probability:
        - When ‘n’ - the sample size, is drawn from a population having a normal distribution, using the equation of t-distribution, the sample mean is transformed into a t statistic. 
        - Following is the equation:
        t = [ X - μ ] / [ S / sqrt( n ) ]
        where, μ is the population mean
        X is the sample mean
        the sample size is n
        n – 1 is degrees of freedom here and 
        s is the standard deviation of the sample.

- Poisson Distribution
    - Poisson Distribution can be used to find the probability of several events in a time period.
    - Conditions for Poisson Distribution:
        - Here the events can occur independently.
        - An event can occur any number of times.
        - The rate of occurrence is constant; i.e., the rate does not change based on time.

## Z Stats

- It allows us to calculate the score probability,  which occurs within our normal distribution. 
- It enables us to compare two scores of different normal distributions. 
- z-score is defined as the number of the standard deviations a particular point is away from the mean.
- The basic z score formula is: z= (x – μ) / σ
- When you have multiple samples and their sample means (the standard error), you will use the following z-score formula:
      z = (x – μ) / (σ / √n)

## Central Limit Theorem

- Regardless of the initial shape of the population distribution, sampling distribution will approximate to a normal distribution.
- As the sample size increases, sampling distribution will get narrower and more normal.
- After fetching different samples, which are enough in numbers, we can then calculate the mean of each sample and then plot the various distributions.
- Also, if we take the average of the sample mean, then the result will be equal to the actual population mean &  the standard deviation equals σ/√n.
- Where, ‘σ’ is the population of std deviation
    n = the sample size(i.e., # of observations in our sample)

    - ## Important points while applying the Central Limit Theorem:
        - The distribution of the original(population) dataset does not matter. It could be normal, uniform, binomial, etc.
        - The distribution of the sample means would be Normal Distribution
        - Larger the number of samples taken from the population, the closer to a Normal Distribution the sample means will be. 
        - The samples extracted should be more significant than 30 observations.
        - The sample mean average extracted will be approximately equal to the mean of the population, and its variance would be similar to the original variance, which is divided by the sample size, i.e., ‘n’.

## Hypothesis

- Hypothesis means an idea made from limited evidence.
- It is a starting point for further investigation.
- Go through the 7-step process of hypothesis online.
- An assumption is called a hypothesis, and the statistical tests used for this are called statistical hypothesis tests.
- Two hypotheses:
    - H0 is the Null Hypothesis.
        - The Null Hypothesis assumes that there is a "NO" difference between two sets of values.
    - H1 or HA is the alternative Hypothesis.
        - The alternative hypothesis used in hypothesis testing is contrary to the null hypothesis.
- Hypothesis Testing’s Mechanism
    - Analyze the performance of the students of the university on an overall basis.
    - Here, the population mean is H0 and the percentage is 75.
    - And H1/HA is the population mean 
        - H0 --> when μ0  is equal to  75 percent
        - H1 -->  when μ0 is not equal to 75 percent
- The formula of Z-test :
    https://images.app.goo.gl/aYh2EvgsmdXxXtyNA
- Here x̅ is the sample mean, ‘μ’ is hypothesized mean, ‘s’ is the standard error, and ‘n’ is the sample size.
- So if the sample mean is close enough to hypothesized mean, then Z will be close to 0.
- In this case, we will accept the Null Hypothesis (As demonstrated in the image below). Otherwise, we will reject it.

## P-value

- It is is the level of marginal significance representing a given event's probability of occurrence.
- P-Value tables or spreadsheet/statistical software can be used to calculate the p-value.
- The smaller p-value indicates stronger evidence favoring the alternative hypothesis.
- A p-value is a number between 0 and1:
- A  p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis; the null hypothesis is rejected.
- A p-value (> 0.05) indicates weak evidence against the null hypothesis; the null hypothesis is not rejected.
- p-values very close to the cut-off (0.05). 

    ### P-Values for t-Tests
    - Just as the P-value for a z test is a z curve area, the P-value for a t-test will be a t-curve area. 

## T-Stats

- A t-test is a statistical method used to see if two sets of data are significantly different. 
- T-tests are used to involve data analysis that has applications in business, science, and many other disciplines.

## T-stats vs Z-stats

- Z-tests
    - With the help of z-score, we can come to know how far the data point is from the mean in the standard deviation.
    - A z-test compares a sample to a defined population and is typically used for dealing with problems relating to larger samples (n > 30).
    - Z-score can also be used to test the hypothesis, and if the standard deviation is known, then it is beneficial.

- T-tests
    - Similar to the z-tests, t-tests are also used to test a hypothesis, but it is most useful when there is a need to know the significant difference between 2 independent sample groups.
    - In other words, the t-test asks whether the difference between the means of two groups is unlikely to have occurred because of the random chance. Usually, t-tests are the most appropriate when dealing with problems with a limited sample size (n < 30).

### When to use a t-tests vs. z-tests

- the t-test can be used when your sample:
    - Has a sample size below 30,
    - Has an unknown population standard deviation.

Note: A z-test tells you how many standard deviations away from the mean your result is. You can use the z-table to determine what percentage of the population will fall below or above your result.

## Type 1 and Type 2 Error

There are two possible errors: 

- A Type 1 Error:
    - A Type 1 error occurs when we reject a true null hypothesis. That is, a Type 1 error occurs when the jury convicts an innocent person.
    - In False Positive Error, the null hypothesis is true. A type 1 error occurs but is rejected.

- A Type 2 Error:
    - When the null hypothesis is not rejected, then a Type 2 error occurs. 
    - A type II error, or false negative, is where a test result indicates that a condition failed, while it was successful.

## Bayes Statistics (Bayes Theorem)

- Bayes Statistics is used for calculating conditional probabilities.

- P( Ak | B ) =  	P( Ak ∩ B )
                ________________________________________
                [ P( A1 ∩ B ) + P( A2 ∩ B ) + . . . + P( An ∩ B ) ]

- P( Ak ∩ B ) P( Ak ∩ B ) = P( Ak ) P( B | Ak ) 
	
- #### When to Apply Bayes' Theorem:
    - When the sample space is divided(partitioned) into a set of events { A1, A2,…. Ana}.
    - An event B is present, for which P(B) > 0 exists within the sample space.
    - P( Ak | B ) is the form to compute a conditional probability. 

- #### One of the two sets of probabilities mentioned:
    - For each Ak, Probability, P( Ak ∩ B ).
    - For each Ak, Probability, P( Ak ) and P( B | Ak ) 

## Confidence Interval

- It is the range within which we expect the population parameter to be.
- A confidence interval around the sample statistic is computed in such a way that it has a specific chance of containing the value of the corresponding population parameter.
- It also indicates that the range that’s likely to contain the true population parameter, so the CI focuses on the population.
- They are often used with a margin of error.
- It is denoted by 1 – α, here α is a value between 0 and 1 and is called the Confidence Level of Interval.

- The CI is equal to 1, which is the alpha level. And if 0.05 is the level of significance, then 95% is the corresponding CI.
    - If the significance (alpha) level is higher than the P-value, then we can say that the hypothesis test can be significantly correct.
    - If the null hypothesis value is not found in the confidence interval, then the results are statistically significant.
    - If alpha is higher than the P-value, then the hypothesis value will not be found in the confidence interval.

- For our example, the P-value (0.031) is less than the significance level (0.05), which indicates that our results are statistically significant. Similarly, our 95% confidence interval [267 394] does not include the null hypothesis mean of 260, and we draw the same conclusion.

- Interpreting confidence levels and confidence intervals
    - When we create a confidence interval, it's essential to be able to understand the meaning of the confidence level we used and the interval obtained.
    - The confidence level refers to the long-term success rate of the method, that is, how often this type of interval will capture the parameter of interest.
    - A specific confidence interval gives a range of plausible values for the parameter of interest.
    - Let's look at a few examples that demonstrate how to interpret confidence levels and confidence intervals.

## Chi-Sqaure test

- In probability and statistics, the chi-squared distribution (also chi-square or X2-distribution) with the degrees of freedom ‘k’ is the distribution of a sum of the squares of k independent standard normal random variables.
    - The x^2(chi-square) distribution is a continuous probability distribution that is widely used in statistical inference.
    - The x^2(chi-square) distribution is related to the standard normal distribution:
        - If a random variable Z has the standard normal distribution, then Z^2 has the x^2(chi-square) distribution with one degree of freedom.

- Chi-Square for Goodness of Fit Test
    - Chi-Square test for testing goodness of fit is used to decide whether there is any difference between the experimental value & the expected (theoretical) value.
    - A chi-squared test, also written as x2 test, is any statistical hypothesis test where the sampling distribution of the test statistics is chi-squared distribution when the null hypothesis becomes true. 

## Analysis of variance (ANOVA)

- It is a parametric statistical technique that is used to compare datasets.
- R.A. Fisher is the person who invented this technique. It is also referred to as Fisher’s NOVA.

- #### Assumptions to use ANOVA
    - The independence of a case assumption means that the sample should be selected randomly. There should be no pattern in the selection of the sample.
    - Normality: Distribution of each group should be normal. Kolmogorov-Smirnov or the Shapiro-Wilk test may be used to confirm the normality of the group.
    - Homogeneity means between the group; the variance must be the same. To test the correlation between groups, Levene’s test is used.

- #### ANOVA has 3 types:
    - If we start to compare more than three groups based on a single factor, then it is known as a one-way analysis of variance. 
    - For example, if the mean output of 3 workers is compared whether they are the same based on the working hours of the three workers.
    - Two-way analysis: When factor variables are more than two, then it is said to be the two-way analysis of variance (ANOVA). For example, based on working conditions and working hours, we can compare whether or not the mean output of the three workers is the same.
    - K-way analysis: When factor variables are k, then it is said to be the k-way analysis of variance (ANOVA).

## F Distribution

- #### F-Test (variance ratio test)
    - When we run a regression analysis, we get f value to find out the means between two populations. 
    - It's similar to a T statistic from a T-Test. A T-test will tell you if a single variable is related statistically, and an F test will tell you if a group of variables is jointly significant.
        - F-test is used to test the two independent estimations of population variances(S1^2 & S2^2).
        - F-test is used by comparing the ratio of the two variances S1^2 & S2^2.
        - The samples must be independent.
        - F-test is a small sample test.
            - F = (Larger estimate of population variance) / (Smaller estimate Of population variance)
        - The variance ratio = S1^2 & S2^2
        - F-test never is -ve because the upper value is greater than lower.
        - Degree of freedom for larger population variance is V1 and smaller V2
        - The null hypothesis of two population variance are equal, i.e.,
            - HO: S1^2 = S2^2

- Note:
    - The Student ‘t’ distribution is robust, which means that if the population is non-normal, the results of the t-test and confidence interval estimate are still valid provided that the population is not extremely non-normal.
    - To check this requirement, draw a histogram of the data and see how bell-shaped the resulting figure is. 
    - If a histogram is extremely skewed (say in that case of an exponential distribution), that could be considered “extremely non-normal,” and hence, t-statistics would not be valid in this case.

## Credits

- Ineuron
- [Ahmed Wael](https://www.udemy.com/user/ahmedwael2/) and [Juan E. Galvan](https://www.udemy.com/user/juangalvan3/)








