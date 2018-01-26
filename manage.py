from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cc.html')


@app.route('/note', methods=['GET','PUT'])
def index_cache_ajax():
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)