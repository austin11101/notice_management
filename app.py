from flask import Flask, render_template, request, redirect,url_for ,jsonify
import sqlite3
import logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



app = Flask(__name__, template_folder ='template')
DATABASE ="noticedb.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory =sqlite3.Row
    logging.info("Connected to database successfully")
    return conn 
    
   

@app.route('/')
def index():
    return render_template('index.html')



def init_db():
    with sqlite3.connect('noticedb.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NoticeOfCuratorAndTutor (
                NoticeID INTEGER  AUTOINCREMENT PRIMARY KEY,
                noticeLanguage RADIO,
                province TEXT,
                estateNumber TEXT,
                PersonType RADIO,
                FirstNames TEXT,
                Surname TEXT,
                homeAddress TEXT, 
                curatorTutorType RADIO,           
                curatorTutorName TEXT,
                curatorTutorAddress TEXT,
                appointmentTermination RADIO,
                fromDate DATE,
                mastersOffice TEXT,
                advertiserName TEXT,
                advertiserAddress TEXT,
                advertiserEmail EMAIL,
                advertiserTelephone TEL,
                DateSubmitted DATE,
                publicationDate DATE 
                       
            )
        ''')
        logging.info("Table created succesffully")
        conn.commit()
        conn.close()

       



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

    try:
        with sqlite3.connect('noticedb.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO NoticeOfCuratorAndTutor (
                    noticeLanguage, province, estateNumber, PersonType, FirstNames, Surname, homeAddress, curatorTutorType,
                    curatorTutorName, curatorTutorAddress, appointmentTermination, fromDate, mastersOffice, advertiserName,
                    advertiserAddress, advertiserEmail, advertiserTelephone, DateSubmitted, publicationDate
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', data)
            conn.commit()

            logging.info('record added successfully')
    except Exception as e:
        logging.error(f'Error submitting form: {str(e)}')

    return redirect('/')


@app.route('/visualize', methods=["GET"])
def visualize():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NoticeID,noticeLanguage,province,estateNumber ,PersonType,FirstNames ,Surname, homeAddress,curatorTutorType,curatorTutorName,curatorTutorAddress ,appointmentTermination,fromDate,mastersOffice ,advertiserName,advertiserAddress,advertiserEmail,advertiserTelephone ,DateSubmitted ,publicationDate FROM NoticeOfCuratorAndTutor')
    notices = cursor.fetchall()
    conn.close()

    logging.info('Info viewing submitted successfully')
    return render_template('visualize.html', notices=notices)



@app.route('/delete/<int:NoticeID>', methods=['DELETE' ,'GET','POST'])
def delete_entry(NoticeID):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM NoticeOfCuratorAndTutor WHERE NoticeID = ?", (NoticeID,))
    conn.commit()
    conn.close()
    logging.info('Record deleted')
    return redirect('/visualize')
 

   


if __name__ == '__main__':

    app.run(debug=True)
    app.run()
    app.run(debug = True)
    
    
    


