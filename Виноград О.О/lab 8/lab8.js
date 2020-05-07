const mongo = require('mongodb').MongoClient
const url = "mongodb://lab:lab@localhost"
const csv = require('csvtojson')
const express = require('express')
const jsonParser = express.json();
const app = express()
const port = 3000

app.post('/convert', jsonParser, (request, response) => {
    csv()
        .fromString(request.body.data)
        .then((jsonObj) => {
            response.send(jsonObj)
        })
})

app.post('/save', jsonParser, (request, response) => {
    let data = request.body.data;
    executeMongoRequest((err, collection) => {
        collection.insertMany(data, (err, result) => {
            if (err) {
                response.send(err)
                return console.log(err)
            }
            console.log(result.ops)
            response.send(result.ops)
        })
    })
})

app.get("/sortedUrlList", jsonParser, (request, response) => {
    executeMongoRequest((error, collection) => {
        collection.find({}, {fields: {URL: 1}}).sort({URL: 1}).toArray((error, result) => {
            response.send(result)
        })
    })
})

app.get("/sortedByIpListWithUrl", jsonParser, (request, response) => {
    executeMongoRequest((error, collection) => {
        let url = request.query.url
        collection.find({URL: url}, {fields: {IP: 1}}).sort({IP: 1}).toArray((error, result) => {
            response.send(result)
        })
    })
})

app.get("/sortedByUrlListWithIp", jsonParser, (request, response) => {
    executeMongoRequest((error, collection) => {
        let ip = request.query.ip
        collection.find({IP: ip}, {fields: {URL: 1}}).sort({URL: 1}).toArray((error, result) => {
            response.send(result)
        })
    })
})

app.get("/sortedUrlListWithinPeriod", jsonParser, (request, response) => {
    executeMongoRequest((error, collection) => {
        let start = request.query.start
        let end = request.query.end
        collection.find({timeStamp: {$gte: start, $lte: end}}, {fields: {URL: 1}}).sort({URL: 1})
            .toArray((error, result) => {
                response.send(result)
            })
    })
})

function mapReduceByTimeSpent() {
    emit(this.URL, this.timeSpent);
}

function reduceReduceByTimeSpent(keyURL, valuesTimeSpents) {
    return valuesTimeSpents.reduce((a, b) => Number.parseInt(a) + Number.parseInt(b))
}

app.get("/reduceByTimeSpent", jsonParser, (request, response) => {
    mongo.connect(url, (err, client) => {
        client.db("lab").collection("reduceByTimeSpent").drop({});
        client.close()
    })
    executeMongoRequest((error, collection) => {
        collection.mapReduce(
            mapReduceByTimeSpent,
            reduceReduceByTimeSpent,
            {out: "reduceByTimeSpent"}
        );
    })
    mongo.connect(url, (err, client) => {
        client.db("lab").collection("reduceByTimeSpent").find({}).sort({_id: -1}).toArray((err, result) => {
            if(err) {
                response.send(err)
            }
            response.send(result)
        })
        client.close()
    })
})

function reduceReduceByCount(keyURL, valuesTimeSpents) {
    return valuesTimeSpents.length;
}

app.get("/reduceByCount", jsonParser, (request, response) => {
    mongo.connect(url, (err, client) => {
        client.db("lab").collection("reduceByCount").drop({});
        client.close()
    })
    executeMongoRequest((error, collection) => {
        collection.mapReduce(
            mapReduceByTimeSpent,
            reduceReduceByCount,
            {out: "reduceByCount"}
        );
    })
    mongo.connect(url, (err, client) => {
        client.db("lab").collection("reduceByCount").find({}).sort({_id: -1}).toArray((err, result) => {
            if(err) {
                response.send(err)
            }
            response.send(result)
        })
        client.close()
    })
})

app.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }
    console.log(`server is listening on ${port}`)
})

function executeMongoRequest(request) {
    mongo.connect(url, (err, client) => {
        request(err, client.db("lab").collection("lab"))
        client.close()
    })
}


// Use it to drop the collection
/*
mongo.connect(url, function (err, client) {
    executeMongoRequest((error, collection) => {
        collection.drop({}, (error, result) => console.log(result))
        collection.find({}).toArray((error, result) => {
            if (error) throw error;
            console.log("Collection data successfully removed");
        });
    })
})
*/

