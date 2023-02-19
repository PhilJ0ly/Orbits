// import * as fs from fs
const fs = require("fs");
const parser = require("csv-parser");

const seperator = ",";
const planets = [
    "mercury",
    "venus",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "sun",
];

const read = (path) => {
    const csv = fs.readFileSync(path);
    const array = csv.toString().split(seperator);
    return array;
};

const baseUrl = "../DATA/";
const dict = {};

for (let i = 0; i < planets.length; i++) {

    fs.createReadStream(`${baseUrl}${planets[i]}.csv`)
        .pipe(parser())
        .on("data", (data) => {
            Object.assign(dict, data);
            console.log(data)
        });
    // const path = `${baseUrl}${planets[i]}.csv`;
    // dict[planets[i]] = read(path);
}
console.log(dict);
