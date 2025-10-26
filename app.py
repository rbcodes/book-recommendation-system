import pickle
import streamlit as st
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="📚 Book Recommender System",
    page_icon="📖",
    layout="wide"
)

# ---------- CUSTOM STYLING ----------
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }

    /* Titles */
    .main-title {
        text-align: center;
        font-size: 64px !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 5px;
        letter-spacing: 3px;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    .sub-title {
        text-align: center;
        font-size: 20px !important;
        color: #b8b8d1;
        margin-bottom: 60px;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* Selectbox container */
    .select-container {
        max-width: 500px;
        margin: 0 auto 30px auto;
    }
    
    /* Center selectbox */
    div[data-baseweb="select"] {
        max-width: 500px;
        margin: 0 auto !important;
    }

    /* Button styling */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-bottom: 50px;
    }
    
    div.stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        font-weight: 700;
        border: none;
        border-radius: 50px;
        padding: 15px 60px;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin: 0 auto;
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    /* Book card */
    .book-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        height: 100%;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .book-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.4);
        border: 1px solid rgba(102, 126, 234, 0.5);
        background: rgba(102, 126, 234, 0.1);
    }

    /* Book cover image */
    .book-cover {
        width: 100%;
        height: 280px;
        object-fit: cover;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        display: block;
        margin: 0 auto;
        transition: all 0.3s ease;
    }
    
    .book-card:hover .book-cover {
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
    }

    /* Book title */
    .book-title {
        text-align: center;
        font-weight: 600;
        color: #ffffff;
        margin-top: 15px;
        font-size: 14px;
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1.4;
    }

    /* Section header */
    .rec-header {
        text-align: center;
        color: #ffffff;
        font-size: 28px;
        font-weight: 700;
        margin: 50px 0 40px 0;
        letter-spacing: 1px;
    }
    
    .rec-header-highlight {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 40px 0;
    }

    /* Loading spinner */
    .stSpinner > div {
        border-color: #667eea transparent transparent transparent !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Selectbox styling */
    .stSelectbox {
        max-width: 500px;
        margin: 0 auto !important;
    }
    
    .stSelectbox label {
        color: #b8b8d1 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        text-align: center !important;
        display: block !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HEADER ----------
st.markdown(
    """
    <p class="main-title">📚 BOOKFINDER</p>
    <p class="sub-title">Discover your next adventure powered by AI</p>
    """,
    unsafe_allow_html=True
)

# ---------- LOAD DATA ----------
@st.cache_resource
def load_data():
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
    final_ratings = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
    return model, book_names, book_pivot, final_ratings

model, book_names, book_pivot, final_ratings = load_data()

# ---------- DEFAULT IMAGE ----------
DEFAULT_IMAGE = "https://placehold.co/300x400/1a1a2e/667eea?text=No+Cover"

# ---------- RECOMMENDATION FUNCTION ----------
def recommendBooks(book_name):
    book_list = []
    poster_url_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6
    )

    for i in range(len(suggestions)):
        books = book_pivot.index[suggestions[i]]
        for j in books:
            book_list.append(j)
            try:
                url = final_ratings[final_ratings["Book-Title"] == j]["Image-URL-L"].iloc[0]
                print(url)
                if not str(url).startswith("http"):
                    url = DEFAULT_IMAGE
            except Exception:
                url = DEFAULT_IMAGE
            poster_url_list.append(url)

    return book_list[1:], poster_url_list[1:]  # Skip first (same book)

# ---------- INPUT ----------
st.markdown('<div class="select-container">', unsafe_allow_html=True)
selected_book = st.selectbox(
    "🔍   Search for a book you love to discover similar recommendations.",
    book_names,
    index=None,
    placeholder="Type or select a book title...",
)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTON ----------
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    show_recs = st.button("✨ Get Recommendations", use_container_width=True)

# ---------- RECOMMENDATION DISPLAY ----------
if show_recs and selected_book:
    with st.spinner("🔮 Finding your perfect matches..."):
        recommendation_books, poster_urls = recommendBooks(selected_book)
    
    st.markdown(
        f'<p class="rec-header">🎯 Recommended for <span class="rec-header-highlight">"{selected_book}"</span></p>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f'''
                <div class="book-card">
                    <img src="{poster_urls[i]}" class="book-cover" onerror="this.src='{DEFAULT_IMAGE}'"/>
                    <p class="book-title">{recommendation_books[i]}</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

elif show_recs and not selected_book:
    st.warning("⚠️ Please select a book first!")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; color: #7a7a8c; font-size: 14px; margin-top: 50px;'>
    Built with ❤️ using Streamlit & Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)