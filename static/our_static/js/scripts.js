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
        $("#feed_back_inputs").modal("toggle");
        console.log("clicked submit");
        $.ajax({
            url:"http://localhost:8000/give_feedback",
            success:function(data){
                console.log(data);
                $("#feedback_message").text(data["message"]);
                $("#thank_you_feedback").modal("toggle");
            }
        })
    })
});