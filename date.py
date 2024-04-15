from datetime import datetime

def formate_date_anvil(date):
    date_object = datetime.fromisoformat(date.replace("Z", "+00:00"))
    formatted_date = date_object.strftime("%Y-%m-%d")
    date_array = formatted_date.split("-")

    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "June"
    }

    month = date_array[1] 
    if month[0] == "0":
        month_num = month.replace("0", "")
        print(month_num)
        int_month = int(month_num)
        print(type(int_month))

    return_date = {
        "day": date_array[2],
        "month": months[int_month],
        "month_num": date_array[1],
        "year": date_array[0]
    }
    
    return return_date
