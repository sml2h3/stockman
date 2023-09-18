from stockman.policies import *


def blxp(c: daily_k.stock_close, h: daily_k.stock_high, l: daily_k.stock_low, o: daily_k.stock_open,
                      v: daily_k.stock_vol, ul: daily_k.stock_up_limit, td: daily_k.stock_trade_date):
    # 近7个交易日有过至少》7%以上的涨幅
    recent_days_o = o[-8:]
    recent_days_c = c[-8:]
    has_uplimit = False
    idx = 0

    for idx, item in enumerate(recent_days_c):
        if item >= recent_days_o[idx] * 1.09:
            idx_d = idx - 8
            now_c = c[idx_d + 1]
            last_c = c[idx_d]
            now_h = h[idx_d + 1]
            last_h = h[idx_d]
            now_l = l[idx_d + 1]
            last_l = l[idx_d]
            now_v = v[idx_d + 1]
            last_o = o[idx_d]
            now_o = o[idx_d + 1]
            last_v = v[idx_d]

            now_ul = ul[idx_d + 1]

            # 必须高开
            if now_o > last_c:
                # 成交量必须是倍量,至少1.5
                if last_v * 2 < now_v:
                    # 必须冲高，至少6%
                    if now_h / last_c - 1 > 0.06:
                        # 必须低走, 但是最低不能超过水下-2
                        if now_l > last_c * 0.96 and (now_c > last_c * 0.96 and now_c < last_c * 1.04):
                            return [True, [td[idx_d + 1]]]
    return [False, []]
