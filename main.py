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

def main(fileName, convertMode):
  file = open(fileName, 'r')
  if convertMode == 'csvToJson':
    csvLines = file.readlines()
    csvKeys = csvLines[0]
    keysList = splitValuesFromCSV(csvKeys)
    csvLines.pop(0)
    jsonArray = [];
    for x in range(len(csvLines)):
      jsonObject = buildJsonObject(keysList, csvLines[x])
      jsonArray.append(jsonObject)
    jsonFileName = fileName.split('.')[0] + '.json'
    jsonFile = open(jsonFileName, 'w')
    json.dump(jsonArray, jsonFile, ensure_ascii=False, indent=4)
  print('Job done')

if sys.argv[1] and sys.argv[2]:
  main(sys.argv[1], sys.argv[2])