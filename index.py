from flask import Flask, request, render_template

import dao

app = Flask(__name__)


@app.route('/')
def index():
    kw = request.args.get('kw')
    danh_muc = dao.danh_muc()
    lop_can_gia_su = dao.lop_can_gia_sư(kw)
    return render_template('index.html', danh_muc=danh_muc, lop_can_gia_su=lop_can_gia_su)


if __name__ == '__main__':
    app.run(debug=True)