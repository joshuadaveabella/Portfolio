# Joshua Dave G. Abella | Autobiography and Portfolio (Streamlit)

## Install and run (Windows)
```
python --version                  # needs Python 3.9 or newer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
On macOS/Linux, activate with `source .venv/bin/activate` instead.
The app opens at http://localhost:8501. Stop it with Ctrl+C.

## Make it yours
Open `app.py` and edit the "YOUR CONTENT" block (look for `EDIT`).
Put your photo at `assets/profile.jpg`.

## Deploy (bonus points)
1. Create a PUBLIC GitHub repo and push these files (the .gitignore keeps .venv and secrets out).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Create app -> pick the repo, branch `main`, main file `app.py` -> Deploy.
4. Submit the `.streamlit.app` link.
