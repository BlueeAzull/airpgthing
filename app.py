import os
import sys

# remember to delete all this shit when hosting the code like a real person
def cool_import(name):
    basedir = os.path.dirname(__file__)
    deps_dir = os.path.join(basedir, 'dependencies')
    if deps_dir not in sys.path:
        sys.path.insert(0, deps_dir)
    return __import__(name)

f = cool_import('flask')

yo_im_a_var = "FUCK PIP!!!!!!!!"

# fun part begins here

app = f.Flask(__name__)

@app.route('/')

def home():
    return f.render_template("index.html", hate=yo_im_a_var)

if __name__ == "__main__":
    app.run(debug=True)