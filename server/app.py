from flask import Flask, jsonify, request

app = Flask(__name__)


inventory = [
    {
        "id": 1,
        "product_name": "Organic Almond Milk",
        "brands": "Silk",
        "ingredients_text": "Filtered water, almonds"
    }
]


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data or "product_name" not in data:
        return jsonify({"error": "product_name is required"}), 400

    new_item = {
        "id": len(inventory) + 1,
        "product_name": data["product_name"],
        "brands": data.get("brands", ""),
        "ingredients_text": data.get("ingredients_text", "")
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:
            item["product_name"] = data.get("product_name", item["product_name"])
            item["brands"] = data.get("brands", item["brands"])
            item["ingredients_text"] = data.get("ingredients_text", item["ingredients_text"])

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return "", 204

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)