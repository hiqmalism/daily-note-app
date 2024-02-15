from flask import Flask, render_template, request, redirect, url_for
from models import Activity
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY'] = '@123456&*()'

@app.route('/')
def index():
    model = Activity()
    count_rutin = model.countRutin()
    count_rencana = model.countRencana()
    count_tugas = model.countTugas()
    undone_rutin = model.undoneRutin()
    undone_rencana = model.undoneRencana()
    undone_tugas = model.undoneTugas()
    return render_template('index.html', count_rutin=count_rutin, count_rencana=count_rencana, count_tugas=count_tugas, undone_rutin=undone_rutin, undone_rencana=undone_rencana, undone_tugas=undone_tugas)
    
@app.route('/insert_rutin', methods = ['GET', 'POST'])
def insert_rutin():
    if request.method == 'POST':
        aktivitas = request.form['aktivitas']
        tanggal = request.form['tanggal']
        waktu = request.form['waktu']
        data = (aktivitas, tanggal, waktu)
        model = Activity()
        model.insertRutin(data)
        return redirect(url_for('rutin'))
    else:
        return render_template('rutin.html')
    
@app.route('/insert_rencana', methods = ['GET', 'POST'])
def insert_rencana():
    if request.method == 'POST':
        aktivitas = request.form['aktivitas']
        datetime = request.form['datetime']
        prioritas = request.form['prioritas']
        data = (aktivitas, datetime, prioritas)
        model = Activity()
        model.insertRencana(data)
        return redirect(url_for('rencana'))
    else:
        return render_template('rencana.html')
    
@app.route('/insert_tugas', methods = ['GET', 'POST'])
def insert_tugas():
    if request.method == 'POST':
        aktivitas = request.form['aktivitas']
        datetime = request.form['datetime']
        status = request.form['status']
        data = (aktivitas, datetime, status)
        model = Activity()
        model.insertTugas(data)
        return redirect(url_for('tugas'))
    else:
        return render_template('tugas.html')
    


@app.route('/finishTugas/<no>')
def finishTugas(no):
    model = Activity()
    data = model.getTugasDB(no)
    return render_template('tugas.html', data=data)

@app.route('/tugas_process', methods = ['GET', 'POST'])
def tugas_process():
    no = request.form['no']
    status = request.form['status']
    data = (status,no)
    model = Activity()
    model.finishTugas(data)
    return redirect(url_for('tugas'))

@app.route('/delete_rutin/<no>')
def delete_rutin(no):
    model = Activity()
    model.deleteRutin(no)
    return redirect(url_for('rutin'))

@app.route('/delete_rencana/<no>')
def delete_rencana(no):
    model = Activity()
    model.deleteRencana(no)
    return redirect(url_for('rencana'))

@app.route('/delete_tugas/<no>')
def delete_tugas(no):
    model = Activity()
    model.deleteTugas(no)
    return redirect(url_for('tugas'))

@app.route('/rutin')
def rutin():
    model = Activity()
    container = []
    container = model.selectRutin()
    return render_template('rutin.html', container=container)

@app.route('/rencana')
def rencana():
    model = Activity()
    container = []
    container = model.selectRencana()
    return render_template('rencana.html', container=container)

@app.route('/tugas')
def tugas():
    model = Activity()
    container = []
    container = model.selectTugas()
    return render_template('tugas.html', container=container)

@app.route('/rekap')
def rekap():
    model = Activity()
    harian_rutin = model.harianRutin()
    mingguan_rutin = model.mingguanRutin()
    bulanan_rutin = model.bulananRutin()
    harian_rencana = model.harianRencana()
    mingguan_rencana = model.mingguanRencana()
    bulanan_rencana = model.bulananRencana()
    harian_tugas = model.harianTugas()
    mingguan_tugas = model.mingguanTugas()
    bulanan_tugas = model.bulananTugas()
    return render_template('rekap.html', harian_tugas=harian_tugas, mingguan_tugas=mingguan_tugas, bulanan_tugas=bulanan_tugas, harian_rutin=harian_rutin, mingguan_rutin=mingguan_rutin, bulanan_rutin=bulanan_rutin, harian_rencana=harian_rencana, mingguan_rencana=mingguan_rencana, bulanan_rencana=bulanan_rencana)

if __name__ == '__main__' :
    app.run(debug=True)