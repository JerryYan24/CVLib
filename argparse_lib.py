
# argument
# 1，如何读取命令行中传递进来的参数
#    sys.argv获取命令行中的所有参数
#    format：script的路径,其他参数...
# 2，专门处理命令行的library:  argparse
#   - 添加optional argument，有 add_argument("--a", type=int, help="xxx")
#       - 默认是可选的，意味着可以不用填写
#   - 添加positional argument，有 add_argument("a", type=int, help="xxx")
#       - 默认是不可选，必须填写，否则报错
#   - 添加flags，标记，开关那种形式 action argument
#       比如说，添加一个参数，是否需要打印信息, --verbose表示打印详细信息


import sys
import argparse

# print(sys.argv)
# if sys.argv[3] == "div":
#     print(int(sys.argv[1]) / int(sys.argv[2]))
# else:
#     print(int(sys.argv[1]) * int(sys.argv[2]))

# 先创建解释器
parser = argparse.ArgumentParser()

# 同样实现乘法操作output = a * b
# 添加a参数
parser.add_argument("method", type=str, help="Method")
parser.add_argument("--a", type=int, default=5, help="operator A")
parser.add_argument("--b", type=int, default=6, help="operator B")
parser.add_argument("--verbose", action="store_true", help="Print Message")

# 解析命令行
args = parser.parse_args()

print(args)
print(args.a * args.b)