import glob
import os
import csv


def rename_images(subject_name):
    os.chdir("./" + subject_name)
    for sub_file in glob.glob("*.png"):
        os.rename(sub_file, subject_name + "_" + sub_file)
    os.chdir("./..")


def combine_csv(subject_name, local_first_flag):
    os.chdir("./" + subject_name)
    u_csv_result = ''
    for sub_file in glob.glob("*.csv"):
        with open(sub_file, newline='') as csv_file:
            spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            csv_string = ''
            for row in spamreader:
                temp_row = ', '.join(row)
                if (not local_first_flag) and (('scorer' in temp_row) or ('bodyparts' in temp_row)
                                               or ('coords' in temp_row)):
                    continue
                if '/' in temp_row:
                    row_rename = temp_row.split('/')
                    row_rename[1] = 'combined_data'
                    row_rename[2] = subject_name + "_" + row_rename[2]
                    temp_row = row_rename[0] + '/' + row_rename[1] + '/' + row_rename[2]
                csv_string += temp_row + '\n'
            u_csv_result += csv_string
    os.chdir("./..")
    return u_csv_result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.chdir('./labeled_data/')
    current_dir = os.getcwd()
    final_csv_string = ''
    first_flag = True
    for sub_folder in os.listdir(current_dir):
        rename_images(sub_folder)
        final_csv_string += combine_csv(sub_folder, first_flag)
        if final_csv_string:
            final_csv_string += '\n'
            first_flag = False
    with open('Collected_combined.csv', 'w') as csvfile:
        for line in final_csv_string:
            csvfile.write(line)
        csvfile.close()