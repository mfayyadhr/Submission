import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load used data 
all_df = pd.read_csv("all_data.csv")

# plot Worst Air Quality by Air Pollutants
 
st.header('Air Quality Dashboard :dash:')
st.subheader("Worst Air Quality by Air Pollutants")
 
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(15, 12))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x='PM2.5', y='station', data=all_df.sort_values(by="PM2.5", ascending=False), palette=colors, ax=ax[0, 0])
ax[0, 0].set_ylabel(None)
ax[0, 0].set_xlabel(None)
ax[0, 0].set_title("Worst Air Quality by PM2.5", loc="center", fontsize=15)
ax[0, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x='SO2', y='station', data=all_df.sort_values(by="SO2", ascending=False), palette=colors, ax=ax[1, 0])
ax[1, 0].set_ylabel(None)
ax[1, 0].set_xlabel(None)
ax[1, 0].set_title("Worst Air Quality by SO2", loc="center", fontsize=15)
ax[1, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x='CO', y='station', data=all_df.sort_values(by="CO", ascending=False), palette=colors, ax=ax[2, 0])
ax[2, 0].set_ylabel(None)
ax[2, 0].set_xlabel(None)
ax[2, 0].set_title("Worst Air Quality by CO", loc="center", fontsize=15)
ax[2, 0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="PM10", y='station', data=all_df.sort_values(by="PM10", ascending=False), palette=colors, ax=ax[0, 1])
ax[0, 1].set_ylabel(None)
ax[0, 1].set_xlabel(None)
ax[0, 1].invert_xaxis()
ax[0, 1].yaxis.set_label_position("right")
ax[0, 1].yaxis.tick_right()
ax[0, 1].set_title("Worst Air Quality by PM10", loc="center", fontsize=15)
ax[0, 1].tick_params(axis='y', labelsize=12)

sns.barplot(x="NO2", y='station', data=all_df.sort_values(by="NO2", ascending=False), palette=colors, ax=ax[1, 1])
ax[1, 1].set_ylabel(None)
ax[1, 1].set_xlabel(None)
ax[1, 1].invert_xaxis()
ax[1, 1].yaxis.set_label_position("right")
ax[1, 1].yaxis.tick_right()
ax[1, 1].set_title("Worst Air Quality by NO2", loc="center", fontsize=15)
ax[1, 1].tick_params(axis='y', labelsize=12)

sns.barplot(x="O3", y='station', data=all_df.sort_values(by="O3", ascending=False), palette=colors, ax=ax[2, 1])
ax[2, 1].set_ylabel(None)
ax[2, 1].set_xlabel(None)
ax[2, 1].invert_xaxis()
ax[2, 1].yaxis.set_label_position("right")
ax[2, 1].yaxis.tick_right()
ax[2, 1].set_title("Worst Air Quality by O3", loc="center", fontsize=15)
ax[2, 1].tick_params(axis='y', labelsize=12)
 
st.pyplot(fig)

# plot Scatter Plot Between Air Pollutants of all station
# Aotizhongxin
st.subheader("Scatter Plot Between Air Pollutants in Aotizhongxin")

Aotizhongxin_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Aotizhongxin.csv")
df1 = Aotizhongxin_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns = df1.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns), len(columns), figsize=(16, 16))

for i, x in enumerate(columns):
    for j, y in enumerate(columns):
      sns.scatterplot(x=x, y=y, data=df1, ax=ax[i, j])
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

st.subheader("Scatter Plot Between Air Pollutants in Changping")

# 
Changping_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Coba/main/data/Changping.csv")
df2 = Changping_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns = df2.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns), len(columns), figsize=(16, 16))

for i, x in enumerate(columns):
    for j, y in enumerate(columns):
      sns.scatterplot(x=x, y=y, data=df2, ax=ax[i, j])
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

st.caption('Copyright © Muhammad Fayyadh Rifqi 2024')
