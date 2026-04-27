import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('medicalAppointment.csv')

df = data[['Age', 'ScheduledDay', 'AppointmentDay']].copy()

print(df.head())
print(type(df['ScheduledDay']))

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['Duration'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days

print(df.head())

plt.scatter(df['Age'], df['Duration'])
plt.xlabel('Age')
plt.ylabel('Duration')
plt.show()

