from flask import Flask
import db

app = Flask(__name__, template_folder="templtates")

@app.route('/')
def index():
    return 'The simplest bug-tracker. Made by maxmine2'

@app.route('/bug')
def bug_main_page():
    return 'You could create a bug here'

@app.route('/bug/<int:bug_id>')
def bug_id_page(bug_id):
    return 'Bug #{} here'.format(bug_id)

@app.route('/bug/<int:bug_id>/close')
def bug_remove(bug_id):
    return "You could close bug #{} here".format(bug_id)

@app.route('/bug/<int:bug_id>/status')
def bug_status(bug_id):
    return "You could get a status of bug #{} here".format(bug_id)

@app.route('/bug/<int:bug_id>/status/change')
def bug_status_change_page(bug_id):
    return "You could change a status of bug#{} here".format(bug_id)

if __name__ == "__main__":
    app.run()