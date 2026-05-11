# Lab05 — Amazon Chatbot

This folder contains a simple Streamlit-based Amazon customer support chatbot (`chatbot.py`).

## Prerequisites
- Python 3.10+ (your system has 3.14 — that's fine)
- `python-venv` package (for creating virtual environments)
- Network access to install Python packages

## Recommended (create and use a virtual environment)
From the `Lab05` folder run:

```bash
cd Lab05
# create a virtual environment (only once)
python -m venv .venv_lp2_lab05

# activate it (Linux/macOS)
source .venv_lp2_lab05/bin/activate

# upgrade pip and install dependencies
python -m pip install --upgrade pip setuptools wheel
pip install streamlit
```

Notes:
- If a `.venv_lp2_lab05` was already created for this project, just activate it with `source .venv_lp2_lab05/bin/activate`.
- On systems where system package management blocks `pip install --user`, use a virtualenv as above.

## Run the app
With the virtual environment activated (or using the venv python directly), run:

```bash
# easiest (when venv is active)
streamlit run chatbot.py

# or explicitly with the venv python and fixed port
.venv_lp2_lab05/bin/python -m streamlit run chatbot.py --server.port 8501 --server.headless true
```

Open the app in your browser at: http://localhost:8501

## Stop the server
- Press `Ctrl+C` in the terminal running Streamlit.

## Accessing remotely (SSH)
If the machine running the app is remote, forward the port to your local machine:

```bash
ssh -L 8501:localhost:8501 user@remote-host
# then open http://localhost:8501 on your local machine
```

## Troubleshooting
- `ImportError: No module named streamlit`: activate the venv and install `streamlit` as shown above.
- If you cannot create a venv due to restricted environment, consider using `pipx` or ask your system admin.
- If the app starts but you cannot access the page, check firewall/port forwarding and whether another service is using port 8501.

## Files
- `chatbot.py` — the Streamlit application

If you want, I can also add a `requirements.txt` or a short script to automate setup. Tell me which you prefer.
