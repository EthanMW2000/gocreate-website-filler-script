import pkg.file_opener as file_opener
import pkg.excel_parser as excel_parser
import pkg.website_filler as website_filler


def main():
  filepath = file_opener.open_file()
  if not filepath:
    return print('No file selected. Closing program.')
  parsedfile = excel_parser.parse_excel(filepath)
  website_filler.fill_website(parsedfile)
  


main()