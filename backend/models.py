import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    # Tabla peliculas 
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT,
            year INTEGER,
            genre TEXT,
            description TEXT,
            rating REAL DEFAULT 0.0,
            poster_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    #Tabla contactos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT,
            message TEXT NOT NULL,
            created at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close() 
    print("Base de datos incializada")

# Añade películas de ejemplo para tener datos de prueba
def add_sample_movies():
    movies = [
        ("El Padrino", "Francis Ford Coppola", 1972, "Drama",
        "La historia de una familia mafiosa italiana", 9.2,
        "https://example.com/poster1.jpg"),
        ("Pulp Fiction", "Quentin Tarantino", 1994, "Crimen",
        "Historias entrelazadas en Los Angeles", 8.9,
        "https://example.com/poster2.jpg"),
    ]    

    conn = sqlite3.connect('proyecto.db') 
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO movies(title, director, year, genre, description, rating, poster_url)
        VALUES(?,?,?,?,?,?,?)
    ''', movies)
    
    conn.commit()
    conn.close() 
    print("Inserción realizada con éxito")

def get_all_movies():
    # Obtiene todas las peliculas de la base de datos
    conn = sqlite3.connect('proyecto.db')    
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies ORDER BY created_at DESC')
    movies = cursor.fetchall()

    conn.close()
    return movies

def get_movie_by_id(movie_id):
    conn = sqlite3.connect('proyecto.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # La coma en (movie_id,) nos especifica que es una tupla, no una string
    cursor.execute('SELECT * FROM movies WHERE id =?', (movie_id,))
    movie = cursor.fetchone()
    
    conn.close()
    return movie

# Guarda los 
def save_contact(name, email, subject, message):
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, email, subject, message)
        VALUES (?, ?, ?, ?)       
    ''', (name, email, subject, message))

    conn.commit()
    conn.close()
    print(f"Contacto guardado: {name}")