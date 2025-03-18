import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Load Tamil Nadu Government logo from GitHub
def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")
        return None

logo_url = "https://github.com/Ration123/RATION/raw/main/title"
logo = load_image_from_url(logo_url)

if logo:
    st.image(logo, width=1000 ,length=300)  # Increased logo size to 200
else:
    st.write("Unable to load Tamil Nadu Government logo.")

# Placeholder data
users = {'user1': {'password': 'pass1', 'shop_number': '101'}}
stock_data = {'Rice': 100, 'Sugar': 50, 'Wheat': 80}

# Authentication function
def authenticate(username, password, shop_number):
    user = users.get(username)
    if user and user['password'] == password and user['shop_number'] == shop_number:
        return True
    return False

# Streamlit UI
st.title('Tamil Nadu Ration Shop Management')

# Login Page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    shop_number = st.text_input('Shop Number')
    
    if st.button('Login'):
        if authenticate(username, password, shop_number):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success('Login successful!')
        else:
            st.error('Invalid credentials')
else:
    # Dashboard
    st.sidebar.title('Dashboard')
    option = st.sidebar.selectbox('Choose an option', ['View Stock', 'Purchase Verification', 'Order & Pay', 'Track Delivery'])

    if option == 'View Stock':
        st.subheader('Stock Details')
        
        items = list(stock_data.keys())
        quantities = list(stock_data.values())
        
        fig, ax = plt.subplots()
        bars = ax.bar(items, quantities, color='skyblue')
        
        # Annotate bars with values
        for bar, qty in zip(bars, quantities):
            ax.annotate(f'{qty}', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        
        ax.set_xlabel('Items')
        ax.set_ylabel('Remaining Stock')
        ax.set_title('Stock Overview')
        st.pyplot(fig)

    elif option == 'Purchase Verification':
        st.subheader('Check Purchase Details')
      

    elif option == 'Order & Pay':
        st.subheader('Order and Payment')
        item = st.selectbox('Select Item', list(stock_data.keys()))
        quantity = st.number_input('Quantity', min_value=1)
        if st.button('Place Order'):
            if quantity <= stock_data[item]:
                stock_data[item] -= quantity
                st.success(f'Order placed for {quantity} {item}(s)')
            else:
                st.error('Insufficient stock')

    elif option == 'Track Delivery':
        st.subheader('Track your Delivery')
        st.write('Feature under development.')

    if st.sidebar.button('Logout'):
        st.session_state.clear()
        st.rerun()
