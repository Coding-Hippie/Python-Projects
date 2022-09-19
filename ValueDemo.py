# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:52:18 2022

@author: Jacob Stack
"""

import xlsxwriter

workbook = xlsxwriter.Workbook('c:\\Users\\User alias\\Desktop\\Projects\\Python\\valueDemo.xlsx')
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})
cell_format.set_font_size(14)
cell_format.set_align('center')

cell_format1 = workbook.add_format({'font_color': 'black'})

cell_format1.set_align('center')
worksheet.write('A1', 'value', cell_format)
worksheet.write('B1', 'value', cell_format)
worksheet.write('C1', 'value', cell_format)
worksheet.write('D1', 'value', cell_format)
row = 1
col = 0

worksheet.set_column('A1:A1', 10)
worksheet.set_column('B1:B1', 50)
worksheet.set_column('C1:C1', 40)
worksheet.set_column('D1:D1', 40)

data = (
    ['value', 'value', 'value', 'value'],
    ['value', 'value', 'value', 'value'],
    ['value', 'value', 'value', 'value'],
)

workbook.close()
