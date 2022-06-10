#!/usr/bin/env python3
#
# Python Script for search XSS vulnerability with Knoxss API
# @author: Israel Comazzetto dos Reis [@z3xddd]

from requests import post
from argparse import ArgumentParser

def main():
    print("############################ Knoxss XSS Search #########################")
    print("## Simple Python Script for search XSS Vulnerability using Knoxss API ##")
    print("## @author: Israel Comazzetto dos Reis [@z3xddd]                      ##")
    print("########################################################################")
    argumentsParser = ArgumentParser(description='Python Script for search XSS Vulnerability with Knoxss API')
    argumentsParser.add_argument('-a', '--auth', help='Set Cookie | Authorization for authenticated on Target [EXAMPLE: "Authorization: Bearer value" | "Cookie: value"]', required=False)
    argumentsParser.add_argument('-u','--url', help='Set URL for scan [EXAMPLE: "https://target.com"]', required=False)
    argumentsParser.add_argument('-l','--list', help='Set List URLs for scan [EXAMPLE: listHttpxHostFile]', required=False)
    argumentsParser.add_argument('-k','--key', help='Set API Key Knoxss [EXAMPLE: "apiKeyValue"]', required=True)
    argumentsUser = argumentsParser.parse_args()
    #Cria manual e argumentos

    apiKey = argumentsUser.key
    urlKnoxss = 'https://knoxss.me/api/v3'
    #Atribui valor APIKey e seta URL API Knoxss

    if not argumentsUser.url:
        pass
    #Testa parametro URL
    else:
        if not argumentsUser.auth:
            urlTarget = argumentsUser.url
            contentBodySingleUrl = {'target':urlTarget}
            requestSingleScan = post(urlKnoxss,contentBodySingleUrl,headers={"X-API-KEY":apiKey})
            print(requestSingleScan.text)
        #Recebe URL e faz SCAN
        else:
            authorizationTokenUrl = argumentsUser.auth
            urlTarget = argumentsUser.url
            contentBodySingleUrl = {'target':urlTarget,'auth':authorizationTokenUrl}
            requestSingleScan = post(urlKnoxss,contentBodySingleUrl,headers={"X-API-KEY":apiKey})
            print(requestSingleScan.text)
        #Recebe URL e TOKEN para autenticar no TARGET e faz SCAN

    if not argumentsUser.list:
        pass
    #Testa parametro LIST
    else:
        if not argumentsUser.auth:
            listTarget = argumentsUser.list
            with open(listTarget, "r") as urlList:
                for lineList in urlList:
                    urlTargetList = lineList
                    urlTargetList = urlTargetList.replace("\n","")
                    contentBodyListUrl = {'target':urlTargetList}
                    requestListScan = post(urlKnoxss,contentBodyListUrl,headers={"X-API-KEY":apiKey})
                    print(requestListScan.text)
        #Recebe LISTA URL e faz SCAN
        else:
            authorizationTokenList = argumentsUser.auth
            listTarget = argumentsUser.list
            with open(listTarget, "r") as urlList:
                for lineList in urlList:
                    urlTargetList = lineList
                    urlTargetList = urlTargetList.replace("\n","")
                    contentBodyListUrl = {'target':urlTargetList,'auth':authorizationTokenList}
                    requestListScan = post(urlKnoxss,contentBodyListUrl,headers={"X-API-KEY":apiKey})
                    print(requestListScan.text)
        #Recebe LISTA URL e TOKEN para autenticar no TARGET e faz SCAN

if __name__ == '__main__':
    main()
#Responsavel por realizar a execução de todas as funcoes desenvolvidas