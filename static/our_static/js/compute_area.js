$(document).ready(function(){
    var point_numbers = 3;
    $("#add-coordinate-inputs").click(function (event) {
        event.preventDefault();
        point_numbers+=1;
        console.log(point_numbers);
        $("#point-inputs").append(
            "<div class='form-group'>"+
                "<div  class='input-group'>" +
                    "<div class='input-group-addon'>X"+point_numbers+"</div>" +
                    "<input type='number' id='coordinateX"+point_numbers+"' name='coordinateX"+point_numbers+"' class='form-control' required/>"+
                "</div>"+
                "<div  class='input-group'>" +
                    "<div class='input-group-addon'>Y"+point_numbers+"</div>" +
                    "<input type='number' id='coordinateY"+point_numbers+"' name='coordinateY"+point_numbers+"' class='form-control' required/>"+
                "</div>"+
            "</div>"
        );
        $("input#point_number_input").attr("value", point_numbers.toString());
        $("span#point_number").text(point_numbers);

    });
    $("form#feedback_form").submit(function (event) {
        event.preventDefault();
        var name = $("input#feed_back_name").val();

        var email = $("input#feed_back_email").val();

        var message = $("textarea#feed_back_message").val();

        message = message.replace(/(?:\n)/g, '<putNewLineHere>');

        var feedback_url = $("input#feedback_url").val();

        $("#feed_back_inputs").modal("toggle");

        $.ajax({
            url:feedback_url+"?name="+name+"&&email="+email+"&&message="+message,
            success:function(data){
                console.log(data);
                $("#feedback_message").text(data["message"]);
                $("#thank_you_feedback").modal("toggle");
            }
        })
    });
    var osmlayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.streets'
    });
    var none_layer = L.tileLayer('', {
        maxZoom: 18,
        attribution: 'Empty'
    });
    var map = L.map('map', {
        center: [-1.0500, 37.0833],
        zoom: 10,
        minZoom: 2,
        maxZoom: 18,
        zoomControl: false,
        layers: [osmlayer,]
    });
});