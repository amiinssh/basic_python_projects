hours_played = 15

def get_time_trophy(hours_played):
    if hours_played >= 50:
        trophy_name = "Valiant Veteran"
    elif hours_played >= 10 and hours_played < 23:
        trophy_name = "Active Adventurer"
    elif hours_played >= 24 and hours_played <= 49:
        trophy_name = "Humble Hero"
    else:
        trophy_name = "Trainee Traveller"
        
    return trophy_name


print(get_time_trophy(2))   
print(get_time_trophy(11))  
print(get_time_trophy(33))  
print(get_time_trophy(55))  
print(get_time_trophy(49))