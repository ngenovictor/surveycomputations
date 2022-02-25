
$(document).ready(function(){
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
});