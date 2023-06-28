#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######  
import os

from xhtml2pdf import pisa
from PyPDF2 import PdfMerger

from common.utility import get_logo, get_version, get_language

if get_language() == 'italian':
    import common.constants.controller.report as REPORT
else:
    import common.constants.controller.report_eng as REPORT

class Html2Pdf:
    def __init__(self, cases_folder_path, case_info, ntp):
        self.cases_folder_path = cases_folder_path
        self.output_front = os.path.join(self.cases_folder_path , "front_report.pdf")
        self.output_content = os.path.join(self.cases_folder_path , "content_report.pdf")
        self.output_front_result = open(self.output_front, "w+b")
        self.output_content_result = open(self.output_content, "w+b")
        self.case_info = case_info
        self.ntp = ntp

    def generate_pdf(self, result, info_file_path):

        # PREPARING DATA TO FILL THE PDF
        with open(info_file_path, "r") as f:
            info_file = f.read()
        # FILLING FRONT PAGE WITH DATA

        front_index = open('assets/templates/front.html').read().format(
            img=get_logo(), t1=REPORT.T1,
            title=REPORT.TITLE, report=REPORT.REPORT, version=get_version()
        )


        content_index = open('assets/templates/template_pec.html').read().format(

            title=REPORT.TITLE,
            index=REPORT.INDEX,
            description=REPORT.DESCRIPTION, t1=REPORT.T1, t2=REPORT.T2,
            case=REPORT.CASEINFO, casedata=REPORT.CASEDATA,
            case0=REPORT.CASE, case1=REPORT.LAWYER, case2=REPORT.PROCEEDING,
            case3=REPORT.COURT, case4=REPORT.NUMBER, case5=REPORT.ACQUISITION_TYPE, case6=REPORT.ACQUISITION_DATE,
            t3=REPORT.REPORT_PEC, info_file=info_file,

            data0=str(self.case_info['name'] or 'N/A'),
            data1=str(self.case_info['lawyer_name'] or 'N/A'),
            data2=str(self.case_info['proceeding_type'] or 'N/A'),
            data3=str(self.case_info['courthouse'] or 'N/A'),
            data4=str(self.case_info['proceeding_number'] or 'N/A'),
            typed=REPORT.TYPED, type=REPORT.REPORT_PEC,
            date=REPORT.DATE, ntp=self.ntp,

        )
        # create pdf front and content, merge them and remove merged files
        pisa.CreatePDF(front_index, dest=self.output_front_result)
        pisa.CreatePDF(content_index, dest=self.output_content_result)
        merger = PdfMerger()
        merger.append(self.output_front_result)
        merger.append(self.output_content_result)
        merger.write(os.path.join(self.cases_folder_path , "report_integrity_pec_verification.pdf"))
        merger.close()
        self.output_content_result.close()
        self.output_front_result.close()
        if os.path.exists(self.output_front):
            os.remove(self.output_front)
        if os.path.exists(self.output_content):
            os.remove(self.output_content)
        if os.path.exists(info_file_path):
            os.remove(info_file_path)

