import pyspark
import numpy as np
import sys


def pt_idx(l):
    # flatMap to format ((centroid key, dimension index),
    #                    (value, 1))
    for i in range(len(l[1])):
        yield((l[0], i), (l[1][i], 1))


def write_txt(input):
    # write finals seeds to txt file
    file = open("final_seeds.txt", "w")
    for i in input:
        pt = ""
        for num in i:
            pt += str(num) + " "
        file.write(pt + "\n")
    file.close()


def pyspark_kmeans(data_file, centroids_file, max_iter=20):
    """
    data_file: txt file name, stores all points
    centroids_file: txt file name, stores starting point
    max_iter: int, maximum iteration limit before stopping
    return: txt file that contains final seeds
    """
    # Load the data
    data = sc.textFile(data_file).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    # Load the initial centroids
    centroids1 = sc.textFile(centroids_file).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).collect()

    centroids = np.array(centroids1[:])
    for iter_count in range(max_iter):
        # group points by centriods
        labeled_data = data.map(lambda l: (np.argmin([np.linalg.norm(l-i)
                                for i in centroids]), (l, 1)))
        # idx_data = labeled_data.flatMap(pt_idx)
        # sum_data = idx_data.reduceByKey(lambda n1, n2: (n1[0] + n2[0],
        #                                 n1[1] + n2[1]))
        # rearrange = sum_data.map(lambda l: (l[0][0], [(l[0][1],
        #                                     l[1][0]/l[1][1])]))
        # group = rearrange.reduceByKey(lambda a, b: a + b).collect()
        group = labeled_data.reduceByKey(
            lambda a, b: (a[0] + b[0], a[1] + b[1])).sortByKey(ascending=True)
        # new_centroids = np.array([[j[1] for j in sorted(i[1])]
        #                          for i in sorted(group)])
        new_centroids = np.array(group.map(
            lambda l: l[1][0]/l[1][1]).collect())
        check = np.linalg.norm(centroids - new_centroids)
        # print(check)
        if check == 0:
            break
        else:
            centroids = new_centroids[:]
        write_txt(centroids)


if __name__ == '__main__':
    sc = pyspark.SparkContext(appName="k-means")
    pyspark_kmeans(sys.argv[1], sys.argv[2], max_iter=20)
    sc.stop()
