# import xlsxwriter module 
import xlsxwriter 
 
workbook = xlsxwriter.Workbook("line_chart.xlsx") 

worksheet = workbook.add_worksheet() 

bold = workbook.add_format({"bold": 1}) 
 
headings = ["Year", "Microsoft", "Alphabet", "Amazon"] 
data = [ 
    [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    [18.76, 23.15, 16.98, 21.86, 22.07, 12.19, 16.8, 21.2],
    [8.376, 9.706, 10.179, 12.733, 14.136, 16.348, 19.478, 12.662],
    [1.152, 0.631, 0.139, 0.274, 0.241, 0.596, 2.371, 3.033], 
] 

worksheet.write_row("A1", headings, bold) 

worksheet.write_column("A2", data[0]) 
worksheet.write_column("B2", data[1]) 
worksheet.write_column("C2", data[2]) 
worksheet.write_column("D2", data[3]) 

chart = workbook.add_chart({"type": "line"}) 
 
chart.add_series( 
    { 
        "name": "=Sheet1!$B$1", 
        "categories": "=Sheet1!$A$2:$A$9", 
        "values": "=Sheet1!$B$2:$B$9", 
    } 
) 

chart.add_series( 
     { 
        "name": ["Sheet1", 0, 2], 
        "categories": ["Sheet1", 1, 0, 8, 0], 
         "values": ["Sheet1", 1, 2, 8, 2], 
     } 
) 

chart.add_series( 
    { 
       "name": ["Sheet1", 0, 3], 
        "categories": ["Sheet1", 1, 1, 8, 1], 
        "values": ["Sheet1", 1, 3, 8, 3], 
    } 
) 
chart.set_title({"name": "Company Profit Analysis"}) 
chart.set_x_axis({"name": "Year"}) 
chart.set_y_axis({"name": "Profit (in Billions)"}) 
chart.set_style(4) 
 
worksheet.insert_chart("D2", chart, {"x_offset": 25, "y_offset": 10}) 
 
workbook.close()
