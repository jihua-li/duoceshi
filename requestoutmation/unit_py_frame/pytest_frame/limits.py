import pytest, sys
#pip list |grep 'python3'  #查看pyton版本号

#python版本
limit_ver = pytest.mark.skipif(sys.version_info < (3, 8), reason="python版本过低跳过")