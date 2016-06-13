import os
import cat_services
import requests
import subprocess


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('=============================================')
    print('                CAT FACTORY')
    print('============================================= \n')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.isdir(full_path):
        print('Creating new directory...')
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for x in range(1,cat_count+1):
        print('Download cat {}'.format(x))
        name = 'lolcat {}'.format(x)
        cat_services.get_cat(folder, name)


def display_cats(folder):
    subprocess.call(['open', folder])



if __name__ == '__main__':
    main()

