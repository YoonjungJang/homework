from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 1. 클라이언트가 준 name, count, address, phone 가져오기.
    # 2. DB에 정보 삽입하기
    # 3. 성공 여부 & 성공 메시지 반환하기

    # name_receive로 클라이언트가 준 name 가져오기
    name_receive = request.form['name_give']
    # count_receive로 클라이언트가 준 count 가져오기
    count_receive = request.form['count_give']
    # address_receive로 클라이언트가 준 address 가져오기
    address_receive = request.form['address_give']
    # phone_receive로 클라이언트가 준 phone 가져오기
    phone_receive = request.form['phone_give']

    # DB에 삽입할 doc 만들기
    order = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive,
    }
    # orders에 doc 저장하기
    db.orders.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 1. DB에서 주문 정보 모두 가져오기
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
