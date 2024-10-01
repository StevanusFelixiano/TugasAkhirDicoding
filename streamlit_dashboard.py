import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv('dataset.csv')  
    return data

data = load_data()

st.title("Data Analysis Dashboard")
st.write("This dashboard presents an analysis of sales data including distributions and product category performance.")

st.sidebar.header("User Input Features")
category = st.sidebar.selectbox("Select a Product Category", data['product_category'].unique())
spending_filter = st.sidebar.slider("Minimum Total Spending", 0, int(data['total_spending'].max()), 0)

filtered_data = data[(data['product_category'] == category) & (data['total_spending'] >= spending_filter)]

st.subheader("Distribution of Orders per Customer")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['order_count'], bins=30)
st.pyplot()

st.subheader("Total Spending per Customer")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['total_spending'], bins=30, color="orange")
st.pyplot()

st.subheader("Top Product Categories by Revenue")
category_revenue = data.groupby('product_category')['total_spending'].sum().sort_values(ascending=False)
st.bar_chart(category_revenue)

st.subheader("Correlation Analysis")
correlation_matrix = data.corr()
st.write(sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm"))
st.pyplot()

st.write("This dashboard is designed to explore sales performance based on customer spending and product category performance.")
