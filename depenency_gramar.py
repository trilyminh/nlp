from database import *
import io


def get_question_token(question):
    question = question.rstrip().lstrip().lower()
    question = question.replace(",", " ,")
    if question[-1] == "?":
        question = question[:-1].rstrip()

    words = question.split(" ")
    num_words = len(words)
    question_tokens = []
    start_index = 0
    while start_index < num_words:
        for end_index in range(num_words, start_index, -1):
            token = " ".join(words[start_index:end_index])
            if token in token_dicts:
                start_index = end_index
                question_tokens.append(token)
                break
        else:
            exit("Error: cannot parse question = " + question)

    return question_tokens


def get_dependency(token_lst):
    stack, dependency, idx = [], [], 0
    while idx < len(token_lst):
        if not stack:
            stack.append(token_lst[idx])
            idx += 1
            continue

        relation = token_dicts.get(stack[-1])[0] + "_" + token_dicts.get(token_lst[idx])[0]
        if relation in dependency_dict:
            if dependency_dict[relation][0] == "left_arc":
                if dependency_dict[relation][1] == 'AND':
                    dependency.append("{}({})".format(dependency_dict[relation][1], token_lst[idx]))
                else:
                    dependency.append("{}({},{})".format(dependency_dict[relation][1], token_lst[idx], stack[-1]))
                stack.pop()
                continue
            else:  # right_arc
                dependency.append("{}({},{})".format(dependency_dict[relation][1], stack[-1], token_lst[idx]))
        else:
            stack.append(token_lst[idx])
        idx += 1

    return dependency


def dependency_string(vn_question):
    vn_question_tokens = get_question_token(vn_question)
    vn_question_depend = get_dependency(vn_question_tokens)
    with io.open('output_a.txt', 'a+') as wr:
        wr.writelines("=========\n")
        wr.writelines("Câu hỏi: " + vn_question + "\n")
        wr.writelines("- Quan hệ văn phạm: {}\n".format(vn_question_depend))

    return vn_question_depend
