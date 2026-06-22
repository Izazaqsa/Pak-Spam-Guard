import streamlit as st
import pickle

# Set page layout and title
st.set_page_config(page_title="Pak Spam Guard", page_icon="🛡️", layout="centered")

# Custom header
st.title("🛡️ Pak Spam Guard")
st.subheader("Localized Multilingual Spam & Fraud Detection")
st.write(
    "Input any message (English, Roman Urdu, or Urdu script) below to check if it's legitimate or a scam."
)

# Load the saved vectorizer and classifier
@st.cache_resource # Keeps the model loaded in memory for faster performance
def load_assets():
    with open('splitter.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('detector.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

try:
    vectorizer, model = load_assets()
except FileNotFoundError:
    st.error("⚠️ Error: 'model.pkl' or 'vectorizer.pkl' not found. Please run your training script first.")
    st.stop()

# Text input box for the user message
user_input = st.text_area(
    "Enter the message text here:", 
    placeholder="e.g., BISP khushkhbri! Aap ki qist jari ho chuki hai...",
    height=150
)

# Predict button
if st.button("Analyze Message", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter some text before checking.")
    else:
        # 1. Preprocess and transform the raw string input using the fitted CountVectorizer
        transformed_input = vectorizer.transform([user_input])
        
        # 2. Run prediction using the loaded BernoulliNB model
        prediction = model.predict(transformed_input)[0]
        
        # 3. Display the result beautifully based on the model's mapped outputs
        # (Assuming 1 = spam, 0 = ham from your mapping)
        st.write("---")
        if prediction == 1 or prediction == "spam":
            st.error("🚨 **Result: SPAM / FRAUD DETECTED**")
            st.info("💡 *This message displays patterns common to localized scams in Pakistan (e.g., phishing links, fake prize draws, or fraudulent utility alerts).*")
        else:
            st.success("✅ **Result: HAM (LEGITIMATE)**")
            st.info("💡 *This message looks safe and does not match standard scam behaviors tracked in the dataset.*")

# Footer
st.markdown("---")
st.caption("Developed for Pak-Spam-Guard Portfolio Project.")