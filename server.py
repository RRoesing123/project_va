from flask_app import app

from flask_app.controllers import vets, users

if __name__=="__main__":   
    app.run(debug=True)    



# @app.route('/user', methods=['post'])
# def handle_data():
#     print(request.form)['name']
#     session['name'] = request.form['name']
#     session['dojoLocation'] = request.form['dojoLocation']
#     session['favoriteLanguage'] = request.form['favoriteLanguage']
#     session['comments'] = request.form['comments']
#     return redirect('/show')