from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "image": "https://placehold.co/600x400?text=Laptop"
    },
    {
        "id": 2,
        "name": "Phone",
        "image": "https://placehold.co/600x400?text=Phone"
    },
    {
        "id": 3,
        "name": "Shoes",
        "image": "https://placehold.co/600x400?text=Shoes"
    }
]

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Product Catalog</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                text-align: center;
            }

            .container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                max-width: 900px;
                margin: auto;
            }

            .card {
                background: white;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                transition: 0.2s;
                cursor: pointer;
            }

            .card:hover {
                transform: scale(1.03);
            }

            .card img {
                width: 100%;
                height: 150px;
                object-fit: cover;
            }

            .card h3 {
                padding: 10px;
                margin: 0;
                text-align: center;
            }
        </style>
    </head>

    <body>
        <h1>Product Catalog</h1>
        <div class="container" id="products"></div>

        <script>
            fetch('/api/products')
                .then(res => res.json())
                .then(data => {
                    const container = document.getElementById('products');

                    data.forEach(p => {
                        const card = document.createElement('div');
                        card.className = 'card';

                        card.innerHTML = `
                            <img src="${p.image}" />
                            <h3>${p.name}</h3>
                        `;

                        card.onclick = () => {
                            window.location.href = '/product/' + p.id;
                        };

                        container.appendChild(card);
                    });
                });
        </script>
    </body>
    </html>
    """

@app.route("/product/<int:id>")
def product(id):
    product = next((p for p in products if p["id"] == id), None)

    if not product:
        return "<h2 style='text-align:center;'>Product not found</h2>"

    return f"""
    <html>
    <body style="font-family:Arial; text-align:center; padding:40px;">
        <h1>{product['name']}</h1>
        <img src="{product['image']}" style="width:300px; border-radius:10px;" />
        <br><br>
        <button onclick="window.location.href='/'">Back</button>
    </body>
    </html>
    """

@app.route("/api/products")
def api_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
