#coding=utf-8

'''
有 A - K 13张牌按顺序覆在桌上，为牌堆1，每次把最顶上一张翻过来放在另一牌堆,如此反复直至牌堆1为空

'''


def rotate_poke(lst, tem=[]):
    
    if not lst:
        return tem

    tem.append(lst.pop(-1))
    if not lst:
        return tem

    lst.insert(0, lst.pop(-1))
    return rotate_poke(lst, tem)


r = rotate_poke(list(range(12)))
print(r)


