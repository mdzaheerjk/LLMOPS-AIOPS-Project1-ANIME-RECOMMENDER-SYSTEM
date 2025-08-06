import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommnder",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)


