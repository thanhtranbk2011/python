#!/usr/bin/python

import csv
import netaddr #need install lib from https://pypi.python.org/pypi/netaddr
from collections import defaultdict
from netaddr import IPAddress,IPNetwork

#Define IP LIST & IP SUB NET LIST
ip_list = []
grid = []
new_list = []
company = []

# Example input
# ip_list = ['10.0.33.44', '10.55.102.1']
# grid  = ['10.0.32.0/23', '239.0.0.0/8', '100.64.0.0/10', '143.127.180.164/30', '10.0.32.0/23' ]


#Add ip from ip_list.csv into ip_list
with open('ip_list.csv','rb') as f:
	ip_list_csv = csv.reader(f)
	for row_ip in ip_list_csv:
		if len(row_ip) != 0:
			ip_list.append(row_ip[0])

#print out to check
#print(ip_list)

columns = defaultdict(list)
#Add network from grid.csv into grid list
with open('grid.csv','rb') as f_subnet: #add input grid IP SUbnets
	ip_subnet_csv = csv.DictReader(f_subnet)
	for row_subnet in ip_subnet_csv:
		for (k, v) in row_subnet.items():  # go over each column name and value
			columns[k].append(v)

grid = columns['Network_and_Mask']
company = columns['Company']

#print out to check
# print(grid)
#Output as [['Company A','Company B'],[[1,2,3],[2,3,4]]]

new_list = []
listCompany = []
listIP = []
listNetWork = []

for Z in grid:
	for X in ip_list:
		if IPAddress(X) in IPNetwork(Z):
			new_list.append(X)
			#check if list company don't include currently company
			if(company[grid.index(Z)] not in listCompany):
				listCompany.append(company[grid.index(Z)])
			#check if list network don't include currently company
			if(grid[grid.index(Z)] not in listNetWork):
				listNetWork.append(grid[grid.index(Z)])
	if len(new_list)!=0:
		listIP.append(new_list)
		new_list=[]

#List of IP exists in of the networks with index as same company
print(listIP) 

#List of network
print(listNetWork)

#List of Company
print(listCompany)