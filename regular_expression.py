
import re

re.match(r'^\d{3}\-\d{3,8}$', '010-123456')

# 编译正则字符串
re_telephone = re.compile(r'^(\d{3})-(\d{3,8}$)')
# 使用
re_telephone.match('010-12345').groups()
re_telephone.match('010-8589').groups()
