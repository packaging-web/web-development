from app import app
from db_setup import init_db, db_session
from forms import ProductSearchForm, ProductForm
from flask import flash, render_template, request, redirect
from models import Master

init_db()

@app.route('/', methods = ['GET', 'POST'])
def index():
    search = ProductSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form = search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Master)
        results = qry.all()
        print(results)

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results = results)

@app.route('/new_product', methods = ['GET', 'POST'])
def new_product():
    # add a new product
    form = ProductForm(request.form)

    if request.method == 'POST' and form.validate():
        # saving new product
        product = Master()
        save_changes(product, form, new=True)
        flash('New product added successfully!')
        return redirect('/')

    return render_template('new_product.html', form=form)


def save_changes(product, form, new=False):

    product.material_of_construction = form.material_of_construction.data
    product.moulding_process = form.moulding_process.data
    product.neck_type = form.neck_type.data
    product.SKU = form.SKU.data
    product.product = form.product.datax
    product.best_suited_for = form.best_suited_for.data
    product.container_type = form.container_type.data
    product.vendor_name = form.vendor_name.data
    product.product_name = form.product_name.data
    product.ofc = form.ofc.data
    product.weight = form.weight.data
    product.price = form.price.data
    product.shape = form.shape.data

    if new:
        # add new product to the database
        db_session.add(product)

    # commit the data to the database
    db_session.commit()

if __name__ == '__main__':
    app.run()
