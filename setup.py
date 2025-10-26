from setuptools import setup, find_packages

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# --- Package Metadata ---
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "rbcodes"
AUTHOR_EMAIL = "rishabhlashkari@gmail.com"
PACKAGE_NAME = "books_recommender"
DESCRIPTION = "A small package for a Books Recommender System"
VERSION = "0.0.1"

# --- Requirements ---
REQUIREMENTS = [
    "streamlit",
    "numpy",
]

# --- Setup Configuration ---
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="MIT",
    python_requires=">=3.7",
    install_requires=REQUIREMENTS,
)
