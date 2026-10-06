import streamlit as st
from fashion_ai import get_fashion_advice


st.set_page_config(
    page_title="AI Fashion Assistant",
    page_icon="👗",
    layout="wide"
)


st.title("👗 AI Fashion Assistant")
st.write("Get personalized outfit recommendations using Google Gemini AI.")


# Sidebar
st.sidebar.header("Fashion Preferences")

occasion = st.sidebar.selectbox(
    "Occasion",
    [
        "College",
        "Casual",
        "Party",
        "Wedding",
        "Interview",
        "Festival",
        "Travel"
    ]
)

gender = st.sidebar.selectbox(
    "Gender",
    [
        "Female",
        "Male",
        "Unisex"
    ]
)

season = st.sidebar.selectbox(
    "Season",
    [
        "Summer",
        "Winter",
        "Spring",
        "Autumn",
        "All Season"
    ]
)

style = st.sidebar.selectbox(
    "Style",
    [
        "Casual",
        "Formal",
        "Traditional",
        "Western",
        "Streetwear",
        "Minimalist",
        "Trendy"
    ]
)

color_preference = st.sidebar.text_input(
    "Preferred Color",
    "Blue"
)

budget = st.sidebar.selectbox(
    "Budget",
    [
        "Under ₹500",
        "₹500 - ₹1000",
        "₹1000 - ₹2000",
        "₹2000 - ₹5000",
        "Above ₹5000"
    ]
)

outfit_type = st.sidebar.selectbox(
    "Outfit Type",
    [
        "Dress",
        "Top & Jeans",
        "Shirt & Trousers",
        "Kurti",
        "Saree",
        "T-Shirt & Jeans",
        "Any"
    ]
)


# Main button
if st.button("✨ Get Fashion Advice"):

    with st.spinner("Gemini is creating your fashion recommendation..."):

        advice = get_fashion_advice(
            occasion=occasion,
            gender=gender,
            season=season,
            style=style,
            color_preference=color_preference,
            budget=budget,
            outfit_type=outfit_type
        )

    st.subheader("👗 Your Fashion Recommendation")

    st.write(advice)