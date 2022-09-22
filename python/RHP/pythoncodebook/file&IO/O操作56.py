# 想将一段文本或二进制字符串写入类似文件的对象上
# 使用io.StringIO  和  io。BytesIO
import io

s=io.StringIO()
s.write('Hello Word\n')
print('This is a test',file=s)
print(s.getvalue())

s=io.StringIO('Hello\n World\n')
print(s.read(4))  # 会将读取的字符从文件中删除
print(s.read())

# io.StringIO  只能对文本进行处理
# io.BytesIO   处理二进制文件
