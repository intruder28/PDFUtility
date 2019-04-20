import PyPDF2
import os

def func_browse(path):
    pdf_files = []
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            pdf_files.append(filename)
    return pdf_files

def combine(files, output):
    pdf_writer = PyPDF2.PdfFileWriter()
    for file in files:
        pdf_file = open(file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for pageNum in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(pageNum)
            pdf_writer.addPage(page_obj)
    pdf_output = open(output + ".pdf", 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

def funcSplit(file, start, end, output):
    pdf_file = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    if end == "":
        end = pdf_reader.numPages
    else:
        end = int(end)
        end = end - 1
    for pageNum in range(pdf_reader.numPages):
        if (pageNum >= start and pageNum <= end):
            page_obj = pdf_reader.getPage(pageNum)
            pdf_writer.addPage(page_obj)
    pdf_output = open(output + ".pdf", 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()

#Function to clean the active window
def cls():os.system('cls' if os.name=='nt' else 'clear')

choice: str = "y"

#option: int = 1

while choice == "y":

    cls()

    print("Welcome to PDF Merge / Split Utility \n")

    print("Please select the function --> \n\t1. Merge PDFs\n\t2. Split PDFs\n")

    option = input("Please enter your choice? (1/2) --> \t")

    if option == "1":

        cls()

        print("Welcome to PDF Merge Utility \n")

        path: str = input("Please paste the folder path here --> \n")

        output_file: str = input("\nPlease enter the output filename here --> ")

        os.chdir(path)

        path = os.path.abspath(path)

        assert os.path.exists(path), "Folder does not exist. Please validate"

        pdf = func_browse(path)

        combine(pdf, output_file)

        cls()

        print("Completed consolidating ", len(pdf), " files successfully!\n")
    
    else:

        cls()
        
        print("Welcome to PDF Split Utility \n")

        path: str = input("Please enter the PDF file path here --> \n")

        filePath: str = os.path.dirname(path)

        os.chdir(filePath)

        path = os.path.abspath(path)

        start: int = input("\nPlease enter the starting page number -->\t")

        start = int(start) - 1

        end: int = input("Please enter the end page number -->\t")

        output_file: str = input("\nPlease enter the output filename here -->\t")

        funcSplit(path, start, end, output_file)     

        cls()

        print("File split completed successfully!\n")

    choice = input("Do you wish to continue? (y/n) --> ").lower()
