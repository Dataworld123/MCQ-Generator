from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Dataworld123',
    author_email='nishantsingh801102@gmail.com',
    install_requires=["google-generativeai","langchain","streamlit","python-dotenv","PyPDF2","langchain_google_genai"],
    packages=find_packages()
)