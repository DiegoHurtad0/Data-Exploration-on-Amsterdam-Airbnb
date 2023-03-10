import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Amsterdam Airbnb")
st.markdown("Data Exploration on Amsterdam Airbnb")

# Read dataframe
dataframe = pd.read_csv(
    "data/WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 1000 pesos per night
df = df[df["price"] <= 1000]

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with price less than 1000 pesos")

# Create the plotly express figure
fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    color="price",
    size="price",
    size_max=10, 
    color_continuous_scale=px.colors.sequential.Reds, 
    zoom=11,
    height=800,
    width=950,
    hover_name="price",
    hover_data=["Meters from chosen location", "Location"],
    labels={'price':'Price'},
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.update_layout(
    mapbox_style='dark',
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0
    ),
)

fig.update_geos(center=dict(lat=df.iloc[0][2], lon=df.iloc[0][3]))

# Show the figure
st.plotly_chart(fig, use_container_width=True)
