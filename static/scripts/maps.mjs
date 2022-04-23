'use strict';
import fs from 'file-system';
import { readFile, readFileSync } from 'fs';


let distance_url = 'https://api.mapbox.com/directions/v5/mapbox/cycling/';

// Longitude is stored first and then latitude
let cities_coord = {
    'Monaco City' : [7.416667, 43.733334],
    'Genoa': [8.942184, 44.414165],
    'Valencia': [-0.375000, 39.466667], 
    'Barcelona': [2.168365, 41.346176], 
    'Amsterdam': [4.897070, 52.377956],
    'Dusseldorf': [6.783333, 51.233334],
    'Hamburg': [9.993682, 53.551086],
    'Copenhagen': [12.568337, 55.676098]
};

const key_loc = 'C:/Users/Konstantinos/Desktop/Oregon State University/CS 361/maps_token.txt';

function accessKey(){

    // Get the key for the map service
    let text = readFileSync(key_loc, 'utf-8');
    
    return text.toString();
};

function getCityCoordinates(city){
    return cities_coord[city];
}

export default function get_Map(start_city){
    coordinates = getCityCoordinates(start_city)
    mapboxgl.accessToken = accessKey();
    const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/streets-v11', // style URL
    center: coordinates, // starting position [lng, lat]
    zoom: 9 // starting zoom
    });
}


document.addEventListener('load', ()=>{
    getElementById('map').appendChild(get_Map('Genoa'));
});

                