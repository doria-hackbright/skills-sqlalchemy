"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').first()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_from_year = Model.query.filter_by(year=year).all()

    for model in models_from_year:
        print model.name, model.brand_name, model.brand.headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands = Brand.query.all()

    for brand in all_brands:
        print brand.name
        for model in brand.models:
            print "\t", model.name


# -------------------------------------------------------------------

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Returns a list of brand objects that contain or is equal to mystr."""

    mystr = "%" + mystr + "%"
    return Brand.query.filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    """Returns a list of model objects with year between start_year and end_year."""

    return Model.query.filter(Model.year.in_(range(start_year + 1, end_year))).all()

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# Since there is no "execution method" at the end (e.g. all(), first(), one()),
# a SQLAlchemy query object is returned.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is a "linking" table that does not contain any meaningful records
# when used on its own. It manages a "many-to-many" relationship, such as movies and actors.
# A movie can contain many actors and each actor can be a part of more than one movie.
