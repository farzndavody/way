import flask
q=flask.Flask(__name__)
@q.route('/')
def love():
          return flask.render_template('5.html')
@q.route('/ko1')
def come():
    return'do not love you'
@q.route('/<admin>')
def pageadmine(admin):
    return flask.render_template('5.html')  
@q.route('/page<name>')
def name(name):
    return f'{name} amad'  
q.run()  