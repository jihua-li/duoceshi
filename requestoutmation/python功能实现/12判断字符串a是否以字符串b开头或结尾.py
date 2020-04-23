import os, stat

"""已xx开头使用startswith()
   已xx结尾使用endswith()
   注意：多个匹配时参数使用元组"""

#获取12files目录下所有文件名称
files_name = os.listdir('./12files/')
print(files_name)

#获取文件名称以.py结尾的文件名
py_end_file_name = [name for name in files_name if name.endswith('.py')]
print(py_end_file_name)
#获取文件名以a开头的文件名
a_start_filename = [name for name in files_name if name.startswith('a')]
print(a_start_filename )


#获取文件以.py和.html结尾的文件名，多个匹配使用元组
py_html_file_name = [name for name in files_name if name.endswith(('.py', '.html'))]
print(py_html_file_name)

#获取文件的权限，十进制数
st_mode = os.stat('./12files/e.py').st_mode
print(st_mode)
#将十进制数转换成八进制数,0o100644 后面三位就是操作权限
print(oct(st_mode))

#查看文件执行掩码
os.chmod('./12files/e.py', st_mode | stat.S_IXUSR)
print(oct(os.stat('./12files/e.py').st_mode))

"""文件权限掩码
stat.S_ISUID: Set user ID on execution.
stat.S_ISGID: Set group ID on execution.
stat.S_ENFMT: Record locking enforced.
stat.S_ISVTX: Save text image after execution.
stat.S_IREAD: Read by owner.
stat.S_IWRITE: Write by owner.
stat.S_IEXEC: Execute by owner.
stat.S_IRWXU: Read, write, and execute by owner.
stat.S_IRUSR: Read by owner.
stat.S_IWUSR: Write by owner.
stat.S_IXUSR: Execute by owner.
stat.S_IRWXG: Read, write, and execute by group.
stat.S_IRGRP: Read by group.
stat.S_IWGRP: Write by group.
stat.S_IXGRP: Execute by group.
stat.S_IRWXO: Read, write, and execute by others.
stat.S_IROTH: Read by others.
stat.S_IWOTH: Write by others.
stat.S_IXOTH: Execute by others."""