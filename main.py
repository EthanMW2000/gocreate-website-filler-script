from pkg.file_opener.file_opener import open_file
from pkg.excel_parser.excel_parser import parse_excel
from pkg.setup_website.setup_website import setup
from pkg.setup_website.fill_users import fill_users


def main():
  filepath = open_file()
  if not filepath:
    return print('No file selected. Closing program.')
  parsedfile = parse_excel(filepath)
  browser = setup()
  fill_users(parsedfile, browser)
  


main()