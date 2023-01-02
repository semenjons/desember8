
from Sort import sort,get_da
from Viewing import choice_number_operasion,get_data
from Write_file import read_file,write_file
from main import sort_data


def button():
    return sort_data(choice_number_operasion,read_file,write_file,sort,get_da,get_data)