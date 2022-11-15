var url = "http://127.0.0.1:5000/view";
var id = "view";

async function generator(url, id) {
  var request = await new XMLHttpRequest();

  request.open("GET", url, true);
  request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);
    view(data, request, id);
  };

  request.send();
}

function view(data, request, id) {
  if (id == "view") {
    if (request.status >= 200 && request.status < 400) {
      data.forEach((query) => {
        console.log(request.status);
        var div = document.createElement("tr");
        var div2 = document.createElement("tr");
        var mainContainer2 = document.getElementById("view2");
        var mainContainer = document.getElementById(id);
        div.innerHTML = "<td>"+query.Id+"</td><td><input id='RegNumber"+query.Id+"'  value='"+query.RegNumber+"'/></td><td><input id='Brand"+query.id+"'  value='"+query.Brand+"'/></td><td><input id='Model"+query.id+"'  value='"+query.Model+"'/></td><td><input id='Year"+query.id+"'  value='"+query.Year+"'/></td><td><input id='Hp"+query.id+"'  value='"+query.Hp+"'/></td>";
        div2.innerHTML = "<td>"+query.Id+"</td><td><input id='RegNumber"+query.Id+"'  value='"+query.RegNumber+"'/></td><td><input id='Color"+query.id+"'  value='"+query.Color+"'/></td><td><input id='Fuel"+query.id+"' value='"+query.Fuel+"'/></td><td><input id='ShiftType"+query.id+"' value='"+query.ShiftType+"'/></td><td><input id='DailyPrice"+query.id+"' value='"+query.DailyPrice+"'/></td>";
        mainContainer.appendChild(div);
        mainContainer2.appendChild(div2);
      });
    } else {
      console.log("error");
    }
  }
}

async function generate_html() {
  await generator(url, id);
}

function deleterecord(Id) {
  const data = JSON.stringify({
    Id: parseInt(document.getElementById("RegNumber")),
  });
  navigator.sendBeacon("http://127.0.0.1:5000/deleterecord/", data);
  console.log(data);
}


generate_html();
