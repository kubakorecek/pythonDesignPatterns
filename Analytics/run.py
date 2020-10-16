from application import app # bad practice, but on debug necessary






import application.routes

if __name__ == '__main__':



    app.run(debug=True, port = 9000)