from flask import Flask, render_template, redirect, url_for, flash, request
from models import init_db, add_sample_movies, get_all_movies, get_movie_by_id, save_contact
# Para comentar todo ctrl + k + c


app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static",
)


app.config['SECRET_KEY'] = 'clave secreta'

from flask import render_template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_movie")
def add_movie():
    return render_template("add_movie.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name') 
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Por favor rellena los campos requeridos.', 'error')
            return redirect(url_for('contact.html'))

        save_contact(name, email, subject, message)

        flash('Gracias por tu mensaje — te responderemos pronto.', 'success')
        return redirect(url_for('contact'))
    return render_template("contact.html")

@app.route("/movies")
def movies():
    movies_list = get_all_movies()
    return render_template("movies.html", movies=movies_list)


@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = get_movie_by_id(movie_id)
    if not movie:
        return redirect(url_for("movies"))
    return render_template("movie_detail.html", movie=movie)

if __name__ == "__main__":
    init_db()

    existing = get_all_movies();
    if not existing:
        add_sample_movies()
    app.run(debug=True)

