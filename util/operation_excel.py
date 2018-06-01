import xlrd

class OperationExcel:
    def __init__(self,file_name,sheet_id):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.data = self.get_data()

    #获取sheets内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取tables行数
    def get_lines(self):
        tables = self.get_data()
        return tables.nrows

    #获取指定单元格内容
    def get_cell_value(self,row,col):
        return self.get_data().cell_value(row,col)

if __name__ == '__main__':
    opers = OperationExcel('./dataconfig/interface.xlsx',0)
    print(opers.get_data().nrows)
    print(opers.get_lines())
    print(opers.get_cell_value(2,2))
   