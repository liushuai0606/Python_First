from asyncio import protocols

from matplotlib import pyplot as plt
# import matplotlib
# print(matplotlib.matplotlib_fname())
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'b', 'g', 'y']


def mat_bing(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(12, 6))
    # 某部分爆照出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.01,0.01,0.01,0.01)

    patches, label_test, percent_text = plt.pie(size_list,
                                                # explode=explode,
                                                labels=name_list,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    # labeldistance, 文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，园里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow, 饼是否有阴影
    # startangle, 起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance,百分比的text离圆心的距离
    # patches,1_texts,p_texts,为了得到饼图的返回值，p_texts饼图内部文本的，1_texts饼图外labe的文本
    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for l in label_test:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20
    # 设置x,y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


def mat_zhu(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=colorlist)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=colorlist)

    # 添加主题和注释
    plt.title('协议与带宽分布')  # 主题
    plt.xlabel('带宽（M/s）')  # X轴注释
    plt.ylabel('协议')  # Y轴注释

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


def mat_line(cpu_usage_list):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S')) # 设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    # 把cpu_usage_list的数据,拆分为x轴的时间,与y轴的利用率
    x = []
    y = []

    for time, cpu in cpu_usage_list:
        x.append(time)
        y.append(cpu)

    # 添加主题和注释
    plt.title('路由器CPU利用率')
    plt.xlabel('采集时间')
    plt.ylabel('CPU利用率')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果你有两套数据,完全可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    counters = [30, 53, 12, 45]
    proto = ['http协议', 'ftp协议', 'rdp协议', 'qq协议']
    mat_bing(counters, proto)
    mat_zhu(counters, proto)
    from datetime import datetime, timedelta
    from random import randrange
    now = datetime.now()
    time_cpu_usage = []
    for x in range(-12, 13):
        time_cpu_usage.append([(now + timedelta(hours=x)), randrange(101)])
    mat_line(time_cpu_usage)
