import textract
import uuid
from collections import Counter


FILES = {
    'file_id': str(uuid.uuid1()),
    'file_details': {
        'file_type': '',
        'file_name': '',
        'file_size': '',
    },
}


def process():
    select_file = 'files/text/machine_translation.pdf'
    open_document = textract.process(select_file, encoding='utf-8')

    process_file = open("output/file.txt", "wb+")
    process_file.write(open_document.lower())
    process_file.close()

    output_file = open("output/file.txt", "r+")
    output_file = output_file.read().split()

    return len(output_file)

    # print("List\n" + str(output_file) + "\n")
    # print("Frequencies\n" + str(wordfreq) + "\n")
    # print("Pairs\n" + str(zip(output_file, wordfreq)))

print FILES