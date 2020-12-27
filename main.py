from logical_form_string import *
from depenency_gramar import *
from procedural_form import *
from query import *


def read_input_question():
    list_question = []
    with open("input_question.txt", "r") as f:
        data_file = f.readlines()
    for data_line in data_file:
        list_question.append(str(data_line))

    return list_question


def clear_file():
    open('output_a.txt', 'w').close()
    open('output_b.txt', 'w').close()
    open('output_c.txt', 'w').close()
    open('output_d.txt', 'w').close()


def run_program(question):
    print("=========")
    print("Câu hỏi: ", question)
    question_dependency_grammer = dependency_string(question)
    print("Quan hệ văn phạm: ", question_dependency_grammer)
    question_logical_form = logical_form_string(question_dependency_grammer, question)
    print("Dạng luận lý: ", question_logical_form)
    list_question_procedural = schedule_procedural_form_string(question_logical_form, question)
    print("Ngữ nghĩa thủ tục: ", list_question_procedural)
    answer = schedule_query_string(question_logical_form, list_question_procedural, question)
    print("Kết quả truy xuất dữ liệu: ", answer)

def main():
    clear_file()
    list_question = read_input_question()
    if len(list_question) == 0:
        question = "Sinh viên nào học môn cơ sở dữ liệu?"
        run_program(question)
    else:
        for question in list_question:
            run_program(question)


if __name__ == "__main__":
    main()
