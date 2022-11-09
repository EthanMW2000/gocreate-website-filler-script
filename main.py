import pkg.file_opener as file_opener
import pkg.excel_parser as excel_parser
import pkg.setup_website as setup_website


def main():
  filepath = file_opener.open_file()
  if not filepath:
    return print('No file selected. Closing program.')
  parsedfile = excel_parser.parse_excel(filepath)
  setup_website.setup(parsedfile)
  


main()