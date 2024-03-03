import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load used data 
all_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/dashboard/all_data.csv")

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
columns1 = df1.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns1), len(columns1), figsize=(16, 16))

for i, x in enumerate(columns1):
    for j, y in enumerate(columns1):
      sns.scatterplot(x=x, y=y, data=df1, ax=ax[i, j])
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)


# Changping

st.subheader("Scatter Plot Between Air Pollutants in Changping")

Changping_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Changping.csv")
df2 = Changping_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns2 = df2.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns2), len(columns2), figsize=(16, 16))

for i, x in enumerate(columns2):
    for j, y in enumerate(columns2):
      sns.scatterplot(x=x, y=y, data=df2, ax=ax[i, j], color='red')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Dingling

st.subheader("Scatter Plot Between Air Pollutants in Dingling")

Dingling_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Dingling.csv")
df3 = Dingling_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns3 = df3.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns3), len(columns3), figsize=(16, 16))

for i, x in enumerate(columns3):
    for j, y in enumerate(columns3):
      sns.scatterplot(x=x, y=y, data=df3, ax=ax[i, j], color='silver')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Dongsi

st.subheader("Scatter Plot Between Air Pollutants in Dongsi")

Dongsi_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Dongsi.csv")
df4 = Dongsi_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns4 = df4.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns4), len(columns4), figsize=(16, 16))

for i, x in enumerate(columns4):
    for j, y in enumerate(columns4):
      sns.scatterplot(x=x, y=y, data=df4, ax=ax[i, j], color='brown')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Guanyuang

st.subheader("Scatter Plot Between Air Pollutants in Guanyuang")

Guanyuang_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Guanyuang.csv")
df5 = Guanyuang_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns5= df5.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns5), len(columns5), figsize=(16, 16))

for i, x in enumerate(columns5):
    for j, y in enumerate(columns5):
      sns.scatterplot(x=x, y=y, data=df5, ax=ax[i, j], color='orange')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Gucheng

st.subheader("Scatter Plot Between Air Pollutants in Gucheng")

Gucheng_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Gucheng.csv")
df6 = Gucheng_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns6= df6.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns6), len(columns6), figsize=(16, 16))

for i, x in enumerate(columns6):
    for j, y in enumerate(columns6):
      sns.scatterplot(x=x, y=y, data=df6, ax=ax[i, j], color='darkgreen')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Huairou

st.subheader("Scatter Plot Between Air Pollutants in Huairou")

Huairou_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Huairou.csv")
df7 = Huairou_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns7= df7.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns7), len(columns7), figsize=(16, 16))

for i, x in enumerate(columns7):
    for j, y in enumerate(columns7):
      sns.scatterplot(x=x, y=y, data=df7, ax=ax[i, j], color='purple')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Nongzhanguan

st.subheader("Scatter Plot Between Air Pollutants in Nongzhanguan")

Nongzhanguan_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Nongzhanguan.csv")
df8 = Nongzhanguan_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns8= df8.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns8), len(columns8), figsize=(16, 16))

for i, x in enumerate(columns8):
    for j, y in enumerate(columns8):
      sns.scatterplot(x=x, y=y, data=df8, ax=ax[i, j], color='deepskyblue')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Shunyi

st.subheader("Scatter Plot Between Air Pollutants in Shunyi")

Shunyi_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Shunyi.csv")
df9 = Shunyi_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns9= df9.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns9), len(columns9), figsize=(16, 16))

for i, x in enumerate(columns9):
    for j, y in enumerate(columns9):
      sns.scatterplot(x=x, y=y, data=df9, ax=ax[i, j], color='maroon')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Tiantan

st.subheader("Scatter Plot Between Air Pollutants in Tiantan")

Tiantan_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Tiantan.csv")
df10 = Tiantan_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns10= df10.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns10), len(columns10), figsize=(16, 16))

for i, x in enumerate(columns10):
    for j, y in enumerate(columns10):
      sns.scatterplot(x=x, y=y, data=df10, ax=ax[i, j], color='gold')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Wanliu

st.subheader("Scatter Plot Between Air Pollutants in Wanliu")

Wanliu_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Wanliu.csv")
df11 = Wanliu_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns11= df11.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns11), len(columns11), figsize=(16, 16))

for i, x in enumerate(columns11):
    for j, y in enumerate(columns11):
      sns.scatterplot(x=x, y=y, data=df11, ax=ax[i, j], color='limegreen')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

# Wanshouxigong

st.subheader("Scatter Plot Between Air Pollutants in Wanshouxigong")

Wanshouxigong_df = pd.read_csv("https://raw.githubusercontent.com/mfayyadhr/Submission/main/data/Wanshouxigong.csv")
df12 = Wanshouxigong_df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
columns12= df12.select_dtypes(include='number').columns
fig, ax = plt.subplots(len(columns12), len(columns12), figsize=(16, 16))

for i, x in enumerate(columns12):
    for j, y in enumerate(columns12):
      sns.scatterplot(x=x, y=y, data=df12, ax=ax[i, j], color='navy')
      ax[i, j].set_xlabel(x)
      ax[i, j].set_ylabel(y)
      ax[i, j].set_title(f'{x} vs {y}', fontsize=11)
plt.tight_layout()
st.pyplot(fig)

st.caption('Copyright © Muhammad Fayyadh Rifqi 2024')
