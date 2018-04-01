import pymysql
import pandas as pd
import numpy as np
import networkx as nx
import community
import matplotlib.pyplot as plt

conn = pymysql.connect(host='localhost',user='root',password='123456',database='jianshu',port=3306,charset='utf8')
cursor = conn.cursor()
sql = """
select usera,userb,weights from infos5
"""
cursor.execute(sql)
#从数据库中读取用户对信息
userpairs = cursor.fetchall()
conn.close()

#社交图谱建立与计算
G=nx.Graph()
G.add_weighted_edges_from(userpairs)


#社区发现算法 best_partition
partition = community.best_partition(G)
# drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
                                node_color = str(count / size))

nx.draw_networkx_edges(G,pos, alpha=0.5)
plt.show()

#社区发现算法 best_partition
k_clique = list(nx.k_clique_communities(G,3))