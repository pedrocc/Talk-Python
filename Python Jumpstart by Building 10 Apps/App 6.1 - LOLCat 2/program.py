import os
import requests
import shutil


def main():
    print_header()
    catfolder = get_cat_folder()
    download_cat_pictures(catfolder)



def print_header():
    print('============================')
    print('          LOLCats')
    print('============================')


def get_cat_folder():
    filepath = os.path.dirname(__file__)
    filepath = os.path.join(filepath, 'catpictures')
    if not os.path.isdir(filepath):
        os.mkdir(filepath)
        print('catpictures folder created...')
    return(filepath)


def download_cat_pictures(catfolder):
    print('Contacting server to download cats...')
    for x in range(1,9):
        url='http://consuming-python-services-api.azurewebsites.net/cats/random'
        data_cat = requests.get(url, stream=True)
        data = data_cat.raw
        filename = os.path.join(catfolder, str(x) + '.jpg')
        with open(filename, 'wb') as fout:
            shutil.copyfileobj(data, fout)
    print('Cats were born...')


if __name__ == '__main__':
    main()