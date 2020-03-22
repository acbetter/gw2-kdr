from flask import Flask, jsonify

from kdr import my_job

app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def root():
    return app.send_static_file('kdr.html')


@app.route('/update/<int:pass_key>')
def update_data(pass_key: int):
    # please change the key when you deploy
    if pass_key == 123456789:
        my_job()
        return jsonify({'Message': 'Done.'})
    else:
        return jsonify({'Message': 'Wrong Pass Key.'})


if __name__ == "__main__":
    app.run()
