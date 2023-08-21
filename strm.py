import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Wilfred Lai - Portfolio",
        page_icon="📚",
        layout="centered"
    )

    # Header
    st.title("Wilfred Lai")
    st.write("Finalist at Taita Taveta University")
    st.write("Pursuing Bsc Mathematics and Computer Science")
    
    # Display your photo
    st.image("pht.png", caption="Wilfred Lai", use_column_width=True)

    # Contact section
    st.header("Contact")
    st.write("Feel free to reach out to me via email:")
    st.write("[wilfredayiekolai@gmail.com](mailto:wilfredayiekolai@gmail.com)")

    # FAQ section
    st.header("FAQ")
    st.write("Here are some frequently asked questions:")
    st.write("Q: What are your areas of interest?")
    st.write("A: I'm interested in data analysis, machine learning, and web development.")
    st.write("Q: Do you have any coding projects?")
    st.write("A: Yes, I've worked on various coding projects, including club members management system, web developments")
    
    # Social media links
    st.header("Connect with me")
    st.write("[LinkedIn](https://www.linkedin.com/in/your-linkedin)")
    st.write("[Twitter](https://twitter.com/@Wlaihandrozz)")
    st.write("[GitHub](https://github.com/Lai540)")

if __name__ == "__main__":
    main()
