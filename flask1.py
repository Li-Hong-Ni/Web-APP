
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def postcode(postcode)->str:
    parameters = {'postcode':postcode,'key':'2dc3f0c9985d784d29f3e8ef4daeb4c1'}
    base = 'http://v.juhe.cn/postcode/query'
    response = requests.get(base, parameters)
    answer = response.json()
    return answer


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    youbian = request.form['youbian']
    title = '这是查询结果:'
    results = postcode(youbian)
    return render_template('results.html',
                           the_title=title,
                           the_youbian=youbian,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎使用邮编查询地址')


if __name__ == '__main__':
    app.run(debug=True)
