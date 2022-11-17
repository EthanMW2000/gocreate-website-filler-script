from pkg.file_opener.file_opener import open_file
from pkg.excel_parser.excel_parser import parse_excel
from pkg.setup_website.setup_website import setup
from pkg.fill_users.fill_users import fill_users
from tkinter import messagebox


def main():
  filepath = open_file()
  if not filepath:
    return messagebox.Message('No File Selected', 'No file was selected.')
  parsedfile = parse_excel(filepath)
  browser = setup()
  fill_users(parsedfile, browser)
  
  return  

main()