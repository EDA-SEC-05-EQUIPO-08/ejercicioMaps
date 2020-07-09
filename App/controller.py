"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    """
    Funcion que imprime una lista que se pasa por parametro
    Args:
        lst:: list
            Lista que se desea iterar e imprimir
    Return :: None
    """
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)



def compareratings (movie1, movie2):
    """
    Funcion que compara dos peliculas el rating
    Args:
        movie1::
            Primera película a comparar
        movie 2::
            Seguna Pelicula a comparar
    Return :: Boolean
        verdadero si la primera tienen mejor rating, falso si la segunda tiene mayor rating
    """
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))


# Funciones para la carga de datos 

def loadBooks (catalog, sep=','):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    Args:
        catalog::
            Catalogo donde se añadiran los libros
        sep = ','
            separdor usado en la carga de los elementos
    Return:: None
    """
    t1_start = process_time() #tiempo inicial
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(booksfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            # Se adiciona el libro a la lista de libros
            model.addBookList(catalog, row)
            # Se adiciona el libro al mapa de libros (key=title)
            model.addBookMap(catalog, row)
            # Se obtienen los autores del libro
            authors = row['authors'].split(",")
            # Cada autor, se crea en la lista de autores del catalogo, y se 
            # adiciona un libro en la lista de dicho autor (apuntador al libro)
            for author in authors:
                model.addAuthor (catalog, author.strip(), row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga libros:",t1_stop-t1_start," segundos")   



def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    Args:
        None
    Return
        Catalogo vacio para manejar los libros
    """
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    Args:
        catalog
            catalogo en el cual se cargaran los datos del archivo ccsv
    return 
        None
    """
    loadBooks(catalog)
    

# Funciones llamadas desde la vista y enviadas al modelo


def getBookInfo(catalog, bookTitle):
    """
    Funcion que encuentra un elemento con cierto titulo dentro de un arreglo (catalogo)
    Args:
        catalog
            Catalogo donde se encuentra la informaciom
        bookTitle:: str
            nombre del libro que se desea encontrar
    Return
        el libro buscado si existe está en la lista, None si no
    """
    t1_start = process_time() #tiempo inicial
    book=model.getBookInList(catalog, bookTitle)
    #book=model.getBookInMap(catalog, bookTitle)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución buscar libro:",t1_stop-t1_start," segundos")   
    if book:
        return book
    else:
        return None   

def getAuthorInfo(catalog, authorName):
    """
    Metodo que busca en el catalogo a un autor con un nombre dado
    Args:
        catalog
            Catalogo donde se encuentra la informaciom
        authorName:: str
            nombre del libro que se desea encontrar
    Return
        el autor buscado si existe está en la lista, None si no
    """
    author=model.getAuthorInfo(catalog, authorName)
    if author:
        return author
    else:
        return None    

