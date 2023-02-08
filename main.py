from flask import Flask, request, render_template
from flask_sslify import SSLify
import os

app = Flask(__name__)
sllify = SSLify(app)

def confirm_config_file_exists():
  config_file = 'config.txt'
  if not os.path.exists(config_file):
    with open(config_file, "w") as file:
        file.write("")  # write empty string to create the file

@app.route('/')
def index():
    return '<h1>Welcome to the Configuration Editor</h1><br><br><h2>valid routes:</h2><br><br>POST: /edit_config - ' \
           'writes posted payload as config.txt<br>GET: /edit_config - displays current config and allows editing ' \
           'through form'

@app.route('/edit_config', methods=['GET', 'POST'])
def edit_config():
  config_file = 'config.txt'
  if request.method == 'POST':
      new_config = request.form['config_contents']
      # write new_config to config_file
      with open(config_file, 'w') as file:
          file.write(new_config)
      return 'Config file updated successfully'
  with open(config_file, 'r')   as file:
    config_contents = file.read()
  return render_template('edit_config.html', config_contents=config_contents)

if __name__ == '__main__':
  confirm_config_file_exists()
  app.run(
      host='0.0.0.0',
      debug=True
    )