import xlrd

file_path = r"C:\Users\13716\Desktop\学生参考.xls"

workbook = xlrd.open_workbook(file_path)
sheet = workbook.sheets()[1]
nrows = sheet.nrows
ncols = sheet.ncols

ncols_list = [3, 5, 8, 9, 10, 11, 12, 13, 15]
print("reading")
print(nrows, ncols)



with open(r"C:\Users\13716\Desktop\a.txt", "w+", encoding="utf-8")as f:  
    for i in range(nrows):
        for j in ncols_list:
            if j == 9:
                # A
                f.write("A: " + str(sheet.cell_value(i, j)) + "\n")
            elif j == 10:
                f.write("B: " + str(sheet.cell_value(i, j)) + "\n")
            elif j == 11:
                f.write("C: " + str(sheet.cell_value(i, j)) + "\n")
        
            elif j == 12:
                f.write("D: " + str(sheet.cell_value(i, j)) + "\n")

            elif j == 15:
                f.write("正确答案为: " + str(sheet.cell_value(i, j)) + "\n")
            else:
                f.write(sheet.cell_value(i, j) + "\n")
        f.write("\n\n")
