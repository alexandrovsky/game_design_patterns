import random
from flask import Flask
from flask import Response, jsonify, render_template, request
from flask_bootstrap import Bootstrap
import pandas as pd
# import openpyxl
from data import targets
app = Flask(__name__)
Bootstrap(app)

WORK_SHEET = 'game_design_patterns.xlsx'

@app.route('/')
def homepage():    
    # targets = {}
    # wb = openpyxl.load_workbook(WORK_SHEET)
    # ws = wb.get_sheet_by_name('Sheet1')
    # max_row = ws.max_row
    max_row = len(targets.keys())
    print(f"{max_row=}")
    patterns = {} 
    for i in range(3):
        key = list(targets.keys())[random.randrange(0, max_row)]
        val = targets[key]
        patterns[key] = val
        #print(row, max_row)
        # targets[ws.cell(row=row, column=1).value] = ws.cell(row=row, column=1).hyperlink.target    
    return render_template('index.html', targets=patterns)



# def export_ws_as_dict():
#     wb = openpyxl.load_workbook(WORK_SHEET)
#     ws = wb.get_sheet_by_name('Sheet1')
#     max_row = ws.max_row
#     targets = {}
#     for row in range(1,max_row):        
#         print(row, max_row)
#         targets[ws.cell(row=row, column=1).value] = ws.cell(row=row, column=1).hyperlink.target
#     print(targets)


if __name__ == '__main__':
    #export_ws_as_dict()
    app.run(host="0.0.0.0", port=80)
    