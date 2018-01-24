# Task
Detect customer genderm using his/her transaction data

## Data files: 
1. `transactions.csv` - Transaction log for all customers (15000 of them)
2. `tr_mcc_codes.csv - MCC codes (vendor catrgories assigned by bank). For reference purposes
3. `tr_types.csv` - Transaction types
4. `customers_gender_train.csv` - Training data (customer gender)

Labeled data for training is in `customers_gender_train.csv`. For all customers who 
are not listed there, gender must be determined using the model built.

The generaizing ability of the model is determined using ROC AUC metric.

# Reporting
The final report must contain
1. Solution description
1. ROC AUC as a fugure and accuracy value on cross-validation subset
1. Description on top 20 variables by feature importance and relevant graph
1. Spearman's rank correlation coefficient between top 20 variables and target variable (gender)
It also can contain any other relevant information about steps performed and facts considered worth mentioning.
