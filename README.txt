ANALYSIS-OF-RESEARCH-TRENDS-IN-COMPUTER-SCIENCE

################################
Analysis of DBLP:
The code for this is located in analysis.dblp file in analysis_of_dblp folder. 
We first calculate the frequency of words in the titles of the publications. 
Then, we create a wordcloud for the top 100 most frequent words. 
WordClouds are the visual representations of words that give more prominence to the words that appear frequently. 
We also calculate the count of number of publications by authors and create wordcloud for 
the top 100 authors with the greatest number of publications. 
We also use bar plots to visualise the year wise frequency distribution of 
words that occur in the titles of the publications. We create a file named 
“words_years.csv” and save the year wise distribution of words in it. 
We also use bar plots to visualise the year wise publication count distribution 
of authors. We create a file named “authors_years.csv” and save the year wise publication count of authors in it. 
We consider the years 1970 to 2021. 

We create a file named “words_years.csv” and save the year wise distribution of words in it with 
columns word,1970,1971……..2021 as shown above. 


#################################
Association Rules:
The code to obtain the association rules is in association_rules folder and 
there execute the fpgrowth.ipynb file. Then, the output file that is generated will be 
 1) association_rules.csv


Association rules are "if-then" statements. They help us to show the probability of relationships between data items. They are useful in 
fining correlations and co-occurrences between data sets and also can be used to find the patterns in data. Association rule has two parts. 
They are antecedent(if) and consequent(then). 
There are few important terms we need to understand while performing Association Mining. They are support, confidence.  
Support
Support indicates the frequency of occurrence of an item in the dataset divided by the total transactions. We use the parameter min support 
in Association Mining. We consider the items who have a frequency greater than or equal to the min support. For example, if the rule is X=>Y, 
then the Support = Frequency(X,Y)/N where N is total number of transactions.
Confidence
Confidence indicates the conditional probability of the consequent given the antecedent. 
For example, if  the rule is X=>Y, then the Confidence = Frequency(X,Y)/Frequency(X)
We have used FP-Growth algorithm in order to generate the Association Rules. 
FP-Growth
FP-Growth is a popular algorithm used for the mining of association rules. It is very fast when compared to Apriori Algorithm. FP-Growth 
algorithm organizes the data into a tree like structure in order for faster scanning. 
We consider each publication title as a transaction. The words in the title are considered as the items. 
The steps under this FP-Growth algorithm are:
1) We count the frequencies of individual items.  
2) We assign a minimum support. We calculated it in the project as the min support = 100/(total transactions). 
Every item with fewer occurrences than the min support will be excluded. 
3) We order the non-excluded words in each transaction in descending order of their frequencies. 
These are called ordered item sets. 
4) We have a root node in the tree which is NULL. We create the tree by inserting all the ordered item sets. 
5) After construction of the tree, the Conditional Pattern Base which is the path of the nodes 
which leads to any particular node. 
6) We find the Conditional Frequent Pattern tree for each item. We do it by considering 
the set of common elements in the paths in Conditional Pattern Base and we calculate support 
count and take the ones with at least min support. 
7) We now generate the frequent pattern rules by pairing items of conditional frequent 
pattern tree with its corresponding item. 
8) We will assign a min confidence parameter. We set min confidence as 0.55 in the project. 
We now generate strong association rules from the frequent patterns. For example, 
if Y is a frequent pattern set, then we generate all possible non empty subsets from Y and for each subset X, 
we calculate the confidence as confidence=support(Y-X)/support(X) for the rule X=>(Y-X). We consider only 
the rules with confidence >= min confidence. 
The association rules will be generated as an output in “association_rules.csv” file. 
There will be 3 columns antecedent, consequent and confidence. More than 2000 association rules 
were generated with min support of 100/(total transactions) and min confidence of 0.7. 

###################################################

Co_Author Prediction:
 The code to predict the co-authors is located in co_author_prediction folder and 
 there execute the Co-Author Prediction.ipynb file. Then, the output files that will be generated will be
 1) jacard_predictions.csv
 2) aac_predictions.csv

