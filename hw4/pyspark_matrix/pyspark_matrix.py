import pyspark
import numpy as np
import sys


def reduce_j(l):
    # to be used in flatMap to create (j, (i, value)) tuple
    for i in l[1]:
        yield(i[1], (l[0], i[0]))


def reduce_v(l):
    # flatMap add index to v
    for i in range(len(l)):
        yield(i, l[i])


def pyspark_matrix(A, v):
    """
    A: name of txt file that contains matrix A
    v: name of txt file that contains vector v
    output: txt file that contains output vector
    """
    A = sc.textFile(A).map(
            lambda line: np.array([float(x) for x in line.split(',')])).cache()
    v = sc.textFile(v).map(
            lambda line: np.array([float(x) for x in line.split(',')])).cache()
    A = A.map(lambda l: (l[0], ((l[1+i], i) for i in range(len(l[1:])))))
    # A_flat_i = A.flatMap(reduce_i)
    A_flat_j = A.flatMap(reduce_j)
    v = v.flatMap(reduce_v)
    A_flat_join = A_flat_j.join(v).map(lambda l: (l[1][0][0],
                                       l[1][0][1]*l[1][1]))
    result = np.array(A_flat_join.reduceByKey(lambda a, b: a + b).
                      map(lambda l: l[1]).collect())
    file = open("matrix_multiply_output.txt", "w")
    pt = ""
    for num in result:
        pt += str(num) + " "
    file.write(pt)
    file.close()


if __name__ == '__main__':
    sc = pyspark.SparkContext(appName="matrix")
    pyspark_matrix(sys.argv[1], sys.argv[2])
    sc.stop()
