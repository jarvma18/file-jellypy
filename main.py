import sys
import json

def splitValuesFromCSV(values):
  valuesList = values.split('\n')
  return valuesList[0].split(',')

def buildJsonObject(keys, values):
  valuesList = splitValuesFromCSV(values)
  jsonObject = {}
  for x in range(len(valuesList)):
    jsonObject[keys[x]] = valuesList[x]
  return jsonObject

def csvToJson(file):
  csvLines = file.readlines()
  csvKeys = csvLines[0]
  keysList = splitValuesFromCSV(csvKeys)
  csvLines.pop(0)
  jsonArray = [];
  for x in range(len(csvLines)):
    jsonObject = buildJsonObject(keysList, csvLines[x])
    jsonArray.append(jsonObject)
  return jsonArray

def appendDataFromJsonToCsv(x, jsonData, csvFile):
  strToAppend = '';
  if x == 0:
    for key in jsonData[x]:
      if len(strToAppend) == 0:
        strToAppend += key
      else:
        strToAppend += ',' + key
    strToAppend += '\n'
    csvFile.write(strToAppend)
    strToAppend = ''
  for key in jsonData[x]:
    if len(strToAppend) == 0:
      strToAppend += jsonData[x][key]
    else:
      strToAppend += ',' + jsonData[x][key]
  strToAppend += '\n'
  csvFile.write(strToAppend)
  return

def main(fileName, convertMode):
  file = open(fileName, 'r')
  if convertMode == 'csvToJson':
    jsonArray = csvToJson(file)
    jsonFileName = fileName.split('.')[0] + '.json'
    jsonFile = open(jsonFileName, 'w')
    json.dump(jsonArray, jsonFile, ensure_ascii=False, indent=2)
  elif convertMode == 'jsonToCsv':
    jsonData = json.load(file);
    csvFileName = fileName.split('.')[0] + '.csv'
    csvFile = open(csvFileName, 'a')
    for x in range(len(jsonData)):
      appendDataFromJsonToCsv(x, jsonData, csvFile)
  print('Job done')

if sys.argv[1] and sys.argv[2]:
  main(sys.argv[1], sys.argv[2])