We first find out the authors who have worked together in their publications from the dblp data. 
Then, we make a graph or network of the authors that have worked together using an adjacency list. 
After the construction of the adjacency list, we will then use certain link prediction techniques in order to 
predict the possibility of co-authors working together in the future for any particular author who have not worked together in the past. 
We have used 2 link prediction techniques. They are:
1) Jaccard Coefficient
2) Adamic Adar Coefficient
For predicting, we consider any particular author as input and for that author, 
the neighbours of the neighbouring authors to the input author will be considered as the possible future co-authors. 
Then, the Jaccard index and Adamic/Adar Index will be calculated. Then, we output at most 5 possible authors with the highest Jaccard Index and Adamic/Adar Index separately. 
We have done this for 10000 randomly selected authors. We will then save the results in two csv files named “jaccard_predictions.csv” and “aac_predictions.csv”. 

In "jaccard_predictions.csv",First column is the input author for whom we have to predict the co-author. 
The second column is the predicted co-author. The third column is the jaccard Coefficient. 
In “aac_predictions.csv”, First column is the input author for whom we have to predict the co-author. 
The second column is the predicted co-author. The third column is the adamic/adar Coefficient. 

####################################################

Correlation:
 The code to find the correlations is in correlation folder and 
there, execute the correlation.ipynb file. Then, the output files that will be generated will be 
 1) Authors Correlation Matrix.png
 2) authors_correlation.csv
 3) title_words_correlation.csv
 4) Title Words COrrelation Matrix.png
We first calculate the frequencies of title words. We will then consider the top 100 frequent words for finding the correlation between them. 
ϕ correlation coefficient is used for the measure of association between binary variables. 
Let us consider two words X and Y. Here, “Has word X” and “No word X” is a dichotomous variable. 
“Has word Y” and “No word Y” is also dichotomous variable. 
We calculate these coefficients between all possible pairs of the top 100 frequent words. 
After calculating this coefficient, we then save these results in “title_words_correlation.csv” file. 
For the purpose of plotting the correlation matrix, we set the diagonal elements of the matrix to zero 
for better visualization of the correlation matrix. We use seaborn library to plot the heatmap of the correlation matrix. 
We repeat the above process for the authors too. 
We generate heatmaps for both title words and authors. 
We save the correlations in “title_words_correlation.csv” file with three columns namely word1, word2, correlation. 
We also save the correlations in “authors_correlation.csv” file with three columns namely author1, author2, correlation. 
###############################################

YEAR WISE DISTRIBUTION OF PUBLICATIONS/CONFERENCES:

The code for this is located in year_wise.ipynb file.
We first read the dblpv13.json file.
Iteratively, this file is read line by line.
We then parse the literals in lines which contains year as keyword.
We maintain a dictionary to include these years into it along with count.
When we encounter more and more occurances of year we iterate the count associated to that key.
Since, every year in any line corresponds to exactly one publication, we take advantage of this fact and add 1 to 
our count whenever we encounter one occurance of an year.
After completing reading the entire file, we now have data for all the years.
Now, we plot the year wise publications count values 



##########################################
Analysis of phd thesis data:
Code  is located in thesis-analysis/dblp_pg.ipyb  
Analysis is performed on phd thesis data present in dblp.xml file https://dblp.uni-trier.de/xml/ 
tf-idf is used for vectorization of thesis titles
K-means clustering is done on thesis titles to get related thesis titles. 
Optimal number of clusters is selected by elbow method
World cloud is for frequently occurig words is generated and is printed in dblp_pg.ipyb file 
Barplot is created in dblp_pg.ipyb file to show top 15 universities which have phd thesis data available in dblp.xml
cluster0.csv, cluster1.csv, cluster2.csv,cluster3.csv, cluster4.csv contains phd thesis titles belonging to that cluster

Software packages used:
matplotlib
TfidfVectorizer (sklearn)
Polyglot
KMeans
###############################################

###############################################
Topic modelling of publication data
Code is present in dm_proj_trends.ipynb
Analysis is performed on Citation Network Dataset https://www.aminer.org/citation
Data (title+keywords+field of study+abstract) is extracted for all the research publications
Data is preprocessed using tokenization,stemming,vectorization(tf-idf).
LDA(Latent Dirichlet allocation) is performed on the data for topic modelling
Topics,Topic clusters,Frequently occuring words are  obtained as result.
Topic modelling is done for research data from 1961-1981 and 1981-2021

Software packages used:
gensim
nltk
pyLDAvis
###################################################



