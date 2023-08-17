# ...（之前的代码部分）

def create_pdf(begin, final):
    merger = PdfFileMerger()
    # 提取前两位数字
    begin_prefix = begin[:2]
    final_prefix = final[:2]
    ModelName = ""
    tp = 0

    if begin_prefix == '42':
        ModelName = "MVR Lite"
    elif begin_prefix == '44':
        ModelName = "MVR Pro"
    elif begin_prefix == '45':
        ModelName = "MVC Pro SDI to HDMI"
    elif begin_prefix == '46':
        ModelName = "MVR"
    else:
        # print("wrong")
        tp = 1

    begin_num = int(begin)
    final_num = int(final)

    # ...（后续的代码部分）

    i = 0
    while begin_num + i <= final_num and tp == 0:
        # ...（后续的代码部分）

        with open(f'{begin_num + i}.pdf', 'rb') as file:
            pdf_data = file.read()

        # Convert the PDF data to base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
        return pdf_base64

    # ...（后续的代码部分）

# ...（后续的代码部分）

try:
    # ...（之前的代码部分）

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

        # ...（后续的代码部分）

except Exception as e:
    st.error(e)
