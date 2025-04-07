import streamlit as st
import pandas as pd
import plotly.express as px

# === Set Background ===
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

# === Title Image ===
def show_title_image():
    st.image("https://raw.githubusercontent.com/Ration123/RATION/main/title", use_container_width=True)

# === Translation Dictionary ===
def t(text):
    return {
        "Home": "முகப்பு",
        "Welcome to Tamil Nadu Ration Shop Portal": "தமிழ்நாடு ரேஷன் கடை போர்டல் வரவேற்கிறது!",
        "This portal allows citizens to:": "இந்த போர்டல் வழியாக பொதுமக்கள் பின்வரும் சேவைகளை பெறலாம்:",
        "- Apply/modify ration cards": "- ரேஷன் அட்டையை விண்ணப்பிக்க / மாற்றம் செய்ய",
        "- Track shop stock": "- கடை பொருள் இருப்பை பின்தொடர்",
        "- Submit complaints": "- புகார் அளிக்க",
        "- Place orders & track status": "- ஆர்டரை இட & நிலையை பின்தொடர",
        "Smart Ration Card updates from May 1st.": "ஸ்மார்ட் ரேஷன் அட்டை மே 1 முதல் புதுப்பிக்கப்படும்.",
        "Biometric verification required from June.": "ஜூன் மாதம் முதல் பயோமெட்ரிக் சரிபார்ப்பு தேவையாகும்.",
        "Ration Card Services": "ரேஷன் கார்ட் சேவைகள்",
        "Apply for Ration Card": "ரேஷன் கார்டுக்கு விண்ணப்பிக்கவும்",
        "Modify Existing Card": "ஏற்கனவே உள்ள கார்டை மாற்றவும்",
        "Check Application Status": "விண்ணப்ப நிலையை சரிபார்க்கவும்",
        "Full Name": "முழுப் பெயர்",
        "Address": "முகவரி",
        "Family Members": "குடும்ப உறுப்பினர்கள்",
        "Submit": "சமர்ப்பிக்கவும்",
        "Application submitted successfully.": "விண்ணப்பம் வெற்றிகரமாக சமர்ப்பிக்கப்பட்டது.",
        "Ration Card Number": "ரேஷன் கார்டு எண்",
        "Change": "மாற்றம்",
        "Add Member": "உறுப்பினரைச் சேர்க்கவும்",
        "Remove Member": "உறுப்பினரை நீக்கவும்",
        "Change Address": "முகவரியை மாற்றவும்",
        "Modification sent.": "மாற்றம் அனுப்பப்பட்டது.",
        "Application Number": "விண்ணப்ப எண்",
        "Check Status": "நிலையை சரிபார்க்கவும்",
        "Your application is under review.": "உங்கள் விண்ணப்பம் பரிசீலனையில் உள்ளது.",
        "Real-Time Stock": "நிகழ்நேர பொருள் நிலை",
        "Select Shop": "கடையைத் தேர்ந்தெடுக்கவும்",
        "Current Stock Levels": "தற்போதைய இருப்பு நிலை",
        "Ration Shop Locator": "ரேஷன் கடை தேடல்",
        "Login Portal": "உள்நுழைவு போர்டல்",
        "Login as:": "உள்நுழைவு பயனராக:",
        "User": "பயனர்",
        "Admin": "நிர்வாகி",
        "Username": "பயனர் பெயர்",
        "Password": "கடவுச்சொல்",
        "Login": "உள்நுழை",
        "Welcome": "வரவேற்கின்றோம்",
        "Card Type: APL": "அட்டை வகை: APL",
        "🧾 Order Status: Received this month ✔️": "🧾 ஆர்டர் நிலை: இந்த மாதம் பெற்றது ✔️",
        "💸 Pay via GPay: UPI@gov": "💸 GPay வழியாக செலுத்த: UPI@gov",
        "Place Order": "ஆர்டர் இடு",
        "Shop Purchase Log": "கடை வாங்கும் பதிவுகள்",
        "New User Signup": "புதிய பயனர் பதிவு",
        "New Username": "புதிய பயனர் பெயர்",
        "New Password": "புதிய கடவுச்சொல்",
        "Signup": "பதிவு",
        "Account created.": "கணக்கு உருவாக்கப்பட்டது.",
        "Submit Complaint or Feedback": "புகார் அல்லது கருத்தை சமர்ப்பிக்கவும்",
        "Contact Email / Phone": "தொடர்பு மின்னஞ்சல் / தொலைபேசி",
        "Your Message": "உங்கள் செய்தி",
        "Thank you! We received your feedback.": "நன்றி! உங்கள் கருத்தை பெற்றோம்.",
        "Language Switcher": "மொழி மாற்று",
        "Use the checkbox in the sidebar to toggle between Tamil and English.": "தமிழ் மற்றும் ஆங்கிலத்தை மாற்ற பக்கப்பட்டி பெட்டியைப் பயன்படுத்தவும்.",
    }.get(text, text) if lang_toggle else text

