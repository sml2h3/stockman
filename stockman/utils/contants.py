"""
      Author:  sml2h3                              
      Date:    2023/1/19                             
      File:    contants                             
      Project: PyCharm                     
"""

create_stock_list_table_sql = '''
CREATE TABLE `{}stock_list`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '股票代码，A股一般为6位，暂时设置为10位以防以后做其他的',
  `stock_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票名称',
  `stock_area` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票公司主体所在位置区域',
  `stock_industry` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票公司主体所在行业',
  `stock_fullname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票公司主体名称',
  `stock_enname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票公司主体英文名称',
  `stock_cnspell` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票公司主体名成的拼音缩写',
  `stock_market` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票所处市场（目前分类为主板、创业板、科创板、CDR）',
  `stock_exchange` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票所处交易所的代码',
  `stock_currtype` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票当前使用的交易货币',
  `stock_status` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票当前的上市状态 L 上市 D 退市 P 暂停上市',
  `stock_createtime` int(8) NULL DEFAULT NULL COMMENT '股票上市时间',
  `stock_deletetime` int(8) NULL DEFAULT NULL COMMENT '股票退市时间',
  `stock_hs` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '股票是否为沪深港通标的 N为否  H 沪股通 S 深股通',
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE INDEX `code`(`stock_code`) USING BTREE COMMENT '股票代码',
  INDEX `area`(`stock_area`) USING BTREE COMMENT '股票公司主体所在位置区域',
  INDEX `stock_name`(`stock_name`) USING BTREE COMMENT '股票名称',
  INDEX `status`(`stock_status`) USING BTREE COMMENT '股票上市状态',
  INDEX `createtime`(`stock_createtime`) USING BTREE COMMENT '股票上市时间',
  INDEX `hs`(`stock_hs`) USING BTREE COMMENT '股票是否为沪深港通标的'
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
'''

create_stock_daily_k_table_sql = '''
CREATE TABLE `stockman_daily_k`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '股票代码',
  `stock_trade_date` int(11) NULL DEFAULT NULL COMMENT '股票交易日期',
  `stock_close` float NULL DEFAULT NULL COMMENT '股票收盘价',
  `stock_open` float NULL DEFAULT NULL COMMENT '股票开盘价',
  `stock_high` float NULL DEFAULT NULL COMMENT '股票最高价',
  `stock_low` float NULL DEFAULT NULL COMMENT '股票最低价',
  `stock_pre_close` float NULL DEFAULT NULL COMMENT '股票昨收价',
  `stock_change` float NULL DEFAULT NULL COMMENT '股票涨跌额',
  `stock_pct_change` float NULL DEFAULT NULL COMMENT '股票涨跌幅',
  `stock_vol` float NULL DEFAULT NULL COMMENT '股票成交量（手）',
  `stock_amount` float NULL DEFAULT NULL COMMENT '股票成交额（千元）',
  `stock_adj_factor` float NULL DEFAULT NULL COMMENT '股票复权因子',
  `stock_open_hfq` float NULL DEFAULT NULL COMMENT '股票开盘价后复权',
  `stock_open_qfq` float NULL DEFAULT NULL COMMENT '股票开盘价前复权',
  `stock_close_hfq` float NULL DEFAULT NULL COMMENT '股票收盘价后复权',
  `stock_close_qfq` float NULL DEFAULT NULL COMMENT '股票收盘价前复权',
  `stock_high_hfq` float NULL DEFAULT NULL COMMENT '股票最高价后复权',
  `stock_high_qfq` float NULL DEFAULT NULL COMMENT '股票最高价前复权',
  `stock_low_hfq` float NULL DEFAULT NULL COMMENT '股票最低价后复权',
  `stock_low_qfq` float NULL DEFAULT NULL COMMENT '股票最低价前复权',
  `stock_pre_close_hfq` float NULL DEFAULT NULL COMMENT '股票昨收价后复权',
  `stock_pre_close_qfq` float NULL DEFAULT NULL COMMENT '股票昨收价前复权',
  `stock_macd_dif` float NULL DEFAULT NULL COMMENT '股票macd_diff',
  `stock_macd_dea` float NULL DEFAULT NULL COMMENT '股票macd_dea',
  `stock_macd` float NULL DEFAULT NULL COMMENT '股票macd',
  `stock_kdj_k` float NULL DEFAULT NULL COMMENT '股票KDJ_K',
  `stock_kdj_d` float NULL DEFAULT NULL COMMENT '股票KDJ_D',
  `stock_kdj_j` float NULL DEFAULT NULL COMMENT '股票KDJ_J',
  `stock_rsi_6` float NULL DEFAULT NULL COMMENT '股票RSI-6',
  `stock_rsi_12` float NULL DEFAULT NULL COMMENT '股票RSI-12',
  `stock_rsi_24` float NULL DEFAULT NULL COMMENT '股票RSI-24',
  `stock_boll_upper` float NULL DEFAULT NULL COMMENT '股票BOLL_UPPER',
  `stock_boll_mid` float NULL DEFAULT NULL COMMENT '股票BOLL_MID',
  `stock_boll_lower` float NULL DEFAULT NULL COMMENT '股票BOLL_LOWER',
  `cci` float NULL DEFAULT NULL COMMENT '股票CCI',
  `stock_up_limit` float NULL DEFAULT NULL COMMENT '股票涨停价格',
  `stock_down_limit` float NULL DEFAULT NULL COMMENT '股票跌停价格',
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE INDEX `unique_key`(`stock_code`, `stock_trade_date`) USING BTREE COMMENT '唯一键值',
  INDEX `stock_code`(`stock_code`) USING BTREE COMMENT '股票代码',
  INDEX `stock_trade_date`(`stock_trade_date`) USING BTREE COMMENT '股票交易日期'
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;
'''

