import os


def analyze_log_file(log_file):
    pass


# передача нужного файла и каталога
def analyze_logs(directory):
    for file in os.listdir(directory):
        if file.endswith(".log"):
            file_path = os.path.join(directory, file)
            analyze_log_file(file_path)


# Передача каталога, заменю потом на input
log_directory = 'C:\\access_test'
analyze_logs(log_directory)
