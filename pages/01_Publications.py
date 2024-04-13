#################################################################################
# Chat2VIS 
# https://chat2vis.streamlit.app/
# Paula Maddigan
#################################################################################


import streamlit as st
#import streamlit_nested_layout
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Chat2VIS")


st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem;'> \
            Chat2VIS</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;padding-top: 0rem;'>Creating Visualisations using Natural Language \
            with ChatGPT and Code Llama</h2>", unsafe_allow_html=True)

st.subheader(":violet[Academic Publications:]")

st.markdown('</a> Maddigan, P. and Susnjak, T. <a style="text-align: center;padding-top: 0rem;" href="https://doi.org/10.1109/ACCESS.2023.3274199">Chat2VIS: Generating Data \
                    Visualisations via Natural Language using ChatGPT, Codex and GPT-3 \
                 Large Language Models. </a> IEEE Access, vol. 11, pp. 45181-45193, 2023', unsafe_allow_html=True)

st.markdown('</a> Maddigan, P. and Susnjak, T. <a style="text-align: center;padding-top: 0rem;" href="https://doi.org/10.48550/arXiv.2303.14292">Chat2VIS: Fine-Tuning Data Visualisations using Multilingual \
Natural Language Text and Pre-Trained Large Language Models. </a> arXiv preprint arXiv:2303.14292, 2023', unsafe_allow_html=True)

st.subheader(":violet[Streamlit Blogs:]")
st.markdown('</a>Maddigan, P. <a style="text-align: center;padding-top: 0rem;" href="https://blog.streamlit.io/chat2vis-ai-driven-visualisations-with-streamlit-and-natural-language">Chat2VIS: AI-driven visualisations with Streamlit and natural language </a>', unsafe_allow_html=True)
st.markdown('</a>Maddigan, P. <a style="text-align: center;padding-top: 0rem;" href="https://blog.streamlit.io/comparing-code-llama-vs-gpt-3-5-and-gpt-4-to-generate-visualisations">Comparing data visualisations from Code Llama, GPT-3.5, and GPT-4 </a>', unsafe_allow_html=True)

st.subheader(":violet[Medium Articles:]")
st.markdown('</a>Maddigan, P. <a style="text-align: center;padding-top: 0rem;" href="https://medium.com/@paula_m/chat2vis-ai-driven-data-visualisations-with-streamlit-chatgpt-and-natural-language-d70a8e41b9d4">Chat2VIS: AI-driven data visualisations with Streamlit, ChatGPT and natural language </a>', unsafe_allow_html=True)
st.markdown('</a>Maddigan, P. <a style="text-align: center;padding-top: 0rem;" href="https://medium.com/@paula_m/showcasing-code-llama-gpt-3-5-instruct-and-gpt-4-for-generating-data-visualisations-f8a959729c70">Showcasing Code Llama, GPT-3.5 Instruct, and GPT-4 for generating data visualisations </a>', unsafe_allow_html=True)
st.markdown('</a>Maddigan, P. <a style="text-align: center;padding-top: 0rem;" href="https://medium.com/@paula_m/chat2vis-generating-data-visualisations-from-natural-language-text-using-gpt-3-and-chatgpt-7f968d4dac78">Chat2VIS — Generating Data Visualisations from Natural Language Text using GPT-3 and ChatGPT</a>', unsafe_allow_html=True)