create_stock_cal_table_sql = '''
CREATE TABLE `{}trade_cal`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_cal_date` int(11) NULL DEFAULT NULL COMMENT '日历日期',
  `stock_is_open` int(1) NULL DEFAULT 0 COMMENT '是否交易 0休市 1交易',
  `stock_pretrade_date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '上一个交易日',
  PRIMARY KEY (`Id`) USING BTREE,
  UNIQUE INDEX `stock_cal_date`(`stock_cal_date`) USING BTREE COMMENT '日历日期',
  INDEX `stock_is_open`(`stock_is_open`) USING BTREE COMMENT '是否交易'
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
'''

create_stock_func_limits_table_sql = '''
CREATE TABLE `stockman_func_limits`  (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_api_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '数据源名称',
  `stock_func_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '调用的函数名称',
  `stock_times` int(11) NULL DEFAULT NULL COMMENT '在某个时间长度内最大调用次数',
  `stock_times_time` int(11) NULL DEFAULT NULL COMMENT '单位时间长度，单位为秒',
  PRIMARY KEY (`Id`) USING BTREE,
  INDEX `stock_api_name`(`stock_api_name`) USING BTREE COMMENT '数据源名称',
  INDEX `stock_func_name`(`stock_func_name`) USING BTREE COMMENT '调用的函数名称',
  UNIQUE INDEX `unique_keys`(`stock_api_name`, `stock_func_name`) USING BTREE COMMENT '数据源对应的函数名称只能有一个'
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
'''

init_stock_func_limits_data_sql = '''
INSERT INTO `{}func_limits` VALUES (1, 'tushare', 'stock_daily_sub', 100, 60);
'''

show_tables_sql = '''
show tables;
'''

stock_list_col_names = [
    "stock_code",
    "stock_name",
    "stock_area",
    "stock_industry",
    "stock_fullname",
    "stock_enname",
    "stock_cnspell",
    "stock_market",
    "stock_exchange",
    "stock_currtype",
    "stock_status",
    "stock_createtime",
    "stock_deletetime",
    "stock_hs",
]

