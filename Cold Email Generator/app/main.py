import streamlit as st
import textwrap
from langchain_community.document_loaders import WebBaseLoader 

from chains import Chain
from portfolio import Portfolio 
from utils import clean_text 

def wrap_text(text, width=70):
    paragraphs = text.split('\n')
    wrapped_text = [textwrap.fill(paragraph, width=width) if paragraph.strip() else "" for paragraph in paragraphs]
    return '\n'.join(wrapped_text)

def create_streamlit_app(llm, portfolio, clean_text):
    st.title('📧 Cold Email Generator')
    url_input = st.text_input('Please enter the URL of the job posting you are applying for:', value='https://jobs.nike.com/job/R-47337?from=job%20search%20funnel')
    submit_button = st.button('Submit')

    if submit_button:
        try: 
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_cold_email(job, links)
                wrapped_email = wrap_text(email, width=120)
                st.code(wrapped_email, language='markdown')
        except Exception as e:
            st.error(f'The following error occurred: {e}')

if __name__ == '__main__':
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout='wide', page_title='Cold Email Generator', page_icon='📧')
    create_streamlit_app(chain, portfolio, clean_text)