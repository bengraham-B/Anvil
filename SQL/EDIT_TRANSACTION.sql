UPDATE transaction 
SET 
    details = {details},
    amount = {amount},
    category = {category},
    class = {_class},
    date = {date},

    month = {month},
    year = {year},
    day = {day}


WHERE 
    user_id = {user_id} and id={transaction_id}
