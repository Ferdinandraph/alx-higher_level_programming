#!/usr/bin/bash
const check = process.argv;
console.log(typeof check[2] === 'undefined' ? 'No argument' : check[2]);
