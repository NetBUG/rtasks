# Task
The SMS text corpus attached (see in data/) is separated into 2 classes (`ham`/`spam`). The model is to be built to discriminate between these two classes.
Metric - ROC AUC, as the task is binary.

# Usage
Installing dependencies:
`pip3 install -r reqirements.txt`
Virtual environment will work perfectly.

Running:
`python3 app.py`
The model will be built, and AU will be shown.

You can use *gaussian* or *bernoulli* as a command-line parameter to change model behavior, e.g.
`python3 app.py gaussian` will build you a (useless) Gaussian model.