import base64

#圖片檔轉成程式碼

def pic2py(picture_name):
    """
    將圖像文件轉換爲py文件
    :param picture_name:
    :return:
    """
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    # 注意這邊b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()

if __name__ == '__main__':
    pics = ["bg.jpg"]
    for i in pics:
        pic2py(i)
    print("ok")
