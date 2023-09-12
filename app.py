from flask import Flask, request, redirect, url_for, jsonify
from urllib.parse import quote
from Controller import MahasiswaController, PerguruanTinggiController, ProdiController, HitController, DosenController

app = Flask(__name__)


@app.route("/")
def home():
  return {
    'how_to_use': [{
      'text': 'you can use this API from link in routes_available.'
    }],
    'owner': [{
      'name': 'ridwaanhall',
      'address': 'Sleman, DIY',
      'my_love': 'Afida'
    }],
    'social_media': [{
      'instagram': 'https://www.instagram.com/ridwaanhall',
      'facebook': 'https://www.facebook.com/ridwaanhall',
      'tiktok': 'https://www.tiktok.com/@ridwaanhall',
      'twitter': 'https://twitter.com/ridwaanhall',
      'threads': 'https://www.threads.net/@ridwaanhall',
      'linkedin': 'https://www.linkedin.com/in/ridwaanhall',
      'github': 'https://github.com/ridwaanhall',
      'replit': 'https://replit.com/@ridwaanhall',
      'telegram': 'https://t.me/ridwaanhall'
    }],
    'routes_available': [{
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/hit_mhs',
      'z_note':
      'this route for search of list mahasiswa data. By input a text. available to input by number of student, university, name, or the combination of number, university, and name. after enter an input, url will redirect to this url /hit_mhs/<string:mahasiswa>'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/hit_mhs/<string:mahasiswa>',
      'z_note':
      'this route for show list result after input the text from route /hit_mhs. the output is a json data (text: name, nim, pt, prodi. website-link:url/id)'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_mahasiswa',
      'z_note':
      'this route for search detail of mahasiswa using id. will redirect to /data_mahasiswa/<string:id_mahasiswa>'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_mahasiswa/<string:id_mahasiswa>',
      'z_note':
      'this route for show detail of mahasiswa by id. the json data is datastatuskuliah : id_smt, nm_stat_mhs, sks_smt. datastudi : id_smt, kode_mk, nilai_huruf, nm_mk, sks_mk. dataumum : jk, ket_keluar, link_pt, link_prodi, mulai_smt, namajenjang, namaprodi, namapt, nipd, nm_jns_daftar, nm_pd, nm_prodi_asal, n_pt_asal, no_seri_ijazah, reg_pd, ret_prof, tgl_keluar.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/load_pt',
      'z_note':
      'this route for show list if pt. id_sp, kode_pt, nama_pt.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt',
      'z_note':
      'this route using for input data id of pt. and redirect to /data_pt/<string:link_pt>.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt/<string:link_pt>',
      'z_note':
      'this route using for detail of pt. json data such as akreditasi_list : akreditasi, tgl_akreditasi, tgl_berlaku. bujur, email, id_sp, internet, jln, kode_pos, laporatorium, lintang, listrik, luas_tanah, nama_rektor, nama_wil, nm_lemb, no_fax, no_tel, npsn, perpustakaan, ruang_kelas, sk_pendirian_sp, stat_sp, tgl_perdiri, tgl_sk_pendirian_sp, website.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_prodi',
      'z_note':
      'this route for search detail prodi of pt by id of pt. will redirect to /data_pt_prodi/<string:link_pt>.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_prodi/<string:link_pt>',
      'z_note':
      'this route for json data. such as akreditasi, id_sms, jenjang, kode_prodi, nm_lemb, rasio_list : dosen, dosenNidk, dosenNidn, mahasiswa, semester. stat_prodi.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_jumlah',
      'z_note':
      'this route for search statistic from pt by id. will redirect to /data_pt_jumlah/<string:link_pt>'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_jumlah/<string:link_pt>',
      'z_note':
      'this route for json data of statistic by id. such as jumlah_bidangilmu, jumlah_fakultas, jumlah_prodi, jumlah_prodi_akreditasi : A, B, Baik sekali, C, unggul. rasio_list.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_dosen',
      'z_note':
      'this route for search statistic of dosen from pt by id. will redirect to /data_pt_dosen/<string:link_pt>.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_pt_dosen/<string:link_pt>',
      'z_note':
      'this route for json data. such as tetap : jumlah_dosen_jabatan, Categories, series, data, name, jumlah_dosen_jenis_kelamin, L, P, jumlah_dosen_jenjang, jumlah_dosen_registrasi, tidak_tetap.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/stat_pt',
      'z_note':
      'this route for search statistic data of pt. will redirect to /stat_pt/<string:link_pt>.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/stat_pt/<string:link_pt>',
      'z_note':
      'this route for json data statistic of pt. such as id, rasio : nm_jenj_didik, total_kurang_6, total_lebih_, total_semua. rata_lama_studi : nm_jenj_didik, total_cont, total_years.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/load_prodi',
      'z_note':
      'this route for all list of prodi without filter. such as id_sms, id_sp, kode_prodi, nama_prodi.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/load_prodi/<string:id_sp>',
      'z_note':
      'this route for list of prodi using filter by id_sp. json data is id_sms, id_sp, kode_prodi, nama_prodi.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_prodi/<string:link_prodi>',
      'z_note':
      'this route for list json data of prodi data. such as datadosen : gelar, id, idreg, linkdosen, nama, pendidikan. datadosenrasio : gelar_dosen, id, idreg, jenjang_dosen, jenjang_komebase, linkdosen, nama, nidn, prodi_homebase, pt. datamhs : jml, mulai_smt. detailumum : akreditasi, bujur, capaian, deskripsi, email, id_sms, jln, kode_pos, kode_prodi, kompetensi, linkpt, lintang, misi, , namajenjang, namapt, nm_lemb, no_fax, no_tel, npsn, sk_selenggara, visi. rasio : jmldosen, jmlmhs, kode_program_studi, smt.'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/data_dosen/<string:link_dosen>',
      'z_note':
      'this route for json data of dosen data. such as datamengajar : id_smt, kode_mk, linkpt, namapt, nm_kls, nm_mk. datapendidikan : namajenjang, nm_sp_formal, singkatan_gelar, thn_lulus. dataumum : foto, fungsional, -d_sdm, ikatankerja, jk, linkprodi, linkpt, namaprodi, namapt, nm_sdm, pend_tinggi, statuskeaktifan, tmpt_lahir'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/hit',
      'z_note':
      'this route for search of list pt, dosen, prodi data. By input a text. available to input by all available of data search. after enter an input, url will redirect to this url /hit/<string:dsn_prodi_pt>'
    }, {
      'url_base':
      'https://data-mahasiswa.ridwaanhall.repl.co',
      'route':
      '/hit/<string:dsn_prodi_pt>',
      'z_note':
      'this route for json data detail of data dsn_prodi_pt. such as dosen : name, nidn, pt, prodi. prodi : , pt : pt, npsn, singkatan, alamat, link data'
    }],
    'source':
    'pddikti'
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
    return redirect(
      url_for('hit_dsn_prodi_pt_detail', dsn_prodi_pt=dsn_prodi_pt))
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
  encoded_dsn_prodi_pt = quote(dsn_prodi_pt)
  data = HitController.hit(encoded_dsn_prodi_pt)
  return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
