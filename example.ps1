py -m venv .venv
.\.venv\Scripts\activate
py -m pip freeze
py -m pip install -r requirements.txt
py pdf_search.py example.pdf "embedded user"