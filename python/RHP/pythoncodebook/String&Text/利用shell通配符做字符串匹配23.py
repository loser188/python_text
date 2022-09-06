# 当工作在unix shellx下时，想使用常见的通配符模式（*.py\dat[0-9]*.csv)来对文本做匹配

# fnmath模块提供了两个函数-fnmatch和fnmatchcase可用来执行这样的匹配
from fnmatch import fnmatch

print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('dat45.csv','dat[0-9].*'))

# 该函数的匹配模式采用大小写区分规则和底层文件系统相同（根据运行时的操作系统而定）

# fnmatchcase()采用提供的大小写方式来匹配
