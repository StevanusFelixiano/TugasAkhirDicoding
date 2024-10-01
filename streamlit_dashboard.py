import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    customers = pd.read_csv('C:/Bangkit/Submission/Data/customers_dataset.csv')
    orders = pd.read_csv('C:/Bangkit/Submission/Data/orders_dataset.csv')
    order_items = pd.read_csv('C:/Bangkit/Submission/Data/order_items_dataset.csv')
    order_payments = pd.read_csv('C:/Bangkit/Submission/Data/order_payments_dataset.csv')
    products = pd.read_csv('C:/Bangkit/Submission/Data/products_dataset.csv')
    return customers, orders, order_items, order_payments, products

customers, orders, order_items, order_payments, products = load_data()

st.title("E-Commerce Data Analysis Dashboard")
st.write("This dashboard presents an analysis of E-Commerce data, including customers, orders, products, and payments.")

st.sidebar.header("User Input Features")
category = st.sidebar.selectbox("Select a Product Category", products['product_category_name'].unique())
min_spending = st.sidebar.slider("Minimum Total Spending", 0, int(order_items['price'].max()), 0)

merged_data = pd.merge(order_items, products, on='product_id')
merged_data = pd.merge(merged_data, orders, on='order_id')
merged_data = pd.merge(merged_data, order_payments, on='order_id')
merged_data = pd.merge(merged_data, customers, on='customer_id')

filtered_data = merged_data[(merged_data['product_category_name'] == category) & (merged_data['price'] >= min_spending)]

st.subheader("Distribution of Orders per Customer")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['order_id'].value_counts(), bins=30)
st.pyplot()

st.subheader("Total Spending per Customer")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data.groupby('customer_unique_id')['price'].sum(), bins=30, color="orange")
st.pyplot()

st.subheader("Top Product Categories by Revenue")
category_revenue = merged_data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)
st.bar_chart(category_revenue)

st.subheader("Correlation Analysis")
correlation_matrix = merged_data[['price', 'freight_value', 'payment_value']].corr()
st.write(sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm"))
st.pyplot()

st.write("This dashboard helps explore E-Commerce performance based on customer behavior and product sales.")
