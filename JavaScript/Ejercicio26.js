tipo=1
compra=100000
if(tipo==1){
    descuento=compra*0.20
}
else{
    descuento=compra*0.05
}
total=compra-descuento
console.log("Total a pagar:",total)