'use strict'

document.getElementById('logo').addEventListener('click', checkWindow);

document.getElementById('yesButton').addEventListener('click', yesButton);

document.getElementById('noButton').addEventListener('click', hideWindow);

function showWindow(){
    document.getElementById('returnHomePage').style.display = 'block';
};

function hideWindow(){
    document.getElementById('returnHomePage').style.display = 'none';
};

function checkWindow(){
    let value = document.getElementById('returnHomePage').style.display;
    if (value === 'none'){
        showWindow();
    } else{
        hideWindow();
    }
};

function yesButton(){
    window.location.href = '../';
};

function noButton(){
    hideWindow();
}

