#load_data.py
# import pandas as pd
# df = pd.read_csv(r"C:\Users\Keert\PycharmProjects\PythonProject\PS_20174392719_1491204439457_log.csv") #loading the fraud data set
#
# print("Dataset shape:", df.shape) #printing data set
# print("\nfirst 5 rows:") #next line printing first 5 rows
# print(df.head()) #printing field names
# print("\nFraud distribution:") #next line "Fraud distribution"
# print(df['isFraud'].value_counts(normalize=True)) #value counts normalize means true
#
# #save basic info
# df.info()
# df.describe()

#finding fraud patterns
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"/PS_20174392719_1491204439457_log.csv")
print("=== Fraud Patterns For Banking OPS ===")

#fraud by transaction type
print("\nFraud rate by Type:")
fraud_by_type = df.groupby('type')['isFraud'].mean().sort_values(ascending=False)
print(fraud_by_type)

#amount analysis
print("\nFraud vs Normal amounts:")
print("\nNormal median:", df[df.isFraud==0]['amount'].median())
print("Fraud median:", df[df.isFraud==1]['amount'].median())

#visuals to identify issues
plt.figure(figsize=(15,20))

plt.subplot(2,3,1)
sns.boxplot(data=df, x='isFraud', y='amount')
plt.title("Amount: Fraud vs Normal")

plt.subplot(2,3,2)
sns.boxplot(data=df, x='type', hue='isFraud')
plt.title("Fraud by payment type")
plt.xticks(rotation=45)

plt.subplot(2,3,3)
sns.histplot(data=df[df.isFraud==1], x='amount', bins=50, alpha=0.7, color='red')
plt.title("Fraud Transaction Amounts")

plt.subplot(2,3,4)
df.groupby('step')['isFraud'].mean().plot()
plt.title("Fraud Rate Over Time (steps)")

plt.subplot(2,3,5)
sns.boxplot(data=df, x='type', y='amount', hue='isFraud')
plt.title("Amount by type + Fraud")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("fraud_eda.png", dpi=300, bbox_inches='tight')
plt.show()

print("\nPlots saves as 'fraud_eda.png'")
print("Key insights ready for your portfolio")


