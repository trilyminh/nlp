
token_dicts = {
    "xe bus": ("N", "BUS"),
    "b3": ("N", "B3"),
    "những xe bus": ("N", "BUS"),
    "những xe": ("N", "BUS"),
    "nào": ("WH", "NÀO"),
    "đi": ("V", "ĐI"),
    "xuất phát": ("V", "XUẤT PHÁT"),
    "lúc": ("P", "LÚC"),
    "đến": ("P", "ĐẾN"),
    "từ": ("P", "TỪ"),
    "thành phố huế": ("CITY", "HUE"),
    "đà nẵng": ("CITY", "DANANG"),
    "thành phố hồ chí minh": ("CITY", "HCMC"),
    "huế": ("CITY", "HUE"),
    "20:00hr": ("TIME", "20:00HR"),
    "thời gian": ("TIME", "RUN-TIME"),
    "sinh viên": ("N", "SINHVIEN"),
    "mã số sinh viên": ("N", "MSHV"),
    "hãy liệt kê": ("WH", "Hãy liệt kê"),
    "môn": ("N", "MON"),
    "xử lý ngôn ngữ tự nhiên": ("N", "XLNNTN"),
    "ngôn ngữ lập trình": ("N", "NNLT"),
    "cơ sở dữ liệu": ("N", "CSDL"),
    "học": ("V", "HỌC"),
    "hãy cho biết": ("WH", "Hãy cho biết"),
    "mt12001": ("N", "mt12001"),
    "mt12002": ("N", "mt12002"),
    "mt12003": ("N", "mt12003"),
    "mt12004": ("N", "mt12004"),
    "mt12005": ("N", "mt12005"),
    "mt12006":("N", "mt12006"),
    "mt12007": ("N", "mt12007"),
    "mt12008": ("N", "mt12008"),
    "mt12009": ("N", "mt12009"),
    "mt12010": ("N", "mt12010"),
    "mt1101": ("N", "mt1101"),
    "mt1306": ("N", "mt1306"),
    "mt1105": ("N", "mt1105"),
    "mt1104": ("N", "mt1104"),
    "mt1301": ("N", "mt1301"),
    "ở": ("P", "ở"),
    ",": (",", ","),
    "có": ("V", "có"),
    "phòng": ("N", "phòng"),
    "ngày": ("N", "ngày"),
    "mấy": ("P", "mấy"),
    "tiết": ("N", "tiết"),
    "tên sinh viên": ("N", "tên sinh viên"),
    "tên": ("N", "tên môn học"),
    "khác": ("V", "khác"),
    "môn học": ("N", "môn học")
}
preposition_dict = {
    "từ": "SOURCE",
    "đến": "DEST",
    "lúc": "TIME",
}
noun_dict = {
    "môn": "MON",
    "mã số sinh viên": "MSHV",
}


dependency_dict = {
    "N_WH": ("right_arc", "NMOD"),
    "WH_N": ("left_arc", "NMOD"),
    "V_CITY": ("right_arc", "NMOD"),
    "N_N": ("right_arc", "NMOD"),
    "TIME_WH": ("right_arc", "NMOD"),
    "N_V": ("left_arc", "NSUBJ"),
    "P_CITY": ("left_arc", "CASE"),
    "V_TIME": ("right_arc", "TMOD"),
    "TIME_V": ("left_arc", "TMOD"),
    "P_TIME": ("left_arc", "CASE"),
    "N_,": ("left_arc", "N"),
    "WH_,": ("left_arc", "AND"),
    "P_N": ("left_arc", "CASE")
}

database_dict = {
    "BUS": {"B1", "B2", "B3", "B4"},
    "ATIME": {
        "B1 HUE 22:00HR",
        "B2 HUE 22:30HR",
        "B3 HCMC 05:00HR",
        "B4 HCMC 05:30HR",
        "B5 DANANG 13:30HR",
        "B6 DANANG 09:30HR",
        "B7 HCMC 20:30HR",
    },
    "DTIME": {
        "B1 HCMC 10:00HR",
        "B2 HCMC 12:30HR",
        "B3 DANANG 19:00HR",
        "B4 DANANG 17:30HR",
        "B5 HUE 8:30HR",
        "B6 HUE 5:30HR",
        "B7 HUE 8:30HR",
    },
    "RUNTIME": {
        "B1 HCMC HUE 12:00HR",
        "B2 HCMC HUE 10:00HR",
        "B3 DANANG HCMC 14:00HR",
        "B4 HCMC DANANG 12:00HR",
        "B5 DANANG HUE 5:00HR",
        "B6 DANANG HUE 4:00HR",
        "B7 HCMC HUE 12:00HR",
    },
    "MON":{
        "XLNNTN",
        "NNLT",
        "CSDL"
    },
    "MA_HV": {
        "MT12001",
        "MT12002",
        "MT12003",
        "MT12004",
        "MT12005",
        "MT12006",
        "MT12007",
        "MT12008",
        "MT12009",
        "MT12010",
        "MT1101",
        "MT1306",
        "MT1105",
        "MT1104",
        "MT1301"
    },
    "MA_TEN_HV": {
        "MT12001":"Phạm Văn Hai",
        "MT12002":"Trần Anh Dũng",
        "MT12003":"Nguyễn Thị Mai",
        "MT12004":"Nguyễn Thị Trang",
        "MT12005":"Đỗ Thanh Hải",
        "MT12006":"Lê Minh Trang",
        "MT12007":"Trần Quốc Việt",
        "MT12008":"Đoàn Minh Thịnh",
        "MT12009":"Văn Bạch Mai",
        "MT12010":"Nguyễn Hạnh Phúc",
        "MT1101":"Trần Thị Tuyết",
        "MT1306":"Phạm văn Ba",
        "MT1105":"Võ Khánh Triết",
        "MT1104":"Trịnh Xuân Hùng",
        "MT1301":"Lê Thanh Uyên"
    },
    "LICH_HOC": {
        "MT12001 XLNNTN",
        "MT12002 NNLT",
        "MT12003 XLNNTN",
        "MT12004 XLNNTN",
        "MT12005 NNLT",
        "MT12006 NNLT",
        "MT12007 XLNNTN",
        "MT12008 XLNNTN",
        "MT12009 NNLT",
        "MT12010 XLNNTN",
        "MT1101 CSDL",
        "MT1306 CSDL",
        "MT1105 NNLT",
        "MT1104 XLNNTN",
        "MT1301 NNLT"
    }
}
