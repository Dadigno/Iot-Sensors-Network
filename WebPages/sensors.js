setInterval(function() { getData(); }, 2000);

function getData() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.status == 200) {
        var obj;
        try{

            obj = JSON.parse(this.response);
            document.getElementById("temp").innerHTML = obj["sensors"]["temp"].value;
            document.getElementById("hum").innerHTML = obj["sensors"]["hum"].value;
            document.getElementById("tank").innerHTML = obj["sensors"]["tank"].value;

            var st = obj["actuators"]["pump"].state;
            if(st == "ON"){
                document.getElementById("pump_bt").innerHTML = "Spegni";
                document.getElementById("pump_state").innerHTML = "ON"
            }else{
                document.getElementById("pump_bt").innerHTML = "Accendi";
                document.getElementById("pump_state").innerHTML = "OFF"
            }
       }
        catch{
            document.getElementById("temp").innerHTML = "nan";
            document.getElementById("hum").innerHTML = "nan";
            document.getElementById("tank").innerHTML = "nan";
        }
    }
  };

  xhttp.open("GET", "resources", true);
  xhttp.send();
}


function postBT(){
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "sensors/actuators?pump", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  var action;
  if(document.getElementById("pump_state").innerHTML == "OFF"){
    action = "ON";
  }else{
    action = "OFF";
  }
  xhttp.send("{\"state\":\""+action+"\"}")
}
