let age = prompt("Enter your age: ")
if (age > 18){
    alert("You can vote")
    document.write("You can vote");
}else{
    alert("You cannot vote");
    document.write("You cannot vote")
}


let marks = prompt("Enter your marks: ")
if (marks >=70){
    alert("First class honors");
}else if (marks >=60 && marks<=69){
    alert("Second class honors");
}else if (marks >=40 && marks<=59){
    alert("Third class honors");
}else{
    alter("Fail Sorry :(!!!")
}

function num(){
    let a = 5;
    if(true){
        let a = 6;
        console.log("if block" + a);
    }
    console.log("out" + a)
}
num();
function num1(){
    var b = 6;
    if(true){
        var b = 7;
        console.log("if block "+b);
    }
    console.log("out"+b)
}
num1()



/*let i;
for (i=1,i<=100, i++){
    if(i%2==0){
        console.log(i);
    }
}*/

const number = [1,2,3,4,5,6,7,8,9,0,9];
let i;

for(i=0;i<number.length,i++){
    console.log(number[i])
}


