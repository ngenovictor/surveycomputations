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
                    "<input type='number' id='coordinateX"+point_numbers+"' name='coordinateX"+point_numbers+"' class='form-control'/>"+
                "</div>"+
                "<div  class='input-group'>" +
                    "<div class='input-group-addon'>Y"+point_numbers+"</div>" +
                    "<input type='number' id='coordinateY"+point_numbers+"' name='coordinateY"+point_numbers+"' class='form-control'/>"+
                "</div>"+
            "</div>"
        );
        $("input#point_number_input").attr("value", point_numbers.toString());
        $("span#point_number").text(point_numbers);

    })
});