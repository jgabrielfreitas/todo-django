from flask import Flask
app = Flask(__name__)

def get_file_content(file_name):
    content = ""
    responses_path = "./responses/{0}".format(file_name)
    with open(responses_path, 'r') as content_file:
        content = content_file.read()
    return content

@app.route("/todo")
def todo():
    return get_file_content('todo-list.json')

if __name__ == "__main__":
    app.run(debug=True)
