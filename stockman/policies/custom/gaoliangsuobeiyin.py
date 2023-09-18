from stockman.policies import *


def glsby(c: daily_k.stock_close, h: daily_k.stock_high, l: daily_k.stock_low, o: daily_k.stock_open,
         v: daily_k.stock_vol, ul: daily_k.stock_up_limit, td: daily_k.stock_trade_date):
    # 前天出现倍量阴线，今天缩量阴线
    idx_d = -3
    mid_c = c[idx_d + 1]
    now_c = c[idx_d + 2]
    last_c = c[idx_d]
    mid_l = l[idx_d + 1]
    now_l = l[idx_d + 2]
    mid_v = v[idx_d + 1]
    now_v = v[idx_d + 2]
    last_v = v[idx_d]
    ma5_mid_list = v[idx_d+1 - 5:idx_d+1]
    ma5_mid = sum(ma5_mid_list)/len(ma5_mid_list)
    # 成交量必须是倍量,至少2倍
    if mid_c < last_c and last_c * 0.97 > mid_c:
        if last_v * 1.7 < mid_v and mid_v > ma5_mid * 2:
            # 完成倍量, 需要一个缩倍量阴线
            if now_c < mid_c:
                if now_v * 1.7 < mid_v:
                    if abs(now_l / mid_l - 1) < 0.01:
                        return [True, [td[-1]]]

    return [False, []]
