# Fraud Detection Analysis
1. Overview

   This project aims to identify key drivers of fraudulent transactions using transaction data.

2. Objective
   
   To identify when and where fraudulent transactions are most likely to occur and support decision-making for fraud analysts and security teams.

3. Dataset Overview
   
   The dataset used in this project was sourced from Kaggle and contains 100,000 credit card transactions.

   It includes key information such as:
   - IsFraud (0 = non-fraud, 1 = fraud)
   - TransactionDate
   - Amount
   - Location
   - TransactionType

4. Analysis
- Create features 
- Fraud rate by amount 
- Fraud rate by hour, and weekdays 
- Fraud rate by location
- Transaction patterns

5. Key Findings
   
   5.1 Fraud rates vary by time of day  
   Fraud rates vary by time of day.  
   The highest rate occurs around 18:00 (approximately 1.3%), while the lowest occurs around 17:00 (approximately 0.7%).  This indicates that fraud risk can be nearly twice as high during peak hours.
   
   5.2 Certain locations show elevated risk  
   Fraud rates differ across locations.  
   Higher risk is observed in New York and Houston, while lower rates are seen in San Jose and Philadelphia.  This suggests geographic variation in fraud risk.
   
   5.3 Combining time and location reveals high-risk segments  
   Transactions that occur during high-risk hours and in high-risk locations show a higher likelihood of fraud.
   
   5.4 Transaction type shows minor variation  
   Fraud rates do not differ significantly across transaction types.
   
   5.5 Transaction amount is not a strong indicator  
   The average transaction amount is similar between fraudulent and non-fraudulent transactions, suggesting that amount alone is not a reliable indicator.
   
   5.6 Multi-factor risk scoring improves detection  
   A simple risk scoring model was created by combining multiple factors.  
   Transactions during high-risk hours (e.g., 18:00) were assigned a higher score (+2), and transactions from high-risk locations (e.g., New York and Houston) were assigned additional points (+1).  
   The fraud rate increases consistently as the risk score increases, indicating that combining multiple factors improves risk detection.

 
6. Dashboard
The dashboard visualises fraud patterns across time, location, and combined risk factors.
       <img width="655" height="760" alt="Tableau_スクショ" src="https://github.com/user-attachments/assets/79178cc5-3089-4537-a424-1c8705f1c0a5" />


7. Recommendations
These findings suggest the need for more targeted fraud detection strategies:
- Apply additional verification during high-risk hours (e.g., 18:00–19:00). 
- Pay closer attention to transactions from high-risk locations such as New York and Houston. 
- Use multi-factor risk scoring rather than relying solely on transaction amount. 
- Monitor combinations of risk factors, such as time and location, to improve detection accuracy.
8. Conclusion
These results suggest that fraud is driven more by behavioral factors, such as time and location, rather than transaction amount.

9. Tools Used
Python (Pandas)
Tableau (Visualisation)

