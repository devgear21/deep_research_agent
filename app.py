import streamlit as st
from server import handle
from IPython.display import Image
from PIL import Image as PILImage

st.set_page_config(page_title="Deep Researcher", layout="wide")
st.title("🔍 Deep Research Agent")

# Input box
query = st.text_input("Enter your research topic or question:")

if st.button("Run Research") and query:
    with st.spinner("⏳ Running research workflow..."):
        result = handle({"query": query})
        st.success("Research complete!")
        st.markdown("### Final Report")
        st.write(result["report"])

        if "workflow.png" in result:
            st.image(result["workflow.png"], caption="📊 Research Agent Workflow")


st.markdown("---")
st.markdown("Made with LangGraph + Groq")
