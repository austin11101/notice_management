from flask import Flask, render_template, request, redirect,url_for ,jsonify
import sqlite3

app = Flask(__name__, template_folder ='template')
DATABASE ="noticedb.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory =sqlite3.Row
    print("Connected to database successfully")
    return conn 
    
   

@app.route('/')
def index():
    return render_template('index.html')



def init_db():
    with sqlite3.connect('noticedb.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NoticeOfCuratorAndTutor (
                NoticeID INTEGER PRIMARY KEY AUTOINCREMENT,
                noticeLanguage RADIO,
                province TEXT,
                estateNumber TEXT,
                PersonType RADIO,
                curatorTutorName TEXT,
                curatorTutorSurname TEXT,
                curatorTutorAddress TEXT,
                appointmentTermination RADIO,
                fromDate DATE,
                publicationDate DATE,
                mastersOffice TEXT,
                advertiserName TEXT,
                advertiserAddress TEXT,
                advertiserEmail EMAIL,
                advertiserTelephone TEL,
                submitionDate DATE,
                publicationDate DATE 
                       
            )
        ''')
        print("Table created succesffully")
        conn.commit()
        conn.close()

        init_db()



@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = (
        
       
        request.form['noticeLanguage'],
        request.form['province'],
        request.form['estateNumber'],
        request.form['PersonType'], 
        request.form['FirstNames'],
        request.form['Surname'],
        request.form['homeAddress'], 
        request.form['curatorTutorType'],
        request.form['curatorTutorName'],
        request.form['curatorTutorAddress'],
        request.form['appointmentTermination'],
        request.form['fromDate'],
        request.form['mastersOffice'],
        request.form['advertiserName'],
        request.form['advertiserAddress'],
        request.form['advertiserEmail'],
        request.form['advertiserTelephone'],
        request.form['DateSubmitted'],
        request.form['publicationDate']
    )

    with sqlite3.connect('noticedb.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO NoticeOfCuratorAndTutor (
                noticeLanguage, province, estateNumber,PersonType,FirstNames,Surname,homeAddress,curatorTutorType,curatorTutorName,curatorTutorAddress,appointmentTermination, 
                fromDate,mastersOffice,advertiserName,advertiserAddress,advertiserEmail,advertiserTelephone,DateSubmitted,publicationDate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', data)
        conn.commit()

    return redirect('/')


@app.route('/visualize', methods=["GET"])
def visualize():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NoticeID,noticeLanguage,province,estateNumber ,PersonType,FirstNames ,Surname, homeAddress,curatorTutorType,curatorTutorName,curatorTutorAddress ,appointmentTermination,fromDate,mastersOffice ,advertiserName,advertiserAddress,advertiserEmail,advertiserTelephone ,DateSubmitted ,publicationDate FROM NoticeOfCuratorAndTutor')
    notices = cursor.fetchall()
    conn.close()

    return render_template('visualize.html', notices=notices)

@app.route('/delete/int:NoticeID>',methods=['POST'])
def delete_entry(NoticeID):
    conn =get_db_connection
    curso =conn.curso()
    curso.execute("NoticeOfCuratorAndTutor WHERE NoticeID =?", (NoticeID,))
    conn.commit()
    conn.close()

    return redirect('visualize')


if __name__ == '__main__':

    app.run(debug=True)
    app.run()
    app.run(debug = True)
    


