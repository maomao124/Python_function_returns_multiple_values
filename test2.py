"""
 * Project name(项目名称)：Python函数返回多个值
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:56
 * Version(版本): 1.0
 * Description(描述)： 多值返回
 """


def f1(a, b):
    """
    多值返回,加加键乘除取余数
    :param a:
    :param b:
    :return:
    """
    return a + b, a - b, a * b, a / b, a % b


def f2(a, b):
    """
    多值返回,加加键乘除取余数
    :param a:
    :param b:
    :return:
    """
    return (a + b, a - b, a * b, a / b, a % b)


def f3(a, b):
    """
    多值返回,加加键乘除取余数
    :param a:
    :param b:
    :return:
    """
    return (a + b), (a - b), (a * b), (a / b), (a % b)


if __name__ == '__main__':
    print(f1(9, 2))
    print(type(f1(9, 2)))

    print(f2(9, 2))
    print(type(f2(9, 2)))

    print(f3(9, 2))
    print(type(f3(9, 2)))
