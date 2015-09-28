import xlrd
import xlwt
file_location="/Users/yushunzhe/Desktop/fragilestatesindex-2006to2014.xlsx"
workbook=xlrd.open_workbook(file_location)
# sheet=workbook.sheet_by_index(0)
# data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
sheet=[]
for i in range(workbook.nsheets):
	sheet.append(workbook.sheet_by_index(i))
# for i in range(workbook.nsheets):
# 	print(sheet[i].row_values(1))

wbk=xlwt.Workbook()
new_sheet=wbk.add_sheet('combined_version', cell_overwrite_ok=True)
for i in range(workbook.nsheets):
	# for j in sheet[i].nrows:
	j=i * (sheet[i].nrows)
	while j< (i+1)*sheet[i].nrows:
		temp=sheet[i].row_values(j%(sheet[i].nrows))
		# print(temp)
		col=0
		for element in temp:
			new_sheet.write(j, col, element)
			col+=1
		j+=1
wbk.save('data.xls')
