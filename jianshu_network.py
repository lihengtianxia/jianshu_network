import pymysql
import pandas as pd
import numpy as np
import networkx as nx
import community
import matplotlib.pyplot as plt

conn = pymysql.connect(host='localhost',user='root',password='123456',database='jianshu',port=3306,charset='utf8')
cursor = conn.cursor()
sql = """
select usera,userb from infosnew2
"""
cursor.execute(sql)
#从数据库中读取用户对信息
userpairs = cursor.fetchall()
conn.close()

#社交图谱建立与计算
G=nx.DiGraph()
G.add_edges_from(userpairs)

degree = nx.degree(G)      #程度中心性
in_degree_ = nx.in_degree_centrality(G) #入度
closeness_centrality = nx.closeness_centrality(G) #紧密中心性
betweenness_centrality = nx.betweenness_centrality(G) #介数中心性
eigenvector_centrality = nx.eigenvector_centrality(G)  #高特征向量中心性
pagerank = nx.pagerank(G)  #pagerank算法
clustering = nx.clustering(G) #群聚系数

verage_shortest_path_length = nx.average_shortest_path_length(G) #图G所有节点间平均最短路径长度（结果为0.00040136391084636026）
path=nx.all_pairs_shortest_path(G)

G=nx.Graph()
G.add_edges_from(userpairs)
clustering = nx.clustering(G) #群聚系数

score = sorted(eigenvector_centrality.items(), key=lambda item:item[1], reverse = True)
k = 0
for i in score:
    print(i[0],i[1])
    k+=1
    if k >= 10:
        break
