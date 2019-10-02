
#Finding ingredients from tiles and returning true if the file has the ingredients
def find_ingrediens(f_path, term):
    file = open(f_path, encoding='utf-8')
    for line in file:
        line.strip().split('/n')
        if term in line:
            print("true")
    file.close()
find_ingrediens(r'C:\\Users\\yumo0\\OneDrive\\sanitySites\\recipe-pyth-api\\env\\Project\\PDF2Text\Text\\mariero-36.pdf.txt', 'BRINGEBÆR')
