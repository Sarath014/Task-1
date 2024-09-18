import matplotlib.pyplot as plt
import pandas as pd

data = {'Age': [25, 30, 35, 20, 22, 40, 38, 45, 28, 32, 42, 48],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']}


df = pd.DataFrame(data)


plt.figure(figsize=(8, 5))  


gender_counts = df['Gender'].value_counts()


gender_counts.plot(kind='bar')

plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')


plt.show()


plt.figure(figsize=(8, 6))  

plt.hist(df['Age'], bins=10, edgecolor='black')


plt.title('Age Distribution')


plt.xlabel('Age')
plt.ylabel('Frequency')


plt.show()