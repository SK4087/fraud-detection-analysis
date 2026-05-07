import pandas as pd
df = pd.read_csv("credit_card_fraud_dataset.csv")
#print(df.head())

#df.info()
#df.describe()

#Convert from object to Datatime for TransactionDate
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
print(df.head())

df['hour'] = df['TransactionDate'].dt.hour #Extract TransactionDate from the timestamp

#Creating Time Features
df['hour'] = df['TransactionDate'].dt.hour
df['weekday'] = df['TransactionDate'].dt.day_name()


print(df['IsFraud'].value_counts(normalize=True)) #Returns 0 for a valid transaction and 1 for an invalid transaction
print(df.groupby('IsFraud')['Amount'].mean()) #Check if there is a discrepancy between the amounts of legitimate and fraudulent transactions

#Check if the time or day of the week is a factor
print(df.groupby('hour')['IsFraud'].mean())
print(df.groupby('weekday')['IsFraud'].mean())

#Location
print(df.groupby('Location')['IsFraud'].mean().sort_values(ascending=False))

#Analyzing time and location together
combo = df.groupby(['hour','Location'])['IsFraud'].mean()
print(combo.sort_values(ascending=False).head(10))
print(df.groupby(['hour','TransactionType'])['IsFraud'].mean())

#Analyze time differences between consecutive transactions at the same merchant
df = df.sort_values(['MerchantID','TransactionDate'])
df['time_diff'] = df.groupby('MerchantID')['TransactionDate'].diff().dt.seconds
df['rapid_txn'] = df['time_diff'] < 60  
print(df.groupby('rapid_txn')['IsFraud'].mean())

#Risk score
df['risk_score'] = (
    df['hour'].isin([18,1,8]).astype(int) * 2 +
    df['Location'].isin(['New York','Houston']).astype(int) * 1 
)
print(df.groupby('risk_score')['IsFraud'].mean())

print(df['rapid_txn'].value_counts())

df.to_csv("cleaned_fraud_data.csv", index=False)

