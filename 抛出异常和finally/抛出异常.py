# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def handle(self):
#         print "User defined exception: ", self.msg
#
#
#
# try:
#     raise Accident('crash between two cars')
# except Accident as e:
#     e.handle()


#什么是finally
#总的来说，就是意识前面代码因为异常二无法使用
#finally模块下的代码仍然可以执行


