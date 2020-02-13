from app import app
from db_setup import init_db, db_session
from forms import SearchForm, ProductForm
from flask import flash, render_template, request, redirect
from models import Master
from tables import Results

init_db()

@app.route('/', methods = ['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form = search)

@app.route('/results')
def search_results(search):
    results = []

    if search.data['product_select'] == 'Shampoo':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Shampoo'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    elif search.data['product_select'] == 'Lotion':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Lotion'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    elif search.data['product_select'] == 'Cream':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Cream'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    elif search.data['product_select'] == 'Balm':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Balm'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    elif search.data['product_select'] == 'Oil':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Oil'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    elif search.data['product_select'] == 'Conditioner':
        if search.data['shape_select'] == 'Cylinder':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Cylinder'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Flat':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Flat'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Oval':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Oval'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Curvy':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Curvy'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Square':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Square'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Square'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()
        elif search.data['shape_select'] == 'Rectangle':
            if search.data['type_select'] == 'Opaque':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Opaque'))
                results = qry.all()
            elif search.data['type_select'] == 'Transparent':
                qry = db_session.query(Master).filter(
                    Master.product.contains('Conditioner'), Master.shape.contains('Rectangle'),
                    Master.container_type.contains('Transparent'))
                results = qry.all()

    else:
        qry = db_session.query(Master)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')

    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table = table)

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
    product.product = form.product.data
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
