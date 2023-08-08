from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@sparta.lhdjgj6.mongodb.net/?retryWrites=true&w=majority')
db = client.accountinfo


######## 로딩 페이지 ########
@app.route('/')

def home():
    return render_template('index.html')

######## 입력창 페이지 ########
@app.route('/input.html')
def input():
    return render_template('input.html')

######## 메인 페이지 ########
@app.route('/mainpg.html')
def mainpg():
    return render_template('mainpg.html')

######## 계좌 페이지 ########
@app.route('/account.html')
def account():
    return render_template('account.html')

######## 계좌(카카오) 페이지 ########
@app.route('/account-kakao.html')
def accountkakao():
    return render_template('account-kakao.html')
######## 계좌(국민) 페이지 ########
@app.route('/account-kb.html')
def accountkb():
    return render_template('account-kb.html')
######## 계좌(국민에셋) 페이지 ########
@app.route('/account-asset-kb.html')
def accountassetkb():
    return render_template('account-asset-kb.html')
######## 계좌(미래에셋) 페이지 ########
@app.route('/account-asset-mirae.html')
def accounassetmr():
    return render_template('account-asset-mirae.html')


######## 카드 페이지 ########
@app.route('/card.html')
def card():
    return render_template('card.html')

######## 자동이체 페이지 ########
@app.route('/more.html')
def more():
    return render_template('more.html')

######## 더보기 페이지 ########
@app.route('/directdebit.html')
def directdebit():
    return render_template('directdebit.html')

######## 대출내역 페이지 ########
@app.route('/loan.html')
def loan():
    return render_template('loan.html')

######## 휴먼예금/보험금 페이지 ########
@app.route('/deposit.html')
def deposit():
    return render_template('deposit.html')






# 메인페이지 메인타이틀 - (1)입력
@app.route("/maininfo", methods=["POST"])
def maininfo_post():
    maininfo_receive = request.form['maininfo_give']
    doc = {
        'maininfo' : maininfo_receive
    }
    db.maininfo.insert_one(doc)
    return jsonify({'msg': '저장완료'})

# 메인페이지 메인타이틀 - (2)조회
@app.route("/maininfo", methods=["GET"])
def maininfo_get():
    all_maininfo_get = list(db.maininfo.find({},{'_id':False}))
    return jsonify({'result': all_maininfo_get})







if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)