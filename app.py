from dbModel import *

from flask import jsonify

from serializer import *



@app.route("/")
def hello():
    #db.create_all()
    return "Hello, World!"

@app.route('/getMember', methods=['GET'])
def getMember():
    expected="查無使用者"
    memberItem=Member.query.all()
    return jsonify([*map(member_serializer,memberItem)])

if __name__ == '__main__':
    app.run(debug=True)
