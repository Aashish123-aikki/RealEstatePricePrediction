function onclickedEstimateprice(){
    var bhk=get_bhk();
    var loca=get_location();
    var area=get_area();
    var estimated=document.getElementById('uiEstimatedprice');

    var url="http://127.0.0.1:5000/predict_price";
    $.post(url,{total_sqft:parseFloat(area),bhk:bhk,location:loca},function(data,status){
            if(data){
                estimated.innerHTML="<h2>"+ data.estimatedprice.toString() +"Lakhs</h2>";
            }else{
                console.log("no data")
            }
            });


}
function get_location(){
    uiLocat=document.getElementById("uiLocation");
    return uiLocat.value;
}

function get_bhk(){
    uibhk=document.getElementsByName('uiBHK');
    for(var i in uibhk){
        if(uibhk[i].checked){
            return parseInt(i)+1
        }
    }
    return -1;
}
function get_area(){
    uiarea=document.getElementById('uiSqft');
    return uiarea.value;
}
function onPageLoad(){
    console.log("documant loaded");
    var url= "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status){
        console.log("got response for get_location");
        if(data){
            var location=data.locations;
            var uiLocations=document.getElementById("uiLocation");
            $('#uiLocation').empty();
            for (var i in location){
                var opt= new Option(location[i]);
                $('#uiLocation').append(opt);
            }

        }
    });
}
window.onload=onPageLoad;