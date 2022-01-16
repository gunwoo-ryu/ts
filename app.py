import os
import pandas as pd

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH= os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000)

dropzone = Dropzone(app)
@app.route('/',methods=['POST','GET'])
def upload():
    if request.method == 'POST': # 파일 전송 받으면
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'],f.filename)) # 파일을 지정한 경로에 저장
        file_path = os.path.join(app.config['UPLOADED_PATH'],f.filename) # 파일이 저장된 경로
        file_data = pd.read_csv(file_path) # 파일 읽어들임
        print(file_data)
        os.remove(file_path) # 계산 끝나면 파일 삭제해서 개인정보 보호

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)