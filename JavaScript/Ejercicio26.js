tipo_cliente =2
compra = 100000

if(tipo_cliente == 1){

    descuento = compra * 0.20
    total = compra - descuento

    console.log("Cliente VIP")
    console.log("Descuento:", descuento)
    console.log("Total:", total)

}
else{

    descuento = compra * 0.05
    total = compra - descuento

    console.log("Cliente Normal")
    console.log("Descuento:", descuento)
    console.log("Total:", total)

}