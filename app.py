from flask import Flask, request, redirect, url_for, jsonify
from urllib.parse import quote
from Controller import MahasiswaController, PerguruanTinggiController, ProdiController, HitController, DosenController

app = Flask(__name__)

@app.route("/")
def home():
  return {
    'owner': [
      {
      'name'   : 'Ridwan Halim',
      'address': 'Boyolali, Central Java',
      'my_wife': 'Hafidhah Afkariana'
      }
    ],
    'social_media': [
      {
      'instagram': 'https://www.instagram.com/ridwaanhall',
      'facebook' : 'https://www.facebook.com/ridwaanhall',
      'tiktok'   : 'https://www.tiktok.com/@ridwaanhall',
      'twitter'  : 'https://twitter.com/ridwaanhall',
      'threads'  : 'https://www.threads.net/@ridwaanhall',
      'linkedin' : 'https://www.linkedin.com/in/ridwaanhall',
      'github'   : 'https://github.com/ridwaanhall',
      'replit'   : 'https://replit.com/@ridwaanhall',
      'telegram' : 'https://t.me/ridwaanhall'
      }
    ],
    'routes_available': [
      {
        'url_base' : 'https://data-mahasiswa.ridwaanhall.repl.co',
        'route': '/hit_mhs',
        'note': 'this route for search mahasiswa data. such as name, etc.'
      },
      {
        
      },
      {
        
      },
      {
        
      }
    ]
  }

@app.route('/hit_mhs', methods=['GET', 'POST'])
def hit_mhs():
  if request.method == 'POST':
    # Get the input from the form
    mahasiswa = request.form['mahasiswa']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('hit_mhs_detail', mahasiswa=mahasiswa))
  else:
    # Display the input form
    return '''
    <p>bisa input NIM, nama, nama + kampus, dll.</p>
    <form method="post" action="/hit_mhs">
      <label for="mahasiswa">Mahasiswa:</label>
      <input type="text" id="mahasiswa" name="mahasiswa" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/hit_mhs/<string:mahasiswa>', methods=['GET'])
def hit_mhs_detail(mahasiswa):
  encoded_mahasiswa = quote(mahasiswa)
  data = MahasiswaController.hit_mhs(encoded_mahasiswa)
  return jsonify(data)

@app.route('/data_mahasiswa', methods=['GET', 'POST'])
def data_mahasiswa_home():
  if request.method == 'POST':
    # Get the input from the form
    id_mahasiswa = request.form['id_mahasiswa']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_mahasiswa', id_mahasiswa=id_mahasiswa))
  else:
    # Display the input form
    return '''
    <p>input id mahasiswa</p>
    <form method="post" action="/data_mahasiswa">
      <label for="mahasiswa">id mahasiswa:</label>
      <input type="text" id="id_mahasiswa" name="id_mahasiswa" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_mahasiswa/<string:id_mahasiswa>', methods=['GET'])
def data_mahasiswa(id_mahasiswa):
  data = MahasiswaController.data_mahasiswa(id_mahasiswa)
  return jsonify(data)

@app.route('/load_pt', methods=['GET'])
def load_pt():
  data = PerguruanTinggiController.load_pt()
  return jsonify(data)

@app.route('/data_pt', methods=['GET', 'POST'])
def data_pt():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt">
      <label for="link_pt">Mahasiswa:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt/<string:link_pt>', methods=['GET'])
def data_pt_detail(link_pt):
  data = PerguruanTinggiController.data_pt(link_pt)
  return jsonify(data)

@app.route('/data_pt_prodi', methods=['GET', 'POST'])
def data_pt_prodi():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_prodi_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_prodi">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_prodi/<string:link_pt>', methods=['GET'])
def data_pt_prodi_detail(link_pt):
    data = PerguruanTinggiController.data_pt_prodi(link_pt)
    return jsonify(data)

@app.route('/data_pt_jumlah', methods=['GET', 'POST'])
def data_pt_jumlah():
  if request.method == 'POST':
    # Get the input from the form
    link_pt = request.form['link_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('data_pt_jumlah_detail', link_pt=link_pt))
  else:
    # Display the input form
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_jumlah">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_jumlah/<string:link_pt>', methods=['GET'])
def data_pt_jumlah_detail(link_pt):
    data = PerguruanTinggiController.data_pt_jumlah(link_pt)
    return jsonify(data)

@app.route('/data_pt_dosen', methods=['GET', 'POST'])
def data_pt_dosen():
  if request.method == 'POST':
    link_pt = request.form['link_pt']
    return redirect(url_for('data_pt_dosen_detail', link_pt=link_pt))
  else:
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/data_pt_dosen">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/data_pt_dosen/<string:link_pt>', methods=['GET'])
def data_pt_dosen_detail(link_pt):
  data = PerguruanTinggiController.data_pt_dosen(link_pt)
  return jsonify(data)

@app.route('/stat_pt', methods=['GET', 'POST'])
def stat_pt():
  if request.method == 'POST':
    link_pt = request.form['link_pt']
    return redirect(url_for('stat_pt_detail', link_pt=link_pt))
  else:
    return '''
    <p>input ID perguruan tinggi / id_sp pada load_pt</p>
    <form method="post" action="/stat_pt">
      <label for="link_pt">ID:</label>
      <input type="text" id="link_pt" name="link_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/stat_pt/<string:link_pt>', methods=['GET'])
def stat_pt_detail(link_pt):
  data = PerguruanTinggiController.stat_pt(link_pt)
  return jsonify(data)

@app.route('/load_prodi', methods=['GET'])
def load_prodi():
  data = ProdiController.load_prodi()
  return jsonify(data)

# search prodi using id_sp (pt)
@app.route('/load_prodi/<string:id_sp>', methods=['GET'])
def load_detail_prodi(id_sp):
  data = ProdiController.load_detail_prodi(id_sp)
  return jsonify(data)

@app.route('/data_prodi/<string:link_prodi>', methods=['GET'])
def data_prodi(link_prodi):
  data = ProdiController.data_prodi(link_prodi)
  return jsonify(data)

@app.route('/data_dosen/<string:link_dosen>', methods=['GET'])
def data_dosen(link_dosen):
  data = DosenController.data_dosen(link_dosen)
  return jsonify(data)

@app.route('/hit', methods=['GET', 'POST'])
def hit():
  if request.method == 'POST':
    # Get the input from the form
    dsn_prodi_pt = request.form['dsn_prodi_pt']
    # Redirect to the route with the input as a parameter
    return redirect(url_for('hit_dsn_prodi_pt_detail', dsn_prodi_pt=dsn_prodi_pt))
  else:
    # Display the input form
    return '''
    <p>dosen, pt, prodi.</p>
    <form method="post" action="/hit">
      <label for="dsn_prodi_pt">dosen pt prodi:</label>
      <input type="text" id="dsn_prodi_pt" name="dsn_prodi_pt" required>
      <input type="submit" value="OK">
    </form>
    '''

@app.route('/hit/<string:dsn_prodi_pt>', methods=['GET'])
def hit_dsn_prodi_pt_detail(dsn_prodi_pt):
  # Encode the dsn_prodi_pt parameter to handle special characters
  encoded_dsn_prodi_pt = quote(dsn_prodi_pt)
  # Use the encoded_dsn_prodi_pt as input for the dsn_prodi_ptController.hit_mhs() function
  data = HitController.hit(encoded_dsn_prodi_pt)
  return jsonify(data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)