# === Initialize ===
st.set_page_config(page_title="Tamil Nadu Ration Shop", layout="wide")
set_background()

# === Sidebar Menu ===
st.sidebar.title("🛒 தமிழ்நாடு ரேஷன் கடை")
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
menu = st.sidebar.radio("📂 Menu", [
    "🏠 Home", "📊 Stock Availability", "📍 Shop Locator",
    "🔐 Login / Signup", "📬 Grievance", "🌐 Language"
])

# === Pages ===
if menu == "🏠 Home":
    show_title_image()
    st.title(t("Welcome to Tamil Nadu Ration Shop Portal"))
    st.write(t("This portal allows citizens to:"))
    st.markdown(t("""
        - Apply/modify ration cards  
        - Track shop stock  
        - Submit complaints  
        - Place orders & track status
    """))
    st.success(t("Smart Ration Card updates from May 1st."))
    st.info(t("Biometric verification required from June."))



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

elif menu == "📍 Shop Locator":
    show_title_image()
    st.header(t("Ration Shop Locator"))
    st.map(pd.DataFrame({
        'lat': [13.0827, 9.9252, 11.0168],
        'lon': [80.2707, 78.1198, 76.9558],
        'shop': ['Chennai', 'Madurai', 'Coimbatore']
    }))
    st.markdown("📞 Chennai: 044-12345678  |  Madurai: 0452-2345678  |  Coimbatore: 0422-3456789")

elif menu == "🔐 Login / Signup":
    show_title_image()
    st.header(t("Login Portal"))
    role = st.radio(t("Login as:"), [t("User"), t("Admin")])
    username = st.text_input(t("Username"))
    password = st.text_input(t("Password"), type="password")
    if st.button(t("Login")):
        st.success(f"{t('Welcome')} {username}!")
        if role == t("User"):
            st.subheader(t("Card Type: APL"))
            st.write(t("🧾 Order Status: Received this month ✔️"))
            st.write(t("💸 Pay via GPay: UPI@gov"))
            st.button(t("Place Order"))
        else:
            st.subheader(t("Shop Purchase Log"))
            st.write("🧍‍♂️ Ramesh - Shop 101 - Rice - April 5")
            st.write("🧍‍♀️ Sita - Shop 102 - Wheat - April 6")

    st.markdown("---")
    st.subheader(t("New User Signup"))
    st.text_input(t("New Username"))
    st.text_input(t("New Password"), type="password")
    if st.button(t("Signup")):
        st.success(t("Account created."))

elif menu == "📬 Grievance":
    show_title_image()
    st.header(t("Submit Complaint or Feedback"))
    st.text_input(t("Full Name"))
    st.text_input(t("Contact Email / Phone"))
    st.text_area(t("Your Message"))
    if st.button(t("Submit")):
        st.success(t("Thank you! We received your feedback."))

elif menu == "🌐 Language":
    show_title_image()
    st.header(t("Language Switcher"))
    st.write(t("Use the checkbox in the sidebar to toggle between Tamil and English."))
