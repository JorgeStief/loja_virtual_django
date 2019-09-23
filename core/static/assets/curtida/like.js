$(".click1").click(function() {
    
    let like = $("#like").data("like")
    let dislike = $("#dislike").data("dislike")
    if($(".click1").hasClass("fas fa-thumbs-up")){

        like--;
        $("#like").data("like",like);
        $(".click1").removeClass("fas fa-thumbs-up").addClass("far fa-thumbs-up"); 

    }else{

        like++;
        $(".click1").removeClass("far fa-thumbs-up").addClass("fas fa-thumbs-up");
        $("#like").data("like",like);

        if($(".click2").hasClass("fas fa-thumbs-down")){
            dislike--;
            $("#dislike").data("dislike",dislike);
            $(".click2").removeClass("fas fa-thumbs-down").addClass("far fa-thumbs-down");
        }
    }
    
    $("#like").text(like)
    $("#dislike").text(dislike)
 })

 $(".click2").click(function() {
    
    let like = $("#like").data("like")
    let dislike = $("#dislike").data("dislike")
    if($(".click2").hasClass("fas fa-thumbs-down")){
        dislike--;
        
        $("#dislike").data("dislike",dislike);
        $(".click2").removeClass("fas fa-thumbs-down").addClass("far fa-thumbs-down");

        
    }else{
        dislike++;
        $(".click2").removeClass("far fa-thumbs-down").addClass("fas fa-thumbs-down");
        $("#dislike").data("dislike",dislike);

        if($(".click1").hasClass("fas fa-thumbs-up")){
            like--;
            $("#like").data("like",like);
            $(".click1").removeClass("fas fa-thumbs-up").addClass("far fa-thumbs-up");
        }
    }
    
    $("#like").text(like)
    $("#dislike").text(dislike)
 })