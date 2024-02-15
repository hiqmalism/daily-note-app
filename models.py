import pymysql
import config

db = cursor = None

class Activity:
    def __init__(self, no=None, jenis_kegiatan=None, keterangan=None, tanggal=None, waktu=None):
        self.no = no
        self.jenis_kegiatan = jenis_kegiatan
        self.keterangan = keterangan
        self.tanggal = tanggal
        self.waktu = waktu
        
    def openDB(self):
        global db, cursor
        db = pymysql.connect(host = config.DB_HOST, user = config.DB_USER, password = config.DB_PASSWORD, database = config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()
    
    def insertRutin(self, data):
        self.openDB()
        cursor.execute("insert into rutin(aktivitas, tanggal, waktu) values('%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def insertRencana(self, data):
        self.openDB()
        cursor.execute("insert into rencana(aktivitas, datetime, prioritas) values('%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()

    def insertTugas(self, data):
        self.openDB()
        cursor.execute("insert into tugas(aktivitas, datetime, status) values('%s', '%s', '%s')" % data)
        db.commit()
        self.closeDB()
    
    def getTugasDB(self, no):
        self.openDB()
        cursor.execute("select * from tugas where no='%s'" % no)
        data = cursor.fetchone()
        return data

    def finishTugas(self, data):
        self.openDB()
        cursor.execute("update tugas set status=%s where no=%s" % data)
        db.commit()
        self.closeDB()

    def deleteRutin(self, no):
        self.openDB()
        cursor.execute("delete from rutin where no=%s" % no)
        db.commit()
        self.closeDB()

    def deleteRencana(self, no):
        self.openDB()
        cursor.execute("delete from rencana where no=%s" % no)
        db.commit()
        self.closeDB()

    def deleteTugas(self, no):
        self.openDB()
        cursor.execute("delete from tugas where no=%s" % no)
        db.commit()
        self.closeDB()

    def selectRutin(self):
        self.openDB()
        cursor.execute("select no, aktivitas, tanggal, waktu from rutin order by tanggal desc, waktu desc")
        container = []
        for no, aktivitas, tanggal, waktu in cursor.fetchall():
            container.append((no, aktivitas, tanggal, waktu))
        self.closeDB()
        return container
    
    def selectRencana(self):
        self.openDB()
        cursor.execute("select no, aktivitas, datetime, prioritas from rencana order by datetime desc")
        container = []
        for no, aktivitas, datetime, prioritas in cursor.fetchall():
            container.append((no, aktivitas, datetime, prioritas))
        self.closeDB()
        return container
    
    def selectTugas(self):
        self.openDB()
        cursor.execute("select no, aktivitas, datetime, status from tugas order by status, datetime desc")
        container = []
        for no, aktivitas, datetime, status in cursor.fetchall():
            container.append((no, aktivitas, datetime, status))
        self.closeDB()
        return container
    

    def countRutin(self):
        self.openDB()
        cursor.execute("select count(*) as hitung from rutin where tanggal>curdate() and waktu>curtime()")
        container =  cursor.fetchone()
        self.closeDB()
        return container
    
    def countRencana(self):
        self.openDB()
        cursor.execute("select count(*) as hitung from rencana where datetime>current_timestamp()")
        container =  cursor.fetchone()
        self.closeDB()
        return container
    
    def countTugas(self):
        self.openDB()
        cursor.execute("select count(*) as hitung from tugas where status=0")
        container =  cursor.fetchone()
        self.closeDB()
        return container
    
    def harianRutin(self):
        self.openDB()
        cursor.execute("select * from rutin where tanggal = curdate() and waktu < curtime() order by tanggal, waktu;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def mingguanRutin(self):
        self.openDB()
        cursor.execute("select * from rutin where tanggal >= date_sub(current_timestamp(), interval 1 week) order by tanggal, waktu;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def bulananRutin(self):
        self.openDB()
        cursor.execute("select * from rutin where date_format(tanggal, '%Y-%m') = date_format(curdate(), '%Y-%m') order by tanggal, waktu;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def harianRencana(self):
        self.openDB()
        cursor.execute("select * from rencana where date(datetime) = curdate() order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def mingguanRencana(self):
        self.openDB()
        cursor.execute("select * from rencana where datetime >= date_sub(current_timestamp(), interval 1 week) order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def bulananRencana(self):
        self.openDB()
        cursor.execute("select * from rencana where date_format(datetime, '%Y-%m') = date_format(curdate(), '%Y-%m') order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container

    def harianTugas(self):
        self.openDB()
        cursor.execute("select * from tugas where date(datetime) = curdate() and status=1 order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def mingguanTugas(self):
        self.openDB()
        cursor.execute("select * from tugas where datetime >= date_sub(current_timestamp(), interval 1 week) and status=1 order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def bulananTugas(self):
        self.openDB()
        cursor.execute("select * from tugas where date_format(datetime, '%Y-%m') = date_format(curdate(), '%Y-%m') and status=1 order by datetime desc;")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def undoneRutin(self):
        self.openDB()
        cursor.execute("select * from rutin where tanggal>curdate() and waktu>curtime()")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def undoneRencana(self):
        self.openDB()
        cursor.execute("select * from rencana where datetime>current_timestamp()")
        container = cursor.fetchall()
        self.closeDB()
        return container
    
    def undoneTugas(self):
        self.openDB()
        cursor.execute("select * from tugas where status=0")
        container = cursor.fetchall()
        self.closeDB()
        return container