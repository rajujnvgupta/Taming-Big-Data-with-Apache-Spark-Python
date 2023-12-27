from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local").setAppName("MaximumTemperature")

sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3])*0.1*(9.0/5.0) + 32.0
    return (stationID, entryType, temperature)

lines = sc.textFile("1800.csv")
parsedLine = lines.map(parseLine)
maxTemps = parsedLine.filter(lambda x : "TMAX" in x[1])
stationsTemps = maxTemps.map(lambda x : (x[0], x[2]))
maxTemps = stationsTemps.reduceByKey(lambda x, y : max(x, y))
results = maxTemps.collect()

for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))

