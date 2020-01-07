import requests
from bs4 import BeautifulSoup,Comment
import pandas as pd
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import os




problem_text_folder='codeforces_problem_folder\\'
from pathlib import Path



def codeforces_problem_des_extract(problem_url):

    problem_content = requests.get('https://codeforces.com/' +problem_url).text

    # print(problem_content)

    soup = bs(problem_content, 'html.parser')

    problem_statement = []

    for stat in soup.find_all('div', attrs={'class': 'problem-statement'}):
        # print(stat)
        sp = bs(stat.text, 'html.parser')

        for des in soup.find_all('p', ):
            problem_statement.append(des.text)
        for inp_op in soup.find_all('pre'):
            problem_statement.append(inp_op.text)

    # print(len(problem_statement))

    # for i in problem_statement:
    #     print(i)
    return problem_statement




def codeforces_problem_list_extract(url):
    content=requests.get(url).text

    #print(content)

    soup=bs(content,'html.parser')

    problem_name=[]
    dict={

    }
    for prob_name in soup.find_all('a',):
        if bool(re.search('/problemset/problem',prob_name['href'])):
            if prob_name['href'] in dict.keys():
               problem_name.append(prob_name['href'])
            else:
                dict.update({prob_name['href']:1})


    #print(len(problem_name))

    all_problem_des=[]

    for i in range(0,len(problem_name)):
         print(problem_name[i])

         #calling the problem description extractor........

         file_name=problem_name[i]
         path=os.path.normpath(file_name)
         path_list=path.split(os.sep)
         print(path_list)
         file_name=path_list[2]+path_list[3]+path_list[4]


         problem_out_dec=codeforces_problem_des_extract(problem_name[i])
         Path(problem_text_folder+file_name+ '.txt').touch()

         with open(problem_text_folder+file_name+ '.txt','w', encoding="utf-8") as f:
             for item in problem_out_dec:
                 f.write("%s\n"%item)
         #all_problem_des.append(problem_out_dec)



    #Give output the all problem description......
    return  all_problem_des




if __name__ == '__main__':
    url = 'https://codeforces.com/problemset'
    prob_decriptions=[]
    prob_decriptions=codeforces_problem_list_extract(url)

    print(len(prob_decriptions))




