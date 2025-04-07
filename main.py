import streamlit as st
import pandas as pd
import plotly.express as px

# Set custom background and title
def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://raw.githubusercontent.com/Ration123/RATION/main/ration.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        .main > div {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            border-radius: 10px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

def show_title_image():
    st.image("https://raw.githubusercontent.com/Ration123/RATION/main/title", use_column_width=True)

set_background()

# Sidebar
st.sidebar.title("🛒 தமிழ்நாடு ரேஷன் கடை")
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
menu = st.sidebar.radio("📂 Menu", [
    "🏠 Home", "📄 Ration Card Services", "📊 Stock Availability", "📍 Shop Locator",
    "🔐 Login / Signup", "📬 Grievance", "🌐 Language"
])

# Translation dict
def t(text):
    return {
        "Home": "முகப்பு",
        "Ration Card Services": "ரேஷன் கார்ட் சேவைகள்",
        "Stock Availability": "பொருள் நிலை",
        "Shop Locator": "கடை தேடல்",
        "Login / Signup": "உள்நுழைவு / பதிவு",
        "Grievance": "புகார்",
        "Language": "மொழி மாற்று",
        "Submit": "சமர்ப்பிக்கவும்"
    }.get(text, text) if lang_toggle else text

# Home Page
if menu == "🏠 Home":
    show_title_image()
    st.title(t("Welcome to Tamil Nadu Ration Shop Portal"))
    st.write(t("""
        This portal allows citizens to:
        - Apply/modify ration cards
        - Track shop stock
        - Submit complaints
        - Place orders & track status
    """))
    st.success(t("Smart Ration Card updates from May 1st."))
    st.info(t("Biometric verification required from June."))

# Ration Card Services
elif menu == "📄 Ration Card Services":
    show_title_image()
    st.header(t("Ration Card Services"))
    option = st.selectbox(t("Choose Service"), [
        t("Apply for Ration Card"), t("Modify Existing Card"), t("Check Application Status")
    ])
    if option == t("Apply for Ration Card"):
        st.text_input(t("Full Name"))
        st.text_area(t("Address"))
        st.text_input("Aadhaar")
        st.number_input(t("Family Members"), 1, 20)
        if st.button(t("Submit")):
            st.success(t("Application submitted successfully."))
    elif option == t("Modify Existing Card"):
        st.text_input(t("Ration Card Number"))
        st.selectbox(t("Change"), [t("Add Member"), t("Remove Member"), t("Change Address")])
        st.text_area(t("Details"))
        if st.button(t("Submit")):
            st.success(t("Modification sent."))
    elif option == t("Check Application Status"):
        st.text_input(t("Application Number"))
        if st.button(t("Check Status")):
            st.info(t("Your application is under review."))

# Stock Availability with bar graph
elif menu == "📊 Stock Availability":
    show_title_image()
    st.header(t("Real-Time Stock"))
    shop = st.selectbox(t("Select Shop"), ["Shop 101 - Chennai", "Shop 102 - Madurai", "Shop 103 - Coimbatore"])
    data = {
        "Shop 101 - Chennai": {"Rice": 100, "Sugar": 40, "Wheat": 0},
        "Shop 102 - Madurai": {"Rice": 80, "Sugar": 75, "Wheat": 60},
        "Shop 103 - Coimbatore": {"Rice": 30, "Sugar": 60, "Wheat": 90},
    }
    df = pd.DataFrame(data[shop].items(), columns=["Item", "Quantity"])
    fig = px.bar(df, x="Item", y="Quantity", color="Item", title=t("Current Stock Levels"))
    st.plotly_chart(fig)

# Ration Shop Locator with gmap
elif menu == "📍 Shop Locator":
    show_title_image()
    st.header(t("Ration Shop Locator"))
    st.map(pd.DataFrame({
        'lat': [13.0827, 9.9252, 11.0168],
        'lon': [80.2707, 78.1198, 76.9558],
        'shop': ['Chennai', 'Madurai', 'Coimbatore']
    }))
    st.markdown("📞 Chennai: 044-12345678  |  Madurai: 0452-2345678  |  Coimbatore: 0422-3456789")

# Login Page (User/Admin)
elif menu == "🔐 Login / Signup":
    show_title_image()
    st.header(t("Login Portal"))
    role = st.radio(t("Login as:"), [t("User"), t("Admin")])
    username = st.text_input(t("Username"))
    password = st.text_input(t("Password"), type="password")
    if st.button(t("Login")):
        st.success(t(f"Welcome {username}!"))
        if role == t("User"):
            st.subheader(t("Card Type: APL"))
            st.write(t("🧾 Order Status: Received this month ✔️"))
            st.write(t("💸 Pay via GPay: UPI@gov"))
            st.button(t("Place Order"))
        elif role == t("Admin"):
            st.subheader(t("Shop Purchase Log"))
            st.write("🧍‍♂️ Ramesh - Shop 101 - Rice - April 5")
            st.write("🧍‍♀️ Sita - Shop 102 - Wheat - April 6")

    st.markdown("---")
    st.subheader(t("New User Signup"))
    st.text_input(t("New Username"))
    st.text_input(t("New Password"), type="password")
    if st.button(t("Signup")):
        st.success(t("Account created."))

# Feedback Section
elif menu == "📬 Grievance":
    show_title_image()
    st.header(t("Submit Complaint or Feedback"))
    st.text_input(t("Full Name"))
    st.text_input(t("Contact Email / Phone"))
    st.text_area(t("Your Message"))
    if st.button(t("Submit")):
        st.success(t("Thank you! We received your feedback."))

# Language Switcher
elif menu == "🌐 Language":
    show_title_image()
    st.header("🌐 Language Switcher")
    st.write("Use the checkbox in the sidebar to toggle between Tamil and English.")
