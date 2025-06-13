from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/products/<product_name>')
def product_detail(product_name):
    product_data = {
        'shampoo': {
            'name': 'Hotel Shampoo',
            'description': 'A refreshing, lightly scented shampoo perfect for hotel guests.',
            'image': 'shampoo.jpg'
        },
        'bodywash': {
            'name': 'Luxury Body Wash',
            'description': 'Gentle on skin, with a luxurious lather.',
            'image': 'bodywash.jpg'
        },
        'soap': {
            'name': 'Natural Soap Bar',
            'description': 'Handmade soap bar with essential oils.',
            'image': 'soap.jpg'
        },
        'robe': {
            'name': 'Plush Bathrobe',
            'description': 'Cozy, high-thread count robe for premium comfort.',
            'image': 'robe.jpg'
        }
    }
    product = product_data.get(product_name)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        abort(404)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/<service_name>')
def service_detail(service_name):
    service_data = {
        'amenity-packaging': {
            'name': 'Custom Amenity Packaging',
            'description': 'Elevate your brand with bespoke packaging for every room essential.',
            'features': ['Eco-friendly options', 'Custom designs', 'Hotel logo branding'],
            'image': 'amenity_packaging.jpg'
        },
        'bulk-supply': {
            'name': 'Bulk Supply Solutions',
            'description': 'Cost-effective bulk deliveries of your preferred hotel products.',
            'features': ['Scheduled deliveries', 'Warehouse support', 'Inventory management'],
            'image': 'bulk_supply.jpg'
        },
        'fragrance-customization': {
            'name': 'Fragrance Customization',
            'description': 'Signature scents tailored to reflect your brand identity.',
            'features': ['Custom blends', 'Aromatherapy options', 'Long-lasting effect'],
            'image': 'fragrance_customization.jpg'
        },
        'laundry-service': {
            'name': 'Laundry & Linen Care',
            'description': 'Professional care for your luxury linens and bathrobes.',
            'features': ['Timely pickup & delivery', 'Stain treatment', 'Softener finish'],
            'image': 'laundry_service.jpg'
        },
        'eco-packaging': {
            'name': 'Eco-Friendly Packaging',
            'description': 'Sustainable, biodegradable alternatives to reduce your footprint.',
            'features': ['Biodegradable', 'Minimal design', 'Custom print'],
            'image': 'eco_packaging.jpg'
        },
        'branding-consulting': {
            'name': 'Brand Consulting',
            'description': 'Hospitality branding strategies from experts in guest experience.',
            'features': ['Visual branding', 'Digital strategy', 'Market analysis'],
            'image': 'branding_consulting.jpg'
        }
    }
    service = service_data.get(service_name)
    if service:
        return render_template('service_detail.html', service=service)
    else:
        abort(404)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host='0.0.0.0', port=port)
