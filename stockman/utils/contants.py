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

stock_list_insert_or_update_sql = "INSERT INTO {}stock_list ({}) VALUE ({}) ON DUPLICATE KEY UPDATE {}"

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

stock_list_status = [
    "L",
    "D",
    "P"
]

# 数据源列表，默认首字母大写
apis_list = [
    'Tushare',
]

# 权限列表，用于生成权限清单等，方便多数据源共同工作
permissons_list = [
    'stock_list',  # 股票列表
    'stock_daily',  # 股票日线数据
]

# 初始化时 按顺序需要执行的操作
init_ops = [
    "stock_list",
    "stock_daily",
]
