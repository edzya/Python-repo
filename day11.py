import string
from typing import Counter


def read_data(fpath):
    with open(fpath, encoding='utf-8') as txt:
        read = txt.read()
    return read


def file_line_len(fpath):
    readFile = read_data(fpath)
    qty = 0
    for line in readFile:
        if line.endswith('\n'):
            qty += 1
    print("Lines in file: ", qty)
    return qty


file_line_len('veidenbaums.txt')


def get_poem_lines(fpath):
    with open(fpath, encoding='utf-8') as txt:
        read = txt.readlines()
        readCopy = read.copy()
        for lines in read:
            if lines.endswith('***\n') or lines == '\n':
                readCopy.remove(lines)

        print(readCopy)
    return readCopy


get_poem_lines("veidenbaums.txt")


def save_lines(destpath, lines):
    with open(destpath, encoding='utf8', mode='w') as newFile:
        newFile.writelines(lines)


save_lines('veidenbaums_clean.txt', get_poem_lines('veidenbaums.txt'))


def clean_punkts(srcPath, destPath):
    with open(destPath, encoding='utf-8', mode='w') as destFile, open(srcPath, encoding='utf-8') as srcFile:
        for line in srcFile:
            for c in string.punctuation:
                line = line.replace(c, '')
            destFile.write(line)


clean_punkts('veidenbaums_clean.txt', 'veidenbaums_no_punkts.txt')


def get_word_usage(srcpath, destpath, top=50):
    with open(srcpath, encoding='utf-8') as fin, open(destpath, encoding='utf-8', mode='w') as fout:
        txt = fin.read()
        readList = txt.replace('\n', ' ').strip().split(' ')
        readListLower = map(lambda el: el.lower(), readList)
        # print(list(readListLower))
        wholeCount = Counter(readListLower)
        top20 = wholeCount.most_common(top)
        for line in top20:
            fout.write(f"{line} \n")


get_word_usage('veidenbaums_no_punkts.txt', 'stats_file.txt', 50)
