import numpy as np


class man():
    love_list = []
    is_free = True
    top = 0

class woman():
    love_list = []
    is_free = True
    pair_man = -1

def man_is_free(m):
    for i in m:
        if m[str(i)].is_free:
            return True
    return False

def man_is_full_proposed(m, num):
    for i in m:
        if m[str(i)].top < num-1:
            return False
    return True


if __name__ == "__main__":

    '''先来个3男3女, 随机赋值心愿列表'''
    number_pair = 20
    m = {}
    w = {}
    for i in range(number_pair):
        # 男生
        m[str(i)] = man()
        # 随机给好感排行榜
        a = np.arange(0, number_pair)
        np.random.shuffle(a)
        m[str(i)].love_list = a.tolist()

        # 女生
        w[str(i)] = woman()
        a = np.arange(0, number_pair)
        np.random.shuffle(a)
        w[str(i)].love_list = a.tolist()

    # # 给定好感排行榜，帮助测试
    # m['0'].love_list = [2, 1, 0]
    # m['1'].love_list = [0, 1, 2]
    # m['2'].love_list = [2, 0, 1]
    # w['0'].love_list = [2, 0, 1]
    # w['1'].love_list = [1, 2, 0]
    # w['2'].love_list = [0, 2, 1]

    # print(m['1'].love_list)
    ind = 0  # 记录是哪个男孩
    for i in m:
        print("男生", i, "好感度排行榜", m[str(i)].love_list)
    print("-------------------------------------------------")
    for i in m:
        print("女生", i, "好感度排行榜", w[str(i)].love_list)
    print("-------------------------------------------------")
    while man_is_free(m) and not man_is_full_proposed(m, number_pair):
        if ind == number_pair:
            ind = 0

        # 如果男生有配偶就直接下一轮
        if not m[str(ind)].is_free:
            ind += 1
            continue
        # 如果男生中意的女生是空闲的
        if w[str(m[str(ind)].love_list[m[str(ind)].top])].is_free:
            m[str(ind)].is_free = False
            w[str(m[str(ind)].love_list[m[str(ind)].top])].is_free = False
            w[str(m[str(ind)].love_list[m[str(ind)].top])].pair_man = ind
        elif w[str(m[str(ind)].love_list[m[str(ind)].top])].love_list.index(w[str(m[str(ind)].love_list[m[str(ind)]
                .top])].pair_man) > w[str(m[str(ind)].love_list[m[str(ind)].top])].love_list.index(ind):
            m[str(w[str(m[str(ind)].love_list[m[str(ind)].top])].pair_man)].is_free = True
            w[str(m[str(ind)].love_list[m[str(ind)].top])].pair_man = ind
            m[str(ind)].is_free = False
        m[str(ind)].top += 1
        ind += 1
    for i in w:
        print("女性:", i, "其配偶是:", w[str(i)].pair_man)

