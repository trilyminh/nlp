import io


def schedule_procedural_form_string(question_logical_form, question):
    list_question_procedural = {}
    for key_query,question_logical_form_r_entry in enumerate(question_logical_form.r):
        if ' b)' in question_logical_form_r_entry and len(question_logical_form_r_entry.split(" ")) <= 2:
            question_procedural = [question_logical_form_r_entry]
            # condition query
            index = 0
            while index < len(question_logical_form.r):
                if ' b)' not in question_logical_form.r[index]:
                    role = question_logical_form.r[index].split(" ")[0].replace("(", "")
                    m = question_logical_form.r[index].split(" ")[-1][:-1]
                    if role == "MON":
                        if '(SINHVIEN b)' in question_logical_form_r_entry:
                            question_procedural.append("(LICH_HOC b {})".format(m))
                        if '(PHONG b)' in question_logical_form_r_entry:
                            question_procedural.append("(MON_PHONG {} b)".format(m))
                        if '(TIET b)' in question_logical_form_r_entry:
                            question_procedural.append("(MON_TIET {} b)".format(m))
                        if '(NGAY b)' in question_logical_form_r_entry:
                            question_procedural.append("(MON_NGAY {} b)".format(m))
                    if role == "MSHV":
                        if '(MON b)' in question_logical_form_r_entry:
                            question_procedural.append("(LICH_HOC {} b)".format(m))
                index += 1
            list_question_procedural[question_logical_form_r_entry] = question_procedural
    return list_question_procedural

def procedural_form_string(question_logical_form, question):
    if question_logical_form.r[0].split(" ")[0].replace("(", "") == "BUS":
        question_procedural = [question_logical_form.r[0]]
        index = 1
        while index < len(question_logical_form.r):
            role = question_logical_form.r[index].split(" ")[0].replace("(", "")
            question_logical_form.r[index + 1].split(" ")[0].replace("(", "") if index + 1 < len(
                question_logical_form.r) else ""

            if role == "DEST":
                d = question_logical_form.r[index].split(" ")[-1][:-1]
                question_procedural.append("(ATIME b {} ?t)".format(d))
            elif role == "SOURCE":
                s = question_logical_form.r[index].split(" ")[-1][:-1]
                question_procedural.append("(DTIME b {} ?t)".format(s))
            elif role == "TIME":
                t = question_logical_form.r[index].split(" ")[-1][:-1]
                question_procedural[-1] = question_procedural[-1].replace("?t", t)
            index += 1

        with io.open('output_c.txt', 'a+') as wr:
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Ngữ nghĩa thủ tục: (PRINT_ALL b {})\n".format("".join(question_procedural)))
    else:
        question_procedural = "(RUNTIME ?b ?s ?d ?t)"
        # question_procedural = "(SUBJECT ?b ?n)"
        index = 0
        while index < len(question_logical_form.r):
            role = question_logical_form.r[index].split(" ")[0].replace("(", "")
            if role == "DEST":
                d = question_logical_form.r[index].split(" ")[-1][:-1]
                question_procedural = question_procedural.replace("?d", d)
            elif role == "SOURCE":
                s = question_logical_form.r[index].split(" ")[-1][:-1]
                question_procedural = question_procedural.replace("?s", s)
            elif role == "BUS":
                b = question_logical_form.r[index].split(" ")[1]
                question_procedural = question_procedural.replace("?b", b)
            index += 1

        with io.open('output_c.txt', 'a+') as wr:
            wr.writelines("=========\n")
            wr.writelines("Câu hỏi: " + question + "\n")
            wr.writelines("- Ngữ nghĩa thủ tục: (PRINT_ALL t {})\n".format(question_procedural))

    return question_procedural
