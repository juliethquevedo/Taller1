año = 2026

if((año % 4 == 0 && año % 100 != 0) || (año % 400 == 0)){
    console.log("Es bisiesto")
}
else{
    console.log("No es bisiesto")
}
