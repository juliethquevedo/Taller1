lado1 = 5
lado2 = 6
lado3 = 7

if(lado1 == lado2 && lado2 == lado3){
    console.log("Equilatero")
}
else if(lado1 == lado2 || lado1 == lado3 || lado2 == lado3){
    console.log("Isosceles")
}
else{
    console.log("Escaleno")
}