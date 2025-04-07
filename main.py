import streamlit as st

# Inject background image using CSS
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://img.freepik.com/free-photo/sacks-rice-flour-sugar-with-wooden-bowls-rustic-table_1150-20515.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }}
        .main > div {{
            background-color: rgba(0, 0, 0, 0.65);
            padding: 2rem;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Sidebar navigation
st.sidebar.title("Tamil Nadu Ration Shop")
menu = st.sidebar.radio("🔸 Menu", [
    "🏠 Home Page",
    "📄 Ration Card Services",
    "📦 Stock Availability",
    "📍 Ration Shop Locator",
    "🔐 Login / Signup",
    "📝 Grievance / Feedback",
    "🌐 Language Switcher"
])

# 1. Home Page
if menu == "🏠 Home Page":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Tamil_Nadu_Logo.svg/800px-Tamil_Nadu_Logo.svg.png", width=100)
    st.title("Welcome to Tamil Nadu Ration Shop Portal")
    st.write("""
    This portal is developed for Tamil Nadu citizens to:
    - Apply or modify ration cards
    - Track real-time stock in ration shops
    - Locate nearest ration shops
    - Submit grievances and suggestions
    """)
    st.subheader("📢 Latest Announcements")
    st.success("Smart Ration Card updates will be available from May 1st.")
    st.info("Biometric verification will be mandatory from June.")

# 2. Ration Card Services
elif menu == "📄 Ration Card Services":
    st.header("📄 Ration Card Services")
    service = st.selectbox("Choose Service", ["Apply for Ration Card", "Modify Existing Card", "Check Application Status"])

    if service == "Apply for Ration Card":
        st.text_input("Full Name")
        st.text_area("Address")
        st.text_input("Aadhaar Number")
        st.number_input("Number of Family Members", 1, 20)
        if st.button("Submit Application"):
            st.success("Application submitted successfully.")
    elif service == "Modify Existing Card":
        st.text_input("Ration Card Number")
        st.selectbox("Modification", ["Add Member", "Remove Member", "Change Address"])
        st.text_area("Details of Change")
        if st.button("Submit Modification"):
            st.success("Modification request submitted.")
    elif service == "Check Application Status":
        app_id = st.text_input("Enter Application Number")
        if st.button("Check Status"):
            st.info("Your application is under review. Please check back later.")

# 3. Stock Availability
elif menu == "📦 Stock Availability":
    st.header("📦 Real-Time Stock")
    shop = st.selectbox("Select Ration Shop", ["Shop 101 - Chennai", "Shop 102 - Madurai", "Shop 103 - Coimbatore"])
    stock = {
        "Shop 101 - Chennai": {"Rice": "Available", "Sugar": "Low", "Wheat": "Out of Stock"},
        "Shop 102 - Madurai": {"Rice": "Available", "Sugar": "Available", "Wheat": "Available"},
        "Shop 103 - Coimbatore": {"Rice": "Low", "Sugar": "Available", "Wheat": "Available"},
    }
    for item, status in stock[shop].items():
        st.write(f"🛒 **{item}**: {status}")

# 4. Ration Shop Locator
elif menu == "📍 Ration Shop Locator":
    st.header("📍 Locate Your Nearest Ration Shop")
    st.map()  # Show placeholder map
    st.markdown("""
    **Example Locations**
    - Shop 101: 123 MG Road, Chennai | 📞 044-12345678  
    - Shop 102: 45 Anna Nagar, Madurai | 📞 0452-2345678  
    - Shop 103: 78 Gandhipuram, Coimbatore | 📞 0422-3456789  
    """)

# 5. Login / Signup
elif menu == "🔐 Login / Signup":
    st.header("🔐 Login Portal")
    role = st.radio("Login as:", ["Customer", "Staff/Admin"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome {username}!")

    st.markdown("---")
    st.subheader("🆕 New User? Sign up here:")
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Signup"):
        st.success("Account created successfully!")

# 6. Grievance / Feedback
elif menu == "📝 Grievance / Feedback":
    st.header("📝 Submit Your Feedback or Complaint")
    st.text_input("Full Name")
    st.text_input("Email or Contact Number")
    st.text_area("Your Complaint / Feedback")
    if st.button("Submit"):
        st.success("Thanks! Your message has been received.")

# 7. Language Switcher
elif menu == "🌐 Language Switcher":
    st.header("🌐 Switch Language")
    st.markdown("Choose your preferred language:")
    lang = st.radio("Select Language", ["English", "தமிழ் (Tamil)"])
    if lang == "தமிழ் (Tamil)":
        st.success("Interface will be shown in Tamil (to be implemented).")
    else:
        st.info("Currently viewing in English.")
