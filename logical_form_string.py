import io
from logical_form import *
from database import *


def parse_dependency(dependency):
    relationship = dependency.split("(")
    word1 = relationship[1].split(",")
    word2 = word1[1].split(")")
    return relationship[0], word1[0], word2[0]


def logical_form_string(question_dependency, question):
    question_logical_form = LogicalFormWH([], [])
    index = 0

    lastKeyWh = 0
    for keyDependency,question_dependency_entry in enumerate(question_dependency):
        relation, word1, word2 = parse_dependency(question_dependency_entry)
        if relation == 'NMOD' and (token_dicts[word1][0] == 'WH' or token_dicts[word2][0] == 'WH'):
            lastKeyWh = keyDependency

    relation, word1, word2 = parse_dependency(question_dependency[lastKeyWh])
    if relation != "NMOD" and word2 != "nào":
        exit("Error: Cannot parse question " + question)

    question_logical_form.r.append("({} b)".format(token_dicts[word1][1]))
    while index < len(question_dependency):
        if index == lastKeyWh:
            index += 1
            continue
        relation, word1, word2 = parse_dependency(question_dependency[index])
        if relation == "NSUBJ":
            question_logical_form.p.append("({} b)".format(word1.upper().replace(" ", "")))
        elif relation == "CASE":
            if word2 not in preposition_dict:
                exit("Error: Cannot parse question " + question)
            question_logical_form.r.append(
                "({} b {})".format(preposition_dict[word2], token_dicts[word1][1]))
            index += 1
        elif relation == "NMOD":
            if word1 not in noun_dict:
                question_logical_form.r.append("({} {} b)".format(token_dicts[word1][1], token_dicts[word2][1]))
            else:
                question_logical_form.r.append(
                    "({} b {})".format(noun_dict[word1],token_dicts[word2][1]))

        index += 1

    with io.open('output_b.txt', 'a+') as wr:
        wr.writelines("=========\n")
        wr.writelines("Câu hỏi: " + question + "\n")
        wr.writelines("- Dạng luận lý: {}\n".format(question_logical_form.__str__()))

    return question_logical_form
