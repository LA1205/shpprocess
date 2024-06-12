import pandas as pd
import geopandas as gpd

# 读取shapefile
gdf = gpd.read_file('your_shapefile.shp')

# 读取Excel工作表
xls = pd.ExcelFile('your_excel_file.xlsx')

# 创建一个字典来存储每个字段的映射字典，这里目前有问题，会把重复的键值存在一个字典里
mapping_dicts = {}

# 字段和工作表的对应关系
field_sheet_mapping = {'FieldA': 'Sheet1', 'FieldB': 'Sheet2'}  # 请根据实际情况修改

# 对于每个字段和对应的工作表
for field, sheet in field_sheet_mapping.items():
    # 读取工作表
    df = pd.read_excel(xls, sheet)
    # 将数据框转换为字典并存储在mapping_dicts中
    mapping_dicts[field] = df.set_index('key')['value'].to_dict()

# 更新shapefile属性表中的字段
for field, mapping_dict in mapping_dicts.items():
    gdf[field] = gdf[field].map(mapping_dict)

# 保存更新后的shapefile
gdf.to_file('updated_shapefile.shp')