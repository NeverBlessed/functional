class Worker:
    """
    
    Attributes
    ----------
    val : int
        balance of worker

    matrix_ans : array
        matrix_ans is the last solution of worker.
        
    m1, m2 : matrices
        matrices for work

    Methods
    -------
    read_matrix
    
    take_matrices
    
    take_salary(salary = x)
        Increases the val by salary.

    prepare(mat1, mat2)
        checks matrices

    """
    val = 0
    matrix_ans = [[]]
    m1 = [[]]
    m2 = [[]]

    @staticmethod
    def read_matrix(fn):
        """

        parameters
        ---------
        fn : string (filename)

        returns
        ---------
        matrix : list of lists
            matrix from fn

        """
        matrix = []
        with open(fn) as f:
            for line in f:
                line = line.strip()
                matrix.append(list(map(int, line.split())))
            return matrix

    def take_matrices(self, f1, f2):
        """
        changes matrices of worker to matrices from files f1 and f2

        parameters
        ---------
        f1 : string (filename)
        f2 : string (filename)
        """
        self.m1 = self.read_matrix(f1)
        self.m2 = self.read_matrix(f2)

    def prepare(self, mat1, mat2):
        """
        checks if matrices are suitable for workers and make matrix_ans = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        for having 10 coins for the job if they are not

        parameters
        ---------
        mat1 : matrix
        mat2 : matrix

        returns
        ---------
        1 / 0
        """
        self.matrix_ans = []
        if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
            return 1
        else:
            self.matrix_ans = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            return 0

    def take_salary(self, x):
        """ increases val with x

        parameters
        ---------
        x : int

        """
        self.val += x


class Pupa(Worker):
    """

    Attributes
    ----------
    val : int
        balance of Pupa
    matrix_ans : array
        matrix_ans is the last solution of Pupa.

    Methods
    -------
    take_salary(salary = x)
        Increases the balance by salary.
    do_work(file1, file2)
        read matrices from file1 and file2
        and adds element by element to matrix_ans

    """
    def do_work(self, filename1, filename2):
        """
        read matrices from file1 and file2
        and adds element by element to matrix_ans and print it

        parameters
        ---------
        filename1 : string
        filename2 : string

        """
        self.take_matrices(filename1, filename2)
        if self.prepare(self.m1, self.m2):
            self.matrix_ans = [[self.m1[i][j] + self.m2[i][j] for j in range(len(self.m1[0]))] for i in
                               range(len(self.m1))]
            print(self.matrix_ans)


class Lupa(Worker):
    """

    Attributes
    ----------
    val : int
        balance of Lupa
    matrix_ans : array
        matrix_ans is the last solution of Lupa.

    Methods
    -------
    take_salary(salary = x)
        Increases the val by salary.
    do_work(file1, file2)
        read matrices from file1 and file2
        subtracts element by element and add the result to matrix_ans

    """
    def do_work(self, filename1, filename2):
        """
        read matrices from file1 and file2
        subtracts element by element and add the result to matrix_ans and print it

        parameters
        ---------
        filename1 : string
        filename2 : string

        """
        self.take_matrices(filename1, filename2)
        if self.prepare(self.m1, self.m2):
            self.matrix_ans = [[self.m1[i][j] - self.m2[i][j] for j in range(len(self.m1[0]))] for i in
                               range(len(self.m1))]
            print(self.matrix_ans)


class Accountant:
    @staticmethod
    def give_salary(worker):
        x = len(worker.matrix_ans) * len(worker.matrix_ans[0])
        worker.take_salary(x)


def main():
    accountant = Accountant()
    pupa = Pupa()
    lupa = Lupa()
    pupa.do_work('inp1.txt', 'inp2.txt')
    lupa.do_work('inp1.txt', 'inp2.txt')
    print(lupa.val)
    print(pupa.val)
    accountant.give_salary(pupa)
    accountant.give_salary(lupa)
    print(lupa.val)
    print(pupa.val)


if __name__ == "__main__":
    main()
