import streamlit as st

st.set_page_config(page_title="Login", layout="wide")

# ------------------ CSS ------------------
st.markdown("""
<style>
body {
    background-color: #f0f2f5;
}

/* Center container */
.main-box {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

/* Left text */
.left-section {
    padding-right: 50px;
}

.logo {
    color: #1877f2;
    font-size: 60px;
    font-weight: bold;
}

.tagline {
    font-size: 24px;
}

/* Login card */
.card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    width: 350px;
}

input {
    width: 100%;
    padding: 12px;
    margin-top: 10px;
    border-radius: 6px;
    border: 1px solid #ddd;
}

/* Buttons */
.btn-login {
    background-color: #1877f2;
    color: white;
    padding: 10px;
    width: 100%;
    border-radius: 6px;
    border: none;
    margin-top: 10px;
}

.btn-create {
    background-color: #42b72a;
    color: white;
    padding: 10px;
    width: 100%;
    border-radius: 6px;
    border: none;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("""
    <div class="left-section">
        <div class="logo">facebook</div>
        <div class="tagline">
            Connect with friends and the world around you.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    email = st.text_input("Email or Phone")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if email and password:
            st.success("Logged in (Demo)")
        else:
            st.error("Enter credentials")

    st.markdown("---")

    if st.button("Create New Account"):
        st.info("Signup flow here")

    st.markdown('</div>', unsafe_allow_html=True)