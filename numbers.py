import os

class Numbers:
    @staticmethod
    def check_integer(line):
        try:
            if not isinstance(int(line), int):
                return False

            if not float(line).is_integer():
                return False

        except ValueError:
            return False

        return True

    @staticmethod
    def write_numbers(n, write_file):
        '''
        Write n integers into file line by line starting from 1.
        :param n: Count of numbers to be written
        :param write_file: File name where the numbers are written
        :return: Return True if numbers were written. Otherwise False
        '''
        if not write_file or n < 0:
            return False

        with open(write_file, 'w+') as w_file:
            for i in range(1, n + 1):
                w_file.write(str(i) + '\n')

        return True

    @staticmethod
    def read_numbers(n, read_file):
        '''
        Read n integers from file. It is assumed that integers are written in each line
        :param n: Count of numbers to read
        :param read_file: The file name where the numbers are read
        :return: Return list of numbers if n unique numbers were read from file. Otherwise None
        '''

        if not read_file:
            return None

        if not os.path.isfile(read_file):
            return None

        number_list = []
        with open(read_file, 'r') as r_file:
            for line in r_file:
                if Numbers.check_integer(line) and int(line) not in number_list:
                        number_list.append(int(line))

                if len(number_list) == n:
                    break


        if n != len(number_list):
            return None

        return number_list

if __name__ == "__main__":
    file_name = "number_file.txt"
    Numbers.write_numbers(100, file_name)
    print("Wrote 100 numbers to file {}".format(file_name))
    read_list = Numbers.read_numbers(50, file_name)
    print("Read 50 numbers from file {}".format(file_name))
    print(read_list)
