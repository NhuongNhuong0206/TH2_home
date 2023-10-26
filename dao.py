def danh_muc():
    return [
        {
            'id': 1,
            'name': 'Dành cho phụ huynh học sinh'
        },
        {
            'id': 2,
            'name': 'Dành cho gia sư'
        },
        {
            'id': 1,
            'name': 'Thông tin của trung tâm'
        },
    ]


def lop_can_gia_sư(kw=None):
    ds_lop = [
        {
            'id': 1,
            'lop': 'lớp 6',
            'mon': 'Toán',
            'luong': 120000000
        },
        {
            'id': 2,
            'lop': 'lớp 7',
            'mon': 'Văn',
            'luong': 180000000
        },
        {
            'id': 3,
            'lop': 'lớp 9',
            'mon': 'Hoá-lí',
            'luong': 150000000
        },
        {
            'id': 3,
            'lop': 'lớp 11',
            'mon': 'Anh',
            'luong': 170000000
        },
        {
            'id': 4,
            'lop': 'lớp 12',
            'mon': 'Vật lý',
            'luong': 180000000
        }
    ]
    if kw:
        ds_lop = [lop for lop in ds_lop if lop['mon'].lower().find(kw.lower()) >= 0]
    return ds_lop