import codecs
import chardet
import os
import argparse

# 查看目录下文件所有的 encoding
def file_encoding(file_type):
    file_path = '~/Desktop/py-encoding-input/'
    ps = os.path.expanduser(file_path)
    s = set()
    for file in os.listdir(ps):
        if file.lower().endswith(file_type):
            with open(ps+file, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
                if encoding not in s:
                    print(file + ' ' + str(encoding))
                    s.add(encoding)

def rewrite2(file_path, target_file_path, to_encoding):

    # 获取文件 encoding
    with open(file_path, 'rb') as f:
        content = f.read()
    encoding = chardet.detect(content)['encoding']

    print('当前文件编码:'+str(encoding))
    if encoding == 'GB2312':
        with codecs.open(file_path, 'r', encoding='GBK') as f:
            content = f.read()
    elif encoding == 'utf-8':
        with codecs.open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        with codecs.open(file_path, 'r') as f:
            content = f.read()
    target_content = content.encode(to_encoding)

    # save
    with codecs.open(target_file_path, 'wb') as f:
        f.write(target_content)

def loop_file(file_type, to_encoding):
    source_path = '~/Desktop/py-encoding-input/'
    output_path = '~/Desktop/py-encoding-output/'
    ps = os.path.expanduser(source_path)
    po = os.path.expanduser(output_path)
    for file in os.listdir(ps):
        if file.lower().endswith(file_type):
            print(file)
            rewrite2(ps + file, po + file, to_encoding)

def pro(args):
    # 检测字符集
    file_encoding(args.type)
    # 文件编码转换
    loop_file(args.type, args.to)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-type', type=str, default='', help='文件类型')
    parser.add_argument('-to', type=str, default='', help='目标字符集')
    args = parser.parse_args()

    print('开始执行')
    pro(args)
    
    