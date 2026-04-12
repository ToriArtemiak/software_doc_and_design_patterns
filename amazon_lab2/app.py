from flask import Flask, render_template, request, redirect
from data_access.repositories import ProductRepository
from models.models import Product
from database import SessionLocal

app = Flask(__name__)

repo = ProductRepository()


# 🟢 Головна сторінка (показ товарів)
@app.route("/")
def index():
    products = repo.get_products()
    return render_template("index.html", products=products)

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        product = Product(name=name, price=price, quantity=1)

        repo.add_product(product)

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete_product(id):
    session = SessionLocal()

    product = session.query(Product).get(id)
    session.delete(product)
    session.commit()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    session = SessionLocal()
    product = session.query(Product).get(id)

    if request.method == "POST":
        product.name = request.form["name"]
        product.price = request.form["price"]

        session.commit()
        return redirect("/")

    return render_template("edit.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
