python -m pip install matplotlib

        A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific virtual environment that contains a copy of a global interpreter. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions. To create a virtual environment and install the required packages, enter the following commands as appropriate for your operating system:
for mac
python3 -m venv .venv
source .venv/bin/activate

for windows
py -3 -m venv .venv
.venv\scripts\activate


editor.wordWrap   :Controls how lines should wrap. 自动换行