from database import *
import io

def tri_query_string(question_logical_form, question_procedural, question):

    # sinh vien nao
    if question_logical_form.r[0].split(" ")[0].replace("(", "") == "SINHVIEN":
        data_list = {
            "MON": [False, set()],
        }

        for idx in range(1, len(question_procedural)):
            parsed_data = question_procedural[idx].split(" ")
            procedure, mon = parsed_data[0].replace("(", ""), parsed_data[2].replace(")", "")
            data_list[procedure][0] = True
            for data in database_dict[procedure]:
                data_sv, data_mon = data.split(" ")
                if (data_mon == mon):
                    data_list[procedure][1].add(data_sv)

        ans = database_dict["MA_HV"]
        for ans_lst in data_list.values():
            if ans_lst[0]:
                ans = ans.intersection(ans_lst[1])

        ans_name = database_dict["MA_TEN_HV"]
        ans_hv_name = []
        for entry in ans:
            ans_hv_name.append(entry+"-"+ans_name[entry])
        ans = ans_hv_name

        with io.open('output_d.txt', 'a+') as wr:
            if len(ans) == 0:
                ans = "None"
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Kết quả truy xuất dữ liệu: {}\n".format(ans))

    else:
        procedure, bus, source, dest, time = question_procedural.split(" ")
        procedure, time = procedure.replace("(", ""), time.replace(")", "")
        ans = None
        for data in database_dict[procedure]:
            data_bus, data_source, data_dest, data_time = data.split(" ")
            if bus == data_bus and source == data_source and dest == data_dest:
                ans = data_time

        with io.open('output_d.txt', 'a+') as wr:
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Kết quả truy xuất dữ liệu: {}\n".format(ans))

    return ans

def query_string(question_logical_form, question_procedural, question):
    if question_logical_form.r[0].split(" ")[0].replace("(", "") == "BUS":
        bus_list = {
            "ATIME": [False, set()],
            "DTIME": [False, set()],
        }

        for idx in range(1, len(question_procedural)):
            parsed_data = question_procedural[idx].split(" ")
            procedure, location, time = parsed_data[0].replace("(", ""), parsed_data[2], parsed_data[3].replace(")", "")
            bus_list[procedure][0] = True
            for data in database_dict[procedure]:
                data_bus, data_location, data_time = data.split(" ")
                if (data_location == location) and (data_time == time or time == "?t"):
                    bus_list[procedure][1].add(data_bus)

        ans = database_dict["BUS"]
        for ans_lst in bus_list.values():
            if ans_lst[0]:
                ans = ans.intersection(ans_lst[1])

        with io.open('output_d.txt', 'a+') as wr:
            if len(ans) == 0:
                ans = "None"
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Kết quả truy xuất dữ liệu: {}\n".format(ans))

    else:
        procedure, bus, source, dest, time = question_procedural.split(" ")
        procedure, time = procedure.replace("(", ""), time.replace(")", "")
        ans = None
        for data in database_dict[procedure]:
            data_bus, data_source, data_dest, data_time = data.split(" ")
            if bus == data_bus and source == data_source and dest == data_dest:
                ans = data_time

        with io.open('output_d.txt', 'a+') as wr:
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Kết quả truy xuất dữ liệu: {}\n".format(ans))

    return ans
