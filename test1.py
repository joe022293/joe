from reportlab.pdfgen import canvas
from PIL import Image
import qrcode
from PyPDF2 import PdfFileMerger
import streamlit as st
import base64
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

first_list = ['42', '44', '45', '46']
folder_path = 'folder'
try:
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 处理 PDF 文件
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)  # 删除文件

    st.title('Registration QR codes')
    input_i = st.text_input("Input serial numbers (e.g. 42220001,44230010-44230020,45210001)")
    input = input_i.replace(" ", "")

    # 注册Montserrat字体
    pdfmetrics.registerFont(TTFont('Montserrat', 'Montserrat-Regular.ttf'))

    def create_pdf(begin, final):
        merger = PdfFileMerger()
        # ... (之后的代码保持不变)
        
        i = 0
        while begin_num + i <= final_num and tp == 0:
            # ... (之后的代码保持不变)

        with open(f'{begin}-{final}.pdf', 'rb') as file:
            pdf_data = file.read()

        # Convert the PDF data to base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
        return pdf_base64

    begin_list = []
    final_list = []
    pdf_list = []

    # Create a download button
    st.write("")
    if st.button('Generate'):
        temp1 = input.split(',')
        for i in temp1:
            if len(i) == 8 and i.isdigit() and i[:2] in first_list:
                begin = i
                final = i
                begin_list.append(begin)
                final_list.append(final)
                pdf_list.append(create_pdf(begin, final))
            elif '-' in i:
                i_split = i.split('-')
                if len(i_split) == 2 and i_split[0].isdigit() and len(i_split[0]) == 8 and i_split[1].isdigit() and len(i_split[1]) == 8 and i_split[0][:4] == i_split[1][:4] and i_split[0][:2] in first_list:
                    if int(i_split[1]) - int(i_split[0]) <= 200 and int(i_split[1]) - int(i_split[0]) > 0:
                        begin = i_split[0]
                        final = i_split[1]
                        begin_list.append(begin)
                        final_list.append(final)
                        pdf_list.append(create_pdf(begin, final))
                    elif int(i_split[0]) - int(i_split[1]) <= 200 and int(i_split[1]) - int(i_split[0]) <= 0:
                        begin = i_split[1]
                        final = i_split[0]
                        begin_list.append(begin)
                        final_list.append(final)
                        pdf_list.append(create_pdf(begin, final))
                    else:
                        st.write(f'Exceeding the maximum of 200 serial numbers: {i_split[0]}-{i_split[1]}')
                else:
                    st.write(f'Wrong serial number: {i_split[0]}-{i_split[1]}')
            else:
                st.write(f'Wrong serial number: {i}')

        # Generate download link
        for j in range(len(begin_list)):
            if begin_list[j] != final_list[j]:
                href = f'<a href="data:application/pdf;base64,{pdf_list[j]}" download="{begin_list[j]}-{final_list[j]}.pdf">Download {begin_list[j]}-{final_list[j]}.pdf</a>'
                st.markdown(href, unsafe_allow_html=True)
            else:
                href = f'<a href="data:application/pdf;base64,{pdf_list[j]}" download="{begin_list[j]}.pdf">Download {begin_list[j]}.pdf</a>'
                st.markdown(href, unsafe_allow_html=True)
except Exception as e:
    st.error(e)
