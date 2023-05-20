from datetime import datetime


def edit_column(dataframe_name, column_name, edit_function):
    """Edit a dataframe column in-place using the provided edit_function."""
    dataframe_name[column_name] = dataframe_name[column_name].apply(edit_function)
    
def clean_military_time(time_int: int):
    """Takes a military time int object and cleans it by adding zeros at appropriate places"""
    """Assumptions: Single digit and double digit inputs are assumed to be minutes """
    time = str(time_int)
    if len(time) == 3:
        time_mod = '0' + time[0] + ':' + time[1:]
    elif len(time) == 4:
        time_mod = time[0:2] + ':' + time[2:]
    elif len(time) == 1:
        time_mod = '00:'+'0' +time[0]
    elif len(time) == 2 and int(time[0:2])<=59:
        time_mod = '00:'+ time[0:2]
    elif len(time) == 2 and int(time[0:2])>59:
        time_mod = '0'+time[0]+':'+time[1]+'0'
    return datetime.strptime(time_mod, '%H:%M').strftime('%H:%M')
