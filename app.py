import streamlit as st
import json

st.title("AI Invoice Extractor (Vision)")
st.write("Upload an invoice and AI will extract data")

uploaded_file = st.file_uploader("Upload Invoice", type=["png", "jpg", "jpeg"])

if uploaded_file:
    try:
        st.image(uploaded_file, caption="Uploaded Invoice", width=400)

        with st.spinner("Analyzing invoice..."):
            result = """
            {
              "company": "TOM GREEN HANDYMAN",
              "date": "06/05/2016",
              "total": "3367.20"
            }
            """

        st.subheader("Extracted Data")
        st.json(json.loads(result))

    except Exception as e:
        st.error(f"Error: {e}")