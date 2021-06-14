import os
import sys
import csv
from openpyxl import Workbook

# Setting input parameter of layout
filepath = sys.argv[1] 
# the file path
filename = sys.argv[2]
 # file name

# ---------------- Parameters that from Layout ----------------------------
# -----------------------We are changable --------------------------------
##Layout center absolute coordinate
### x 
center_x = 113.620
### y
center_y = 105.622
## adding the  distance in x direction from center to center point of first print
x_center_to_first = 95.568
## adding the distance in x diraction between to print center
x_distance = 5.166
## dictance between 2toCenter and 3toCenter
y_low_dis = 2.745
## dictance between 1or4 to Center
y_high_dis = 44.705
## width of print
width_print = 2.998
# -------------------------------------------------------------------------
# ----------------- We are not changable ----------------------------------
first = center_x - x_center_to_first
offset = width_print*0.8
# -------------------------------------------------------------------------

def rowCoordinate(row)->float:
# Here defined count sequence is from top to bottom, the numer 1-38 is row 1
    output = 0.0
    if row == 1:
        output = y_high_dis + center_y
    elif row == 2:
        output = y_low_dis + center_y
    elif row == 3:
        output = -y_low_dis + center_y
    else:
        output = -y_high_dis + center_y
    return output


# adding new workbook
new_wb = Workbook()
new_ws = new_wb.active
csv_headers = ['Location','x_rel_start','y_rel_start','x_rel_end','y_rel_end']
headers=['Number','row','colume','x_abs','y_abs','x_rel','y_rel']
new_ws.append(headers)

#file write-in
file_pn = filepath + filename +'.csv'
with open(file_pn, 'w', encoding='utf-8', newline='') as target_file:
    target_writer = csv.DictWriter(target_file, fieldnames=csv_headers)
    target_writer.writeheader()

    data_in = input("Please input measure point 1-152,split with ',':\t")
    number_of_measurepoint = data_in.split(",")
    koor_info = []
    loc_info ={}

    for item in number_of_measurepoint:
    
        num = int(item)
        colume = num
        row = 1
        if (num-1) / 38:
            row = 1 + int((num-1) / 38)
            colume = num % 38
            if colume == 0:
                colume = 38
        koor_info=[num, row, colume, first + (colume-1)*x_distance,rowCoordinate(row), first + (colume-1)*x_distance - center_x, rowCoordinate(row) - center_y]

        loc_name = 'R'+ str(row) + 'C' + str(colume)
        loc_x_rel_s = str(first + (colume-1)*x_distance - offset)
        loc_x_rel_e = str(first + (colume-1)*x_distance + offset)
        loc_y_rel = str(rowCoordinate(row) - center_y)
        loc_info['Location']= loc_name
        loc_info['x_rel_start']= loc_x_rel_s
        loc_info['y_rel_start']= loc_y_rel
        loc_info['x_rel_end']= loc_x_rel_e
        loc_info['y_rel_end']= loc_y_rel
        new_ws.append(koor_info)
        target_writer.writerow(loc_info)


wb_path = filepath + filename + '.xlsx'
new_wb.save(wb_path)