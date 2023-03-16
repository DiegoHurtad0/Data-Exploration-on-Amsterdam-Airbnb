import pandas as pd
import plotly.express as px
# from PIL import Image

import streamlit as st
# from streamlit_lottie import st_lottie
# from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Display title and text
# Confit
st.set_page_config(page_title='Amsterdam Airbnb Tool', page_icon=':bar_chart:', layout='wide')

# Title
st.title("Data Exploration on Amsterdam Airbnb")

# Read dataframe
df = pd.read_csv(
    "data/WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
)

# We have a limited budget, therefore we would like to exclude
# listings with a price above 1000 pesos per night
df = df[df["price"] <= 1500]

# Display dataframe and text
st.dataframe(df)


st.subheader("Below is a map showing all the Airbnb listings with price less than 1500 mx pesos")

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
    height=600,
    width=950,
    hover_name="price",
    hover_data=["Meters from chosen location", "Location"],
    labels={'price':'Price'},
)

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig.update_layout(
    mapbox_style='stamen-terrain',
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        bearing=0
    ),
)

fig.update_geos(center=dict(lat=df.iloc[0][2], lon=df.iloc[0][3]))

# Show the figure
st.plotly_chart(fig, use_container_width=True)

st.markdown("Diego Gustavo Hurtado Olivares")

# lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
# lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
# lottie_hello = load_lottieurl(lottie_url_hello)
# lottie_download = load_lottieurl(lottie_url_download)


# st_lottie(lottie_hello, key="hello")

# if st.button("Download"):
#     with st_lottie_spinner(lottie_download, key="download"):
#         time.sleep(5)
#     st.balloons()


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Scientist: [@Diego Hurtado](https://www.linkedin.com/in/diegohurtadoo/)**', icon="👨🏻‍💻")
with c2:
    st.info('**GitHub: [@DiegoHurtad0](https://github.com/DiegoHurtad0/DiegoHurtad0)**', icon="💻")
with c3:
    st.info('**Medium: [Diego Hurtado](https://medium.com/@diego.hurtado.olivares)**', icon="📊")
