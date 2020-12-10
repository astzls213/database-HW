'''
from app.models import (
    User,
    Journal,
    Email,
    Editor,
    Organizer
)

# 初始化数据库 用于开发时测试

def init_database(app,db):
    admin = User(
        'admin',
        'admin@6324.com',
        'iamadmin',
        True
    )
    # Chinese Medical Journal
    CMJ = Journal(
        '0366-6999',
        '11-2154/R',
        'Chinese Medical Journal',
        'Chinese Medical Journal',
        1887,
        24,
        '北京东四西大街42号中华医学会',
        '100710',
        '8610-85158321',
        '8610-85158333'
    )
    editor1 = Editor('照日格图')
    editor2 = Editor('甄洛生牛逼甄洛生牛逼甄洛生牛逼')
    organ1 = Organizer('中华医学会')
    organ2 = Organizer('甄洛生牛逼甄洛生牛逼甄洛生牛逼甄洛生牛逼甄洛生牛逼')
    

    with app.app_context():
        db.drop_all()
        db.create_all()
        # 创建管理员账户
        db.session.add(admin)
        # 为CMJ添加邮箱/主编/主办单位
        db.session.add(Email('cmj@cma.org.cn',CMJ))
        CMJ.editors.append(editor1)
        CMJ.editors.append(editor2)
        CMJ.organizers.append(organ1)
        CMJ.organizers.append(organ2)
        db.session.commit()
'''

import reportlab
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys,os

def createPagePdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1,num+1): 
        c.drawString((210//2)*mm, (4)*mm, str(i))
        c.showPage()
    c.save()
    return 
    with open(tmp, 'rb') as f:
        pdf = PdfFileReader(f)
        layer = pdf.getPage(0)
    return layer


if __name__ == "__main__":
    path = 'report.pdf'
    base = os.path.basename(path)

    tmp = "__tmp.pdf"

    batch = 10
    batch = 0
    output = PdfFileWriter()
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f,strict=False)
        n = pdf.getNumPages()
        if batch == 0:
            batch = -n
        createPagePdf(n,tmp)
        with open(tmp, 'rb') as ftmp:
            numberPdf = PdfFileReader(ftmp)
            for p in range(n):
                if not p%batch and p:
                    newpath = path.replace(base, base[:-4] + '_page_%d'%(p//batch) + path[-4:])
                    with open(newpath, 'wb') as f:
                        output.write(f)
                    output = PdfFileWriter()
                print('page: %d of %d'%(p, n))
                page = pdf.getPage(p)
                numberLayer = numberPdf.getPage(p)

                page.mergePage(numberLayer)
                output.addPage(page)
            if output.getNumPages():
                newpath = path.replace(base, base[:-4] + '_page_%d'%(p//batch + 1)  + path[-4:])
                with open(newpath, 'wb') as f:
                    output.write(f)

        os.remove(tmp)
