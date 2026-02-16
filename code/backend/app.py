from flask import Flask, request, jsonify, send_from_directory


import os
import boto3

app = Flask(__name__)



UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def serve_index():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("../frontend", path)

@app.route("/upload", methods=["POST"])
def upload_product():
    name = request.form.get("name")
    price = request.form.get("price")
    stock = request.form.get("stock")
    description = request.form.get("description")
    image = request.files.get("image")

    if not image:
        return jsonify({"message": "No se recibió imagen"}), 400

    

    # Guardado local temporal
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)




    image.save(image_path)

    # -------------------------
    # Subir imagen a S3
    # -------------------------
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket_name = "datos7533532"

    try:
        s3.upload_file(
            image_path,
            bucket_name,
            image.filename
        )
        print("Imagen subida a S3 correctamente")

    except Exception as e:
        print("Error al subir a S3:", e)
        import traceback
        print("ERROR S3:")
        traceback.print_exc()
        return jsonify({"message": "Error al subir imagen a S3"}), 500

    print("Producto recibido:")
    print(name, price, stock, description)

    return jsonify({
        "message": "Producto guardado correctamente en EC2 y S3"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
