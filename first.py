import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_mistral

st.title("🕷️ AI Web Scraper with Mistral")

url = st.text_input("Enter Website URL")

if st.button("Scrape Website"):
    if url:
        try:
            st.info("Scraping website...")
            raw_html = scrape_website(url)
            body = extract_body_content(raw_html)
            cleaned = clean_body_content(body)

            st.session_state.dom_content = cleaned
            st.success("✅ Scraping complete!")

            st.subheader("🔍 Preview of Cleaned Text")
            st.text_area("DOM Content", cleaned[:1000], height=300)

        except Exception as e:
            st.error(f"Scraping Error: {e}")

if "dom_content" in st.session_state:
    st.subheader("🧠 What would you like to extract?")
    parse_description = st.text_input("Enter a specific instruction, e.g. 'Extract all email addresses'")
    
    if st.button("Parse Content"):
        try:
            st.info("Parsing with Mistral...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_mistral(dom_chunks, parse_description)
            st.success("✅ Parsing complete!")

            st.subheader("📤 Parsed Output")
            st.text_area("Output", result, height=300)
        except Exception as e:
            st.error(f"Parsing Error: {e}")
