from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import (
    get_all_clothing_items,
    get_filtered_clothing_items,
    get_cart_items,
    add_to_cart,
    get_cart_total_price,
    remove_from_cart,
    clear_cart
)

# Midlertidig kunde-id (indtil login-system)
CURRENT_CUSTOMER_ID = 1

@app.route('/')
def home():
    return redirect(url_for('browse'))

@app.route('/browse')
def browse():
    size = request.args.get('size')
    color = request.args.get('color')
    type_ = request.args.get('type')
    sort_by = request.args.get('sort_by')
    sort_direction = request.args.get('sort_direction','asc')

    # Treat 'Other' as None, meaning no filter applied for that field
    if size == "Other":
        size = None
    if color == "Other":
        color = None
    if type_ == "Other":
        type_ = None

    items = get_filtered_clothing_items(size=size, color=color, type = type_, sort_by = sort_by, sort_direction = sort_direction)
    allItems = get_all_clothing_items()
    print(f"Items found: {len(items)}")
    print(f"All clothing items found: {len(allItems)}")
    return render_template('browse.html', items=items, selected_size=size, selected_color=color, selected_type = type_, selected_sort_by = sort_by, selected_sort_direction = sort_direction)

@app.route('/add/<int:item_id>')
def add(item_id):
    add_to_cart(1, item_id)
    return redirect('/browse')

@app.route('/add-to-cart/<int:item_id>', methods=['GET', 'POST'])
def add_to_cart_route(item_id):
    add_to_cart(CURRENT_CUSTOMER_ID, item_id)
    flash("Item added to cart.")
    return redirect(url_for('browse'))


@app.route('/cart')
def cart():
    items = get_cart_items(CURRENT_CUSTOMER_ID)
    total = get_cart_total_price(CURRENT_CUSTOMER_ID)
    return render_template('cart.html', items=items, total=total)

@app.route('/remove/<int:cart_item_id>')
def remove(cart_item_id):
    from app.models import remove_from_cart
    remove_from_cart(cart_item_id)
    return redirect('/cart')

@app.route('/checkout')
def checkout():
    items = get_cart_items(CURRENT_CUSTOMER_ID)
    total = get_cart_total_price(CURRENT_CUSTOMER_ID)
    return render_template('checkout.html', items=items, total=total)

@app.route('/complete-checkout', methods=['POST'])
def complete_checkout():
    clear_cart(CURRENT_CUSTOMER_ID)
    return render_template('confirmation.html')