import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="FlavorGen",
    page_icon="🍴",
    layout="centered"
)

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B;
        color: white;
    }
    .menu-item {
        padding: 10px;
        border-radius: 5px;
        background-color: black;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .footer {
        text-align: center;
        color: #888;
        padding-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🍽️ FlavorGen AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Instant brand and menu creation for your next restaurant</p>", unsafe_allow_html=True)
st.divider()

# --- Sidebar Input ---
st.sidebar.header("📍 Concept Details")
cuisine = st.sidebar.selectbox("Pick a Cuisine", 
                             ["Indian", "Italian", "Mexican", "Japanese", "French", "Greek", "Chinese"])

if st.sidebar.button("Generate Concept"):
    from langchain_helper import generate_restaurant_name_and_items
    
    with st.spinner("🧑‍🍳 Our AI chef is crafting your menu..."):
        result = generate_restaurant_name_and_items(cuisine)
        
        # --- Results Layout ---
        st.balloons()
        
        # Restaurant Name Section
        st.markdown(f"### 🏨 Restaurant Name")
        st.info(f"**{result['restaurant_name']}**")
        
        st.markdown("### 📜 Signature Menu")
        
        # Processing and displaying menu items elegantly
        menu_items = [item.strip() for item in result["menu_items"].split(",")]
        
        # Display items in two columns for a better look
        col1, col2 = st.columns(2)
        for i, item in enumerate(menu_items):
            if i % 2 == 0:
                with col1:
                    st.markdown(f"<div class='menu-item'>{item}</div>", unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown(f"<div class='menu-item'>{item}</div>", unsafe_allow_html=True)
        
        # --- (Inside the 'if st.sidebar.button' block after the Signature Menu section) ---
        
        st.markdown("### ✨ Chef's Recommendations")
        
        # Split the recommendation string by newlines
        rec_list = result["recommendation"].strip().split("\n")
        
        for rec in rec_list:
            if "-" in rec:
                # Splitting name and description for styling
                dish_name, description = rec.split("-", 1)
                st.markdown(f"""
                    <div style='background-color: #fff4f4; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #FF4B4B;'>
                        <strong style='color: #FF4B4B;'>{dish_name.strip()}</strong> — 
                        <span style='color: #555;'>{description.strip()}</span>
                    </div>
                """, unsafe_allow_html=True)
            else:
                # Fallback if the format is slightly different
                st.write(rec)

# --- Footer ---
st.markdown(f"""
    <div class='footer'>
        <hr>
        Made with ❤️ by <b>Nitish</b>
    </div>
""", unsafe_allow_html=True)