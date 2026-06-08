raw_logs = []
processed_logs = []

LINE = "="*60
LINEWITHMINUS = "-"*60

def clean_the_input(input_wanna_to_clean):
    delete_table = str.maketrans("", "", "!#$@")
    return input_wanna_to_clean.translate(delete_table).split(";")
def clean_input():
    global raw_logs
    print("--- NẠP DỮ LIỆU LOG ---")
    while True:
        input_wanna_to_clean = input("Nhập chuỗi log thô (Cách nhau bởi dấu phẩy ; ): ").strip()
        if(not input_wanna_to_clean):
            print("chuỗi log không được để trống !")
            continue 
        break 
    print("Đã làm sạch và lưu 2 dòng log vào hệ thống")
    print(clean_the_input(input_wanna_to_clean))
    raw_logs.append(clean_the_input(input_wanna_to_clean))
def show_warnning(dis_list):
    global processed_logs
    count_warning = 0
    for value in dis_list:
        for item in value:
            if("ERROR" in item.upper() or "CRITICAL" in item.upper()):
                count_warning += 1
                if(item in processed_logs):
                    continue
                processed_logs.append(item)
    return count_warning

def display_warning(dis_list):
    global processed_logs
    print("--- LỌC CẢNH BÁO ---")
    count = show_warnning(dis_list)
    print(f"Tìm thấy {count} cảnh báo nguy hiểm !")
    for item in processed_logs:
            print("- " + item)
def display_ip_address(process_list):
    print("--- MÃ HÓA IP ---")
    print("Báo cáo Log an toàn")
    for idex, value in enumerate(processed_logs):
        result = " ".join([value.split(" ")[0],value.split(" ")[1][0:7:1]+"."+"*"+"."+"*"+"." ,f"{value.split(" ")[2] + " " + value.split(" ")[3]}"])
        print(f"{idex + 1}. {result}")
def show_menu():
    return int(input(
        f"{LINEWITHMINUS} \n"
        f"{"SECURITY LOG ANALYZER".center(60, "=")} \n"
        f"{"[1]. Nhập và làm sạch dữ liệu Log thô".ljust(60, " ")} \n"
        f"{"[2]. Lọc các Log cảnh cáo mức độ cao (ERROR / CRITICAL)".ljust(60, " ")} \n"
        f"{"[3]. Mã hóa địa chỉ IP (Masking)".ljust(60, " ")} \n"
        f"{"[4]. Đóng hệ thống".ljust(60, " ")} \n"
        f"{"".center(60, "=")} \n"
        f"{LINEWITHMINUS} \n"
        f">>> Nhập lựa chọn của bạn: "
        ))

def main():
    while True:
        try:
            choose = show_menu()
        except ValueError:
            print("Lựa chọn không phù hợp với dữ liệu !")
            continue 
        match choose:
            case 1:
                print()
                clean_input()
                print()
            case 2:
                print()
                display_warning(raw_logs)
                print()
            case 3:
                print()
                display_ip_address(processed_logs)
                print()
            case 4:
                print()
                print("Cảm ơn vì đã sử dụng chuong trình !")
                print()
                break 
            case _:
                print()
                print("Lựa chọn chỉ được trong [1 - 4] !")
                print()
                
if __name__ == "__main__":
    main()