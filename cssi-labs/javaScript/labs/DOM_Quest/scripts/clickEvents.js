// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
console.log("Running Click Events Script");
const colors=['red','pink','orange','yellow','blue','purple'];
let box1 = document.querySelector('#box1');
let box2 = document.querySelector('#box2');
let box3 = document.querySelector('#box3');
let box4 = document.querySelector('#box4');
let box5 = document.querySelector('#box5');
let box6 = document.querySelector('#box6');
let box7 = document.querySelector('#box7');

box1.addEventListener('click',switchcolor0);

box2.addEventListener('click',switchcolor1);

box3.addEventListener('click',switchcolor2);

box4.addEventListener('click',switchcolor3);

box5.addEventListener('click',switchcolor4);



function switchcolor0 () {

box1.style.backgroundColor=colors[0];
box2.style.backgroundColor=colors[0];
box3.style.backgroundColor=colors[0];
}

function switchcolor1 () {

box1.style.backgroundColor=colors[1];
box2.style.backgroundColor=colors[1];
box3.style.backgroundColor=colors[1];
}

function switchcolor2 () {

box1.style.backgroundColor=colors[2];
box2.style.backgroundColor=colors[2];
box3.style.backgroundColor=colors[2];
}

function switchcolor3 () {

  box4.style.backgroundColor=colors[3];
  box5.style.backgroundColor=colors[3];
}

function switchcolor4 () {

  box4.style.backgroundColor=colors[4];
  box5.style.backgroundColor=colors[4];
}


function switchcolor5 () {

  box1.style.backgroundColor=colors[3];
  box2.style.backgroundColor=colors[3];
  box3.style.backgroundColor=colors[3];

  box4.style.backgroundColor=colors[3];
  box5.style.backgroundColor=colors[3];

}
