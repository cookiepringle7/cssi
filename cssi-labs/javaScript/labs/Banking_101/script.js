// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name,mybalance = 0){
  balance=mybalance;

  customer_name=name;// Set the value for customer_name equal to name below

  return name +" has opened a new account with a balance of $" + balance;//write the statment you need to return here
}

function deposit(value){
balance = balance + value;
let msg = `${customer_name} has deposited ${value}. ${customer_name}'s total balance is ${balance}.`;
  return msg; // update the value of balance
  //return the correct statement
}

function withdraw(amount){
if (amount > balance){
  let difference = amount - balance;
  return `Sorry, ${customer_name}, you do not have enough money in your account. You need ${difference} more dollars.`;
}
  balance = balance - amount;
  let mg = `${customer_name} has withdraw ${amount}. ${customer_name} has ${balance} remaining.`;
  return mg;//updatethe value of balance
  //return the correct statement
}
console.log("script is running...");
console.log(openAccount("James",300));
console.log(deposit(50));
console.log(withdraw(500));
