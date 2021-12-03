# CS205 Final Project

## Getting Started Development

### Backend

Ensure you have Python 3.9 installed on your system, and that you have venv installed

1. Open up the backend folder in your favorite text editor.
2. In the integrated terminal, run `python3 -m venv env`, this creates the virtual environment
3. In the integrated terminal, run `source env/bin/activate`, this activates the virtual environment (needs to be run again whenever developing, if using VSCode can configure to automatically do so.
4. Check your python version, by running `python --version`, ensure that you are using the virtual env, terminal will have a (venv) on each line
5. In the integrated terminal, run `pip install -r requirements.txt`, this will install all required packages.

### Frontend

Ensure that you have Node v16 installed on your system.

1. Open up the frontend folder in your favorite text editor.
2. In the integrated terminal, run `npm i`, this will install all required packages for the project.

#### Normal Development

To run the project on your local machine, do the following:

1. Open a terminal window, and cd into the `frontend/` directory.
2. Type `npm run start-api` into the terminal window and hit enter.
3. Open a second terminal window, again cd into the `frontend/` directory.
4. Type `npm start` into the terminal window, and hit enter.
5. On your web browser, navigate to the link that the second command returned in
   the terminal window.
