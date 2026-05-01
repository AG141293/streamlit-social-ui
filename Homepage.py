import streamlit as st

st.set_page_config(page_title="Social Home", layout="wide")

# ------------------ CSS ------------------
st.markdown("""
<style>
body {
    background-color: #f0f2f5;
}

/* Top Navbar */
.navbar {
    background-color: #1877f2;
    padding: 12px;
    color: white;
    font-size: 20px;
    font-weight: bold;
}

/* Sidebar */
.sidebar {
    padding: 10px;
}

.sidebar-item {
    padding: 10px;
    border-radius: 8px;
    cursor: pointer;
}
.sidebar-item:hover {
    background-color: #e4e6eb;
}

/* Post Card */
.post {
    background: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}

.post-header {
    font-weight: bold;
    margin-bottom: 5px;
}

.post-actions {
    margin-top: 10px;
    display: flex;
    justify-content: space-around;
    color: gray;
    cursor: pointer;
}

/* Right panel */
.right-box {
    background: white;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAVBAR ------------------
st.markdown('<div class="navbar">📘 Social App</div>', unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2, col3 = st.columns([1,2,1])

# -------- LEFT SIDEBAR --------
with col1:
    st.markdown("### Menu")
    st.markdown('<div class="sidebar-item">🏠 Home</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">👥 Friends</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">📺 Watch</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">🛒 Marketplace</div>', unsafe_allow_html=True)

# -------- FEED --------
with col2:
    st.markdown("### Create Post")
    post = st.text_area("What's on your mind?")
    if st.button("Post"):
        st.success("Posted!")

    st.markdown("### Feed")

    # Example posts
    posts = [
        ("Ankita", "Working on my Streamlit project 🚀"),
        ("Rahul", "Just completed a Python project!"),
        ("Priya", "Learning UI design today 🎨")
    ]

    for user, content in posts:
        st.markdown(f"""
        <div class="post">
            <div class="post-header">{user}</div>
            <div>{content}</div>
            <div class="post-actions">
                👍 Like &nbsp;&nbsp; 💬 Comment &nbsp;&nbsp; ↗️ Share
            </div>
        </div>
        """, unsafe_allow_html=True)

# -------- RIGHT PANEL --------
with col3:
    st.markdown("### Contacts")
    st.markdown('<div class="right-box">👤 Rahul<br>👤 Priya<br>👤 Aman</div>', unsafe_allow_html=True)