stock_daily_col_names = [
    "stock_code",
    "stock_trade_date",
    "stock_close",
    "stock_open",
    "stock_high",
    "stock_low",
    "stock_pre_close",
    "stock_change",
    "stock_pct_change",
    "stock_vol",
    "stock_amount",
    "stock_adj_factor",
    "stock_open_hfq",
    "stock_open_qfq",
    "stock_close_hfq",
    "stock_close_qfq",
    "stock_high_hfq",
    "stock_high_qfq",
    "stock_low_hfq",
    "stock_low_qfq",
    "stock_pre_close_hfq",
    "stock_pre_close_qfq",
    "stock_macd_dif",
    "stock_macd_dea",
    "stock_macd",
    "stock_kdj_k",
    "stock_kdj_d",
    "stock_kdj_j",
    "stock_rsi_6",
    "stock_rsi_12",
    "stock_rsi_24",
    "stock_boll_upper",
    "stock_boll_mid",
    "stock_boll_lower",
    "cci",
    "stock_up_limit",
    "stock_down_limit"
]


stock_list_insert_or_update_sql = "INSERT INTO {}stock_list ({}) VALUE ({}) ON DUPLICATE KEY UPDATE {}"

stock_trade_cal_insert_sql = "INSERT INTO {}trade_cal (stock_cal_date, stock_is_open, stock_pretrade_date) VALUE ( %s, %s, %s)"

stock_daily_insert_or_update_sql = "INSERT INTO {}daily_k ({}) VALUE ({}) ON DUPLICATE KEY UPDATE {}"

stock_get_trade_cal_from_now_sql = "SELECT stock_cal_date, stock_pretrade_date FROM {}trade_cal WHERE stock_is_open = 1 AND stock_cal_date <= {}"

stock_get_trade_cal_from_now_sql_fix = " AND stock_cal_date > {}"

stock_check_trade_date_sql = "SELECT stock_is_open FROM {}trade_cal WHERE stock_cal_date = {}"

stock_daily_get_last_trade_date_sql = "SELECT DISTINCT stock_trade_date FROM {}daily_k"

stock_get_func_times_limits_sql = "SELECT * FROM {}func_limits WHERE stock_api_name = %s AND stock_func_name = %s"

stock_set_func_times_limits_sql = "UPDATE {}func_limits SET stock_times = %s, stock_times_time = %s WHERE stock_api_name = %s AND stock_func_name = %s"

stock_get_single_stock_daily_k_sql = "SELECT * FROM {}daily_k WHERE stock_code = %s ORDER BY stock_trade_date ASC"

stock_get_single_stock_list_sql = "SELECT * FROM {}stock_list WHERE stock_code = %s AND stock_status = 'L'"

stock_get_all_stock_list_sql = "SELECT * FROM {}stock_list WHERE stock_status = 'L'"

stock_list_fields = [
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date",
    "fullname",
    "enname",
    "cnspell",
    "exchange",
    "curr_type",
    "list_status",
    "delist_date",
    "is_hs"
]

stock_trade_cal_fields = [
    "cal_date",
    "is_open",
    "pretrade_date"
]

stock_daily_limit_fields = [
    "ts_code",
    "up_limit",
    "down_limit",
]


stock_daily_fields = [
    "ts_code",
    "trade_date",
    "close",
    "open",
    "high",
    "low",
    "pre_close",
    "change",
    "pct_change",
    "vol",
    "amount",
    "adj_factor",
    "open_hfq",
    "open_qfq",
    "close_hfq",
    "close_qfq",
    "high_hfq",
    "high_qfq",
    "low_hfq",
    "low_qfq",
    "pre_close_hfq",
    "pre_close_qfq",
    "macd_dif",
    "macd_dea",
    "macd",
    "kdj_k",
    "kdj_d",
    "kdj_j",
    "rsi_6",
    "rsi_12",
    "rsi_24",
    "boll_upper",
    "boll_mid",
    "boll_lower",
    "cci"
]

stock_list_status = [
    "L",
    "D",
    "P"
]

stock_prefix = {
    "SZSE": "SZ",
    "BSE": "BJ",
    "SSE": "SH",
}

# 数据源列表，默认首字母大写
apis_list = [
    'Tushare',
]

# 权限列表，用于生成权限清单等，方便多数据源共同工作
permissons_list = [
    'stock_list',  # 股票列表
    'stock_daily',  # 股票日线数据
    'stock_trade_cal',  # 股票交易日历
]

# 初始化时 按顺序需要执行的操作
init_ops = [
    "stock_list",
    "stock_trade_cal",
    "stock_daily",
]
