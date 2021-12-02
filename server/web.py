import os
import platform
import webbrowser

from flask import Flask, blueprints, jsonify, request

Web = blueprints.Blueprint('web', __name__, url_prefix='/web')

module = {"name": "web","version": "0.0.1"}
VERSION = '0.0.1'

@Web.route('/')
def web_index():
    return jsonify(module, {"status": "working"})


@Web.route('/open', methods=['get'])
def web_open():
    url = request.args.get('url')
    webbrowser.open(url)
    return jsonify(module, {"status": "working"})


@Web.route('/bugreport', methods=['get'])
def web_bugreport():
    body = '%23%23%23%23%20Description%0A'+'%23%23%23%23%23%23%20Describe%20your%20problem%20here%0A'+'%23%23%23%23%20Environment%0A'+'%20*%20YouTube-Converter%0A'+f'%20*%20Platform:%20{platform.system()}%0A'+f'%20*%20Arch:%20{platform.architecture()[0]}%0A'+f'%20*%20OS%20Version:%20{platform.version()}%0A'+f'%20*%20Python%20Version:%20{platform.python_version()}%0A'+f'%20*%20Proccesor:%20{platform.processor()}%0A'+f'%20*%20App%20Version:%20{VERSION}'
    title = '[Bug]'
    os.system(f'start https://github.com/philliphqs/YouTube-Converter/issues/new?body={body}&title={title}')
    return jsonify(module, {"status": "working"})
