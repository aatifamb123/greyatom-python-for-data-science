# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include="number")
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(columns = "Loan_ID",axis=0)
# print(banks.isnull().sum())
bank_mode = banks.mode()
banks.fillna(value = bank_mode.to_dict("record")[0] ,inplace=True)
# print(bank_mode.to_dict("record"))
# banks = banks.apply(lambda x:x.fillna(bank_mode[x]))
# banks = banks.replace(bank_mode)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here




avg_loan_amount = banks.pivot_table(index=["Gender","Married","Self_Employed"] , values="LoanAmount",aggfunc="mean") 
print(avg_loan_amount)
# avg_loan_amount_new = banks.groupby(["Gender","Married","Self_Employed"])[["LoanAmount"]].mean()
# print(avg_loan_amount_new)
# code ends here



# --------------
# code starts here
# print(banks["Self_Employed"].head())
# print(banks["Loan_Status"]=="Y")
# print(banks["Self_Employed"]=="Yes")
# print(banks[banks["Self_Employed"]=="Yes" & banks["Loan_Status"]=="Y"].head())
loan_approved_se = len(banks[(banks["Self_Employed"]=="Yes").values & (banks["Loan_Status"]=="Y").values])
loan_approved_nse = len(banks[(banks["Self_Employed"]=="No").values & (banks["Loan_Status"]=="Y").values])

percentage_se = loan_approved_se/614*100
percentage_nse = loan_approved_nse/614*100

# code ends here


# --------------
# code starts here
loan_term = banks["Loan_Amount_Term"].apply(lambda x:x//12)
print(loan_term)
big_loan_term = sum(loan_term>=25)
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby("Loan_Status")
loan_groupby = loan_groupby[["ApplicantIncome","Credit_History"]]
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


