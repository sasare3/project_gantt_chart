import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Title
st.title("Gantt Chart of Project Activities")

# Data
data = {
    'Activity': ['Working on thermal models',
        'Procurement of equipment and setting up lab',
        'Collection of feedstocks from Surrey docks, lab analysis of feedstock',
        'Second stage of Systematic Lit Review','Commencement of BMP Testing'

    ],
    'Start': ['2025-07-11','2025-08-04', '2025-08-12', '2025-08-01','2025-09-25'],
    'Finish': ['2025-10-30','2025-08-30', '2025-08-30', '2025-09-30','2025-12-01']
}

# DataFrame
df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])
df['Duration'] = (df['Finish'] - df['Start']).dt.days

# Gantt Chart using Matplotlib
fig, ax = plt.subplots(figsize=(20, 10))
y_positions = range(len(df), 0, -1)

colors = ['#F4A300', '#F45C00', '#F43E5C','#28a745','#007bff']

for idx, (activity, start, duration) in enumerate(zip(df['Activity'], df['Start'], df['Duration'])):
    ax.barh(y_positions[idx], duration, left=start, height=0.5, color=colors[idx])

# Formatting
ax.set_yticks(list(y_positions))
ax.set_yticklabels(df['Activity'])
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xticks(rotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Activity')
ax.set_title('Gantt Chart of Project Activities')

st.pyplot(fig)
