// Funktion för att hämta tal från inmatningsfälten
function hämtaTal() {
  const tal1 = parseFloat(document.getElementById("tal1").value);
  const tal2 = parseFloat(document.getElementById("tal2").value);
  return { tal1, tal2 };
}

// Funktion för att beräkna summan av talen
function beräknaSumma(tal) {
  const summa = tal.tal1 + tal.tal2;
  return summa;
}

// Funktion för att visa resultatet i en ruta
function visaResultat(summa) {
  alert(`Summan av talen är: ${summa}`);
}

// Händelsehanterare för submit-knappen
document.getElementById("submitButton").addEventListener("click", function () {
  const tal = hämtaTal();
  const summa = beräknaSumma(tal);
  visaResultat(summa);
});
