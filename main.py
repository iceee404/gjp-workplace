from tools.getPdfList import get_pdf_files
from tools.pdfToPng import convert_pdf_to_images
from tools.geminiAPI import process_image
from tools.getPngList import get_png_files
prefix = "./static/"

# pdf_list = get_pdf_files(prefix+"pdf/")

# for pdf_file in pdf_list:
#     print(pdf_file)

# png_list = get_png_files("Example Drawing Package 1A")

# process_image(prefix+"img/"+png_list[0])


# only test specific page
process_image(prefix+"img/Example Drawing Package 1A_images/Example Drawing Package 1A_page_1.png")
process_image(prefix+"img/Example Drawing Package 2A_images/Example Drawing Package 2A_page_3.png")
process_image(prefix+"img/Example Drawing Package 3A_images/Example Drawing Package 3A_page_2.png")
process_image(prefix+"img/Example Drawing Package 4A_images/Example Drawing Package 4A_page_3.png")
process_image(prefix+"img/Example Drawing Package 5A_images/Example Drawing Package 5A_page_3.png")
process_image(prefix+"img/Example Drawing Package 6A_images/Example Drawing Package 6A_page_2.png")
