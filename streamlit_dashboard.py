import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    customers = pd.read_csv('Data/customers_dataset.csv')
    orders = pd.read_csv('Data/orders_dataset.csv')
    order_items = pd.read_csv('Data/order_items_dataset.csv')
    order_payments = pd.read_csv('Data/order_payments_dataset.csv')
    products = pd.read_csv('Data/products_dataset.csv')
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
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data['order_id'].value_counts(), bins=30, ax=ax1)
st.pyplot(fig1)

st.subheader("Total Spending per Customer")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data.groupby('customer_unique_id')['price'].sum(), bins=30, color="orange", ax=ax2)
st.pyplot(fig2)

st.subheader("Top Product Categories by Revenue")
category_revenue = merged_data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)
st.bar_chart(category_revenue)

st.subheader("Correlation Analysis")
fig3, ax3 = plt.subplots(figsize=(10, 6))
correlation_matrix = merged_data[['price', 'freight_value', 'payment_value']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

st.write("This dashboard helps explore E-Commerce performance based on customer behavior and product sales.")
