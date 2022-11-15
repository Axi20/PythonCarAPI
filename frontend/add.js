function sendPost() {
  const data = JSON.stringify({
    regNumber: document.getElementById("RegNumber").value,
    brand: document.getElementById("Brand").value,
    model: document.getElementById("Model").value,
    year: document.getElementById("Year").value,
    hp: document.getElementById("Hp").value,
    color: document.getElementById("Color").value,
    fuel: document.getElementById("Fuel").value,
    shiftType: document.getElementById("ShiftType").value,
    dailyPrice: document.getElementById("DailyPrice").value
  });
  navigator.sendBeacon("http://127.0.0.1:5000/savedetails/", data);
  console.log(data);
  alert("Adat sikeresen hozzáadva!", data);
}


function deleteRecord(){
  const data = JSON.stringify({
    regNumber: document.getElementById("RegNumber").value,
  });
  navigator.sendBeacon("http://127.0.0.1:5000/deleterecord/",data);
  console.log(data);
  alert("Adat sikeresen törölve!", data);
}


function getSelectedValue(){
  var selectedValue = document.getElementById("list").value;
  // console.log(selectedValue);
}

function updateCar(){
  const data = JSON.stringify({
    listItem: document.getElementById("list").value,
    regNumber: document.getElementById("RegNumber").value,
    valueToUpdate: document.getElementById("ItemToUpdate").value
  });
  navigator.sendBeacon("http://127.0.0.1:5000/updatedetails/",data);
  console.log(data);
  alert("Adat sikeresen frissítve!", data);
}
