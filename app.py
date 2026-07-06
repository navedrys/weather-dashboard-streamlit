import streamlit as st
import pandas as pd
from weather_api import get_weather
from file_handler import (
    save_history,
    history_dataframe
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤",
    layout="wide"
)

st.title("🌤 Weather Dashboard")

st.markdown(
    "Search live weather information using **OpenWeather REST API**."
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Page",
    [
        "Home",
        "Search History"
    ]
)

# -----------------------------
# HOME PAGE
# -----------------------------

if page == "Home":

    city = st.text_input(
        "Enter City Name",
        placeholder="Example: Pune"
    )

    search = st.button("Get Weather")

    if search:

        if city.strip() == "":
            st.warning("Please enter a city name.")

        else:

            with st.spinner("Fetching weather..."):

                weather = get_weather(city)

            if weather is None:

                st.error("City not found.")

            else:

                save_history(weather)

                st.success("Weather Loaded Successfully")

                st.divider()

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "📍 City",
                        weather["city"]
                    )

                    st.metric(
                        "🌡 Temperature",
                        f"{weather['temperature']} °C"
                    )

                    st.metric(
                        "🤗 Feels Like",
                        f"{weather['feels_like']} °C"
                    )

                    st.metric(
                        "💧 Humidity",
                        f"{weather['humidity']} %"
                    )

                with col2:

                    st.metric(
                        "☁ Condition",
                        weather["condition"]
                    )

                    st.metric(
                        "📝 Description",
                        weather["description"].title()
                    )

                    st.metric(
                        "🌬 Wind Speed",
                        f"{weather['wind_speed']} m/s"
                    )

                    st.metric(
                        "🌍 Country",
                        weather["country"]
                    )

                st.divider()

                st.subheader("Raw JSON Response")

                st.json(weather)


# -----------------------------
# SEARCH HISTORY PAGE
# -----------------------------

elif page == "Search History":

    st.header("📜 Search History")

    df = history_dataframe()

    if df.empty:

        st.info("No search history found.")

    else:

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download History as CSV",
            data=csv,
            file_name="weather_history.csv",
            mime="text/csv"
        )

        st.divider()

        st.subheader("Statistics")

        total_searches = len(df)

        unique_cities = df["city"].nunique()

        avg_temp = round(df["temperature"].mean(), 2)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Searches",
            total_searches
        )

        col2.metric(
            "Unique Cities",
            unique_cities
        )

        col3.metric(
            "Average Temperature",
            f"{avg_temp} °C"
        )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "Built using Python • Streamlit • REST API • JSON • OpenWeather"
)