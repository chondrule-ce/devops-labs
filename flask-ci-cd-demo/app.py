from flask import Flask 

# Use __name__ as the import_name to let Flask know the location of the application
app = Flask(__name__)

# Use the @ decorator to tell Flask to call the 'CICD_demo' func when access the url '/'
# '/' represents the root path
@app.route("/")
def CICD_demo():
    return "DevOps CI/CD demo"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)