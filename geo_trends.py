# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:50:42 2021

@author: Lenovo
"""
import pandas as pd
import numpy as np
import os
from scipy import stats


country = pd.read_excel('countriesss.xlsx')
country['Name']=country['Name'].str.lower()
country['Name']=np.where((country['Name']=='india') | (country['Name']=='russia'), country['Name'], country['Name']+' ')
country['Name']=' '+country['Name']
countries= country['Name'].to_list()
country=country.set_index('Name')


country['count']=0
f = open('dblpv13.json','r', encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break

    if(line.find('"org" :') != -1):
        org = line.strip()
        org = org[9:]
        if org[-1]==',': org = org[:-1]
        if org[-1]=='"': org = org[:-1]
        org=org.lower()
        org = ' '+org+' '
        for c in countries:
            if c in org: 
                country['count'][c]+=1
f.close()




for i in range(1980,2022):
    country[i]=0
country['citations']=0
tit=0
auth=0
orgs=0
cites=0
f = open('dblpv13.json','r', encoding='utf-8')
while True:
    line = f.readline()
    if(line=='{ \n'):
        tit+=1
        desh=[]
        cite=0
        year=0
        while (line!='},\n'):
            line = f.readline()
            if not line: break
            if(line.find('"name" :') != -1):
                auth+=1
            if(line.find('"org" :') != -1):
                orgs+=1
                org = line.strip()
                org = org[9:]
                if org[-1]==',': org = org[:-1]
                if org[-1]=='"': org = org[:-1]
                org=org.lower()
                org = ' '+org+ ' '
                for c in countries:
                    if c in org: 
                        desh.append(c)
            if(line.find('"n_citation" :') != -1):
                cite = line.strip()
                cite = cite[25:]
                if cite[-1]==',': cite = cite[:-1]
                if cite[-1]==')': cite = cite[:-1]
                cite=int(cite)
                cites+=1
            if(line.find('"year" :') != -1):
                year = line.strip()
                year = year[19:]
                if year[-1]==',': year = year[:-1]
                if year[-1]==')': year = year[:-1]
                year=int(year)
        if year>1979 and year<2022: 
            for c in desh:
                country[year][desh]+=1
                if cite: country['citations'][desh]+=cite
            
    if not line:break
f.close()
country['total']=0
for i in range(1980,2022):
    country['total']+=country[i]

country.to_csv('geo_trends.csv')
print('Total papers: ',tit)
print('Sum of authors :',auth)
print('Authors with orgs mentioned :',  orgs)
print('Papers with citations: ',cites)
print('orgs/authors',orgs/auth)
print('orgs with country mentioned',country['total'].sum())
print('(country found)/(total orgs found',country['total'].sum()/orgs)
