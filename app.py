from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    form_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Webhook Form</title>
    </head>
    <body>
        <h1>Webhook Test</h1>
        <form action="/webhook" method="post">
            <label for="message">Message:</label>
            <input type="text" id="message" name="message" required>
            <button type="submit">Send</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(form_html)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':
        return jsonify({"message": "This is the webhook endpoint. Use POST to send data."})

    data = request.form.to_dict()  
    message = data.get('message', 'No message found')
    print(f"Received message: {message}")  
    return jsonify({"status": "success", "received_message": message}), 200

if __name__ == '__main__':
    app.run(port=5